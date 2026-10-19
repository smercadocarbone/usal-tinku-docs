#!/usr/bin/env python3
"""Diccionario de datos y diagramas entidad-relación de Tinku, generados del esquema real.

El esquema se obtiene aplicando las migraciones Flyway del sistema en un PostgreSQL
(ver scripts/esquema_desde_migraciones.sh) e introspeccionando pg_catalog. El script
tiene dos pasos, que pueden correrse juntos o por separado:

  introspectar  lee la base (variables PG*: PGHOST, PGPORT, PGUSER, PGPASSWORD,
                PGDATABASE) y guarda scripts/esquema_tinku.json. Si se indica la
                ruta del repositorio del sistema, registra además en qué migraciones
                se crea o altera cada tabla y cuál es la última migración.
  generar       a partir de ese JSON y de scripts/descripciones_esquema.py emite
                apendices/C-diccionario-datos.tex y los diagramas
                figuras/der/*.dot (+ .pdf, con Graphviz).

Uso:
  python3 scripts/diccionario_datos.py introspectar --repo /ruta/a/usal-tinku
  python3 scripts/diccionario_datos.py generar
  python3 scripts/diccionario_datos.py todo --repo /ruta/a/usal-tinku
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_ESQUEMA = RAIZ / "scripts" / "esquema_tinku.json"
TEX_SALIDA = RAIZ / "apendices" / "C-diccionario-datos.tex"
DIR_DER = RAIZ / "figuras" / "der"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from descripciones_esquema import ESQUEMAS, TABLAS, COLUMNAS  # noqa: E402

# Esquemas de dominio, en el orden de los módulos (M1..M9).
ORDEN_ESQUEMAS = ["identidad", "matching", "aula", "reservas", "pagos",
                  "resumen", "reputacion", "admin", "seguridad"]

# ---------------------------------------------------------------------------
# 1. Introspección
# ---------------------------------------------------------------------------

SQL_INTROSPECCION = r"""
WITH tablas AS (
    SELECT c.oid, n.nspname AS esquema, c.relname AS tabla
    FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
    WHERE c.relkind IN ('r', 'p')
      AND n.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
)
SELECT json_build_object(
  'tablas', (SELECT json_agg(json_build_object(
      'esquema', t.esquema,
      'tabla', t.tabla,
      'comentario', obj_description(t.oid, 'pg_class'),
      'columnas', (SELECT json_agg(json_build_object(
              'nombre', a.attname,
              'tipo', format_type(a.atttypid, a.atttypmod),
              'no_nulo', a.attnotnull,
              'default', pg_get_expr(d.adbin, d.adrelid),
              'comentario', col_description(t.oid, a.attnum)
          ) ORDER BY a.attnum)
          FROM pg_attribute a
          LEFT JOIN pg_attrdef d ON d.adrelid = a.attrelid AND d.adnum = a.attnum
          WHERE a.attrelid = t.oid AND a.attnum > 0 AND NOT a.attisdropped),
      'restricciones', (SELECT coalesce(json_agg(json_build_object(
              'nombre', k.conname,
              'tipo', k.contype,
              'columnas', (SELECT json_agg(a.attname ORDER BY x.ord)
                           FROM unnest(k.conkey) WITH ORDINALITY x(attnum, ord)
                           JOIN pg_attribute a ON a.attrelid = k.conrelid AND a.attnum = x.attnum),
              'ref_esquema', rn.nspname,
              'ref_tabla', rc.relname,
              'ref_columnas', (SELECT json_agg(a.attname ORDER BY x.ord)
                               FROM unnest(k.confkey) WITH ORDINALITY x(attnum, ord)
                               JOIN pg_attribute a ON a.attrelid = k.confrelid AND a.attnum = x.attnum),
              'al_borrar', k.confdeltype,
              'definicion', pg_get_constraintdef(k.oid)
          ) ORDER BY k.contype, k.conname), '[]'::json)
          FROM pg_constraint k
          LEFT JOIN pg_class rc ON rc.oid = k.confrelid
          LEFT JOIN pg_namespace rn ON rn.oid = rc.relnamespace
          WHERE k.conrelid = t.oid),
      'indices', (SELECT coalesce(json_agg(json_build_object(
              'nombre', ic.relname,
              'unico', i.indisunique,
              'definicion', pg_get_indexdef(i.indexrelid)
          ) ORDER BY ic.relname), '[]'::json)
          FROM pg_index i JOIN pg_class ic ON ic.oid = i.indexrelid
          WHERE i.indrelid = t.oid
            AND NOT EXISTS (SELECT 1 FROM pg_constraint k WHERE k.conindid = i.indexrelid
                                                          AND k.conrelid = t.oid))
  ) ORDER BY t.esquema, t.tabla) FROM tablas t),
  'extensiones', (SELECT json_agg(json_build_object('nombre', extname, 'version', extversion)
                  ORDER BY extname) FROM pg_extension),
  'version_postgres', current_setting('server_version')
);
"""


def introspectar(repo: Path | None) -> dict:
    salida = subprocess.run(
        ["psql", "-X", "-A", "-t", "-v", "ON_ERROR_STOP=1", "-c", SQL_INTROSPECCION],
        check=True, capture_output=True, text=True).stdout
    datos = json.loads(salida)
    datos["migraciones"] = {}
    if repo is not None:
        dir_mig = repo / "backend" / "src" / "main" / "resources" / "db" / "migration"
        archivos = sorted(dir_mig.glob("V*.sql"),
                          key=lambda p: int(re.match(r"V(\d+)__", p.name).group(1)))
        ultima = archivos[-1]
        fecha = subprocess.run(
            ["git", "-C", str(repo), "log", "-1", "--format=%cs", "--", str(ultima)],
            check=True, capture_output=True, text=True).stdout.strip()
        commit = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "--short", "HEAD"],
            check=True, capture_output=True, text=True).stdout.strip()
        datos["ultima_migracion"] = {"archivo": ultima.name, "fecha": fecha,
                                     "commit_repo": commit,
                                     "cantidad": len(archivos)}
        # En qué migraciones se crea o altera cada tabla (sin comentarios SQL).
        for t in datos["tablas"]:
            nombre = re.escape(f"{t['esquema']}.{t['tabla']}")
            patron = re.compile(
                r"(CREATE\s+TABLE|ALTER\s+TABLE|\bON)\s+(IF\s+NOT\s+EXISTS\s+)?"
                + nombre + r"\b", re.IGNORECASE)
            versiones = []
            for f in archivos:
                texto = "\n".join(l.split("--")[0] for l in f.read_text().splitlines())
                if patron.search(texto):
                    versiones.append(int(re.match(r"V(\d+)__", f.name).group(1)))
            datos["migraciones"][f"{t['esquema']}.{t['tabla']}"] = versiones
    datos["generado"] = dt.date.today().isoformat()
    return datos


# ---------------------------------------------------------------------------
# 2. Utilidades de formato
# ---------------------------------------------------------------------------

_ESCAPES = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
            "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
            "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}


def esc(texto: str) -> str:
    return "".join(_ESCAPES.get(c, c) for c in texto)


def tt(texto: str) -> str:
    """Texto monoespaciado que puede cortarse después de _ . , ( y espacios."""
    s = esc(texto)
    s = s.replace(r"\_", r"\_\allowbreak{}").replace(".", r".\allowbreak{}")
    s = s.replace(",", r",\allowbreak{}").replace("(", r"(\allowbreak{}")
    return r"\texttt{" + s + "}"


def prosa(texto: str) -> str:
    """Escapa la descripción y convierte `codigo` en monoespaciado cortable."""
    partes = texto.split("`")
    return "".join(tt(p) if i % 2 else esc(p) for i, p in enumerate(partes))


def simplificar_expr(expr: str) -> str:
    """Hace legible una expresión de pg_get_constraintdef / pg_get_indexdef."""
    s = expr
    s = re.sub(r"::(character varying|text|bpchar|integer|numeric|jsonb|uuid|date|"
               r"timestamp with time zone|timestamp without time zone|time without time zone)"
               r"(\[\])?", "", s)
    # (col = ANY (ARRAY['a', 'b'])) -> col IN ('a', 'b')
    s = re.sub(r"\(?(\w+)\)? = ANY \(\(?ARRAY\[(.*?)\]\)?\)",
               lambda m: f"{m.group(1)} IN ({m.group(2)})", s)
    s = re.sub(r"\((\w+)\)", r"\1", s)            # (col) -> col
    s = re.sub(r"\(\((.*)\)\)", r"(\1)", s)        # ((...)) -> (...)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def tipo_corto(tipo: str) -> str:
    reemplazos = {
        "timestamp with time zone": "timestamptz",
        "timestamp without time zone": "timestamp",
        "time without time zone": "time",
        "character varying": "varchar",
        "double precision": "float8",
        "boolean": "boolean",
    }
    for largo, corto in reemplazos.items():
        tipo = tipo.replace(largo, corto)
    return tipo


def default_corto(d: str | None) -> str:
    if d is None:
        return ""
    d = re.sub(r"::(character varying|text|jsonb|uuid\[\]|integer)", "", d)
    return d


# ---------------------------------------------------------------------------
# 3. Diccionario de datos (LaTeX)
# ---------------------------------------------------------------------------

def claves_columna(t: dict) -> dict[str, list[str]]:
    """Etiquetas cortas por columna: PK, FK, UQ, CK."""
    marcas: dict[str, list[str]] = {c["nombre"]: [] for c in t["columnas"]}
    for k in t["restricciones"]:
        cols = k["columnas"] or []
        if k["tipo"] == "p":
            for c in cols:
                marcas[c].append("PK")
        elif k["tipo"] == "f":
            destino = f"{k['ref_esquema']}.{k['ref_tabla']}"
            for c in cols:
                marcas[c].append("FK " + destino)
        elif k["tipo"] == "u":
            for c in cols:
                marcas[c].append("UQ" if len(cols) == 1 else "UQ*")
        elif k["tipo"] == "c":
            for c in cols:
                if "CK" not in marcas[c]:
                    marcas[c].append("CK")
        elif k["tipo"] == "x":
            for c in cols:
                if "EX" not in marcas[c]:
                    marcas[c].append("EX")
    for i in t["indices"]:
        if i["unico"]:
            m = re.search(r"\((.*?)\)", i["definicion"])
            cols = [c.strip() for c in m.group(1).split(",")] if m else []
            for c in cols:
                if c in marcas and not any(x.startswith("UQ") for x in marcas[c]):
                    marcas[c].append("UQ" if len(cols) == 1 else "UQ*")
    return marcas


def formato_clave(etiqueta: str) -> str:
    if etiqueta.startswith("FK "):
        return r"FK\,$\rightarrow$\," + tt(etiqueta[3:])
    return etiqueta


_BORRADO = {"c": "ON DELETE CASCADE", "n": "ON DELETE SET NULL", "d": "ON DELETE SET DEFAULT",
            "r": "ON DELETE RESTRICT"}


def notas_restricciones(t: dict) -> list[str]:
    """Restricciones de tabla (CHECK, UNIQUE compuestas, EXCLUDE) e índices adicionales."""
    lineas = []
    for k in t["restricciones"]:
        if k["tipo"] == "c":
            lineas.append(r"\textsc{ck} " + tt(k["nombre"]) + ": "
                          + tt(simplificar_expr(k["definicion"])))
        elif k["tipo"] == "u" and len(k["columnas"]) > 1:
            lineas.append(r"\textsc{uq} " + tt(k["nombre"]) + ": "
                          + tt(simplificar_expr(k["definicion"])))
        elif k["tipo"] == "p" and len(k["columnas"]) > 1:
            lineas.append(r"\textsc{pk} compuesta: " + tt(", ".join(k["columnas"])))
        elif k["tipo"] == "x":
            lineas.append(r"\textsc{ex} " + tt(k["nombre"]) + ": "
                          + tt(simplificar_expr(k["definicion"])))
        elif k["tipo"] == "f" and k["al_borrar"] in _BORRADO:
            lineas.append(r"\textsc{fk} " + tt(k["nombre"]) + ": " + _BORRADO[k["al_borrar"]])
    for i in t["indices"]:
        d = i["definicion"]
        d = re.sub(r"^CREATE (UNIQUE )?INDEX \S+ ON \S+ ", "", d)
        d = d.replace("USING btree ", "")
        prefijo = r"\textsc{ix único} " if i["unico"] else r"\textsc{ix} "
        lineas.append(prefijo + tt(i["nombre"]) + ": " + tt(simplificar_expr(d)))
    return lineas


def tabla_tex(t: dict, migs: list[int]) -> str:
    clave = f"{t['esquema']}.{t['tabla']}"
    desc_tabla = TABLAS.get(clave)
    if desc_tabla is None:
        raise SystemExit(f"Falta la descripción de la tabla {clave}")
    marcas = claves_columna(t)
    ancho = (r"\begin{longtable}{@{}>{\raggedright\arraybackslash}p{2.55cm}"
             r">{\raggedright\arraybackslash}p{1.8cm}"
             r">{\centering\arraybackslash}p{0.75cm}"
             r">{\raggedright\arraybackslash}p{1.85cm}"
             r">{\raggedright\arraybackslash}p{2.3cm}"
             r">{\raggedright\arraybackslash}p{\dimexpr\textwidth-9.25cm-10\tabcolsep\relax}@{}}")
    mig_txt = ", ".join(f"V{v}" for v in migs) if migs else "—"
    cab = (r"\tb{Columna} & \tb{Tipo} & \tb{Nulo} & \tb{Default} & \tb{Clave} & \tb{Descripción} \\")
    out = [
        r"\needspace{12\baselineskip}",
        r"\begingroup\scriptsize\setlength{\tabcolsep}{3pt}",
        ancho,
        r"\caption[Diccionario de datos: " + tt(clave) + "]{" + tt(clave) + ": "
        + prosa(desc_tabla) + r"}\label{tab:dd-"
        + clave.replace(".", "-").replace("_", "-") + r"}\\",
        r"\toprule", cab, r"\midrule", r"\endfirsthead",
        r"\multicolumn{6}{@{}l}{\scriptsize\itshape " + tt(clave) + r" (continuación)}\\",
        r"\toprule", cab, r"\midrule", r"\endhead",
        r"\midrule\multicolumn{6}{r@{}}{\scriptsize\itshape continúa en la página siguiente}\\",
        r"\endfoot", r"\bottomrule", r"\endlastfoot",
    ]
    for c in t["columnas"]:
        ck = f"{clave}.{c['nombre']}"
        desc = COLUMNAS.get(ck)
        if desc is None:
            raise SystemExit(f"Falta la descripción de la columna {ck}")
        if c.get("comentario"):
            desc = desc + " " + c["comentario"]
        fila = " & ".join([
            tt(c["nombre"]),
            tt(tipo_corto(c["tipo"])),
            "no" if c["no_nulo"] else "sí",
            tt(default_corto(c["default"])) if c["default"] else "",
            r" \newline ".join(formato_clave(m) for m in marcas[c["nombre"]]),
            prosa(desc),
        ]) + r" \\"
        out.append(fila)
    notas = notas_restricciones(t)
    pie = [r"\textit{Migraciones:} " + mig_txt + "."]
    if notas:
        pie.append(r"\textit{Restricciones e índices:} " + "; ".join(notas) + ".")
    out.append(r"\midrule")
    out.append(r"\multicolumn{6}{@{}p{\textwidth}@{}}{\raggedright " + r" \newline ".join(pie)
               + r"}\\")
    out.append(r"\end{longtable}")
    out.append(r"\endgroup")
    return "\n".join(out)


def generar_tex(datos: dict) -> str:
    tablas = [t for t in datos["tablas"] if t["esquema"] in ORDEN_ESQUEMAS]
    infra = [t for t in datos["tablas"] if t["esquema"] not in ORDEN_ESQUEMAS]
    um = datos.get("ultima_migracion", {})
    n_col = sum(len(t["columnas"]) for t in tablas)
    out = [
        "% ARCHIVO GENERADO por scripts/diccionario_datos.py — no editar a mano.",
        f"% Esquema: {um.get('archivo', '?')} ({um.get('fecha', '?')}), "
        f"repositorio del sistema en {um.get('commit_repo', '?')}; generado el {datos['generado']}.",
        "",
    ]
    out.append(
        r"Las tablas siguientes describen las " + str(len(tablas)) + r" tablas de dominio ("
        + str(n_col) + r" columnas) de los nueve esquemas. Para cada columna se indica el tipo "
        r"de PostgreSQL, si admite nulos, el valor por defecto y su papel en las claves: "
        r"\textsc{pk} clave primaria, \textsc{fk} clave foránea (con la tabla a la que apunta), "
        r"\textsc{uq} unicidad de la columna (\textsc{uq*}: forma parte de una unicidad "
        r"compuesta, detallada al pie), \textsc{ck} restricción \texttt{CHECK} y \textsc{ex} "
        r"restricción de exclusión. Al pie de cada tabla se transcriben las restricciones de "
        r"tabla y los índices que no derivan de una clave, con la expresión que devuelve el "
        r"catálogo de PostgreSQL, y las migraciones que crean o modifican la tabla.")
    out.append("")
    # Resumen por esquema
    out.append(r"\begingroup\small")
    out.append(r"\begin{longtable}{@{}>{\raggedright\arraybackslash}p{2.1cm}"
               r">{\raggedright\arraybackslash}p{\dimexpr\textwidth-3.7cm-4\tabcolsep\relax}"
               r">{\centering\arraybackslash}p{1.6cm}@{}}")
    out.append(r"\caption{Esquemas de la base de datos y cantidad de tablas}"
               r"\label{tab:dd-esquemas}\\")
    out.append(r"\toprule \tb{Esquema} & \tb{Contenido} & \tb{Tablas} \\ \midrule \endfirsthead")
    out.append(r"\toprule \tb{Esquema} & \tb{Contenido} & \tb{Tablas} \\ \midrule \endhead")
    out.append(r"\bottomrule \endfoot")
    for e in ORDEN_ESQUEMAS:
        n = sum(1 for t in tablas if t["esquema"] == e)
        out.append(tt(e) + " & " + prosa(ESQUEMAS[e]) + f" & {n} \\\\")
    out.append(r"\end{longtable}")
    out.append(r"\endgroup")
    out.append("")
    for e in ORDEN_ESQUEMAS:
        out.append(r"\subsection{Esquema \texttt{" + e + r"}}\label{sec:dd-" + e + "}")
        out.append("")
        out.append(prosa(ESQUEMAS[e]))
        out.append("")
        for t in tablas:
            if t["esquema"] != e:
                continue
            out.append(tabla_tex(t, datos["migraciones"].get(f"{e}.{t['tabla']}", [])))
            out.append("")
    # Nota de infraestructura
    qrtz = sorted(t["tabla"] for t in infra if t["tabla"].startswith("qrtz_"))
    out.append(r"\subsection{Tablas de infraestructura}\label{sec:dd-infra}")
    out.append("")
    out.append(
        r"{\raggedright No forman parte del modelo de dominio y se excluyen del diccionario y de los "
        r"diagramas: las " + str(len(qrtz)) + r" tablas del almacén persistente de Quartz "
        r"(\texttt{QRTZ\_*}, en el esquema \texttt{public}, creadas por la migración V3: "
        + ", ".join(tt(q) for q in qrtz) + r"), que guardan los trabajos programados y sus "
        r"disparadores, y la tabla \texttt{flyway\_schema\_history}, que Flyway crea en el "
        r"primer esquema configurado (\texttt{identidad}) para registrar las migraciones "
        r"aplicadas. Las extensiones instaladas son "
        + ", ".join(tt(x["nombre"]) for x in datos["extensiones"] if x["nombre"] != "plpgsql")
        + r" (en \texttt{public}).\par}")
    out.append("")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# 4. Diagramas entidad-relación (Graphviz)
# ---------------------------------------------------------------------------

COLOR_ESQUEMA = {
    "identidad": "#dbe9f6", "matching": "#e2f0d9", "aula": "#fde9d9",
    "reservas": "#fff2cc", "pagos": "#ead1dc", "resumen": "#e4dfec",
    "reputacion": "#ddebf7", "admin": "#ededed", "seguridad": "#f8cbad",
}


def _h(texto: str) -> str:
    return texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def fks(t: dict) -> list[dict]:
    return [k for k in t["restricciones"] if k["tipo"] == "f"]


def unicos(t: dict) -> set[tuple[str, ...]]:
    res = set()
    for k in t["restricciones"]:
        if k["tipo"] in ("p", "u"):
            res.add(tuple(k["columnas"]))
    for i in t["indices"]:
        if i["unico"] and " WHERE " not in i["definicion"]:
            m = re.search(r"\((.*?)\)", i["definicion"])
            if m:
                res.add(tuple(c.strip() for c in m.group(1).split(",")))
    return res


def extremos_arista(t: dict, k: dict) -> tuple[str, str]:
    """Notación pata de gallo: (extremo del hijo, extremo del padre)."""
    cols = tuple(k["columnas"])
    nulable = any(not c["no_nulo"] for c in t["columnas"] if c["nombre"] in cols)
    uno_a_uno = cols in unicos(t)
    hijo = ("tee" if uno_a_uno else "crow") + "odot"
    padre = "teeodot" if nulable else "teetee"
    return hijo, padre


def nodo_completo(t: dict, color: str) -> str:
    pk = set()
    fkcols = set()
    for k in t["restricciones"]:
        if k["tipo"] == "p":
            pk |= set(k["columnas"])
        if k["tipo"] == "f":
            fkcols |= set(k["columnas"])
    unq = set()
    for cols in unicos(t):
        if len(cols) == 1:
            unq |= set(cols)
    filas = [f'<tr><td bgcolor="{color}" colspan="2" align="center"><b>{_h(t["tabla"])}</b></td></tr>']
    omitidas = 0
    for c in t["columnas"]:
        if c["nombre"] not in pk | fkcols | unq:
            omitidas += 1
            continue
        if c["nombre"] in unq and c["nombre"] not in pk:
            marca_uq = " UQ"
        else:
            marca_uq = ""
        marca = ("PK " if c["nombre"] in pk else "") + ("FK" if c["nombre"] in fkcols else "")
        nombre = _h(c["nombre"])
        if c["nombre"] in pk:
            nombre = f"<u>{nombre}</u>"
        if not c["no_nulo"]:
            nombre = f"<i>{nombre}</i>"
        filas.append(
            f'<tr><td align="left" port="{c["nombre"]}">{nombre}</td>'
            f'<td align="left"><font color="#555555">{_h(tipo_corto(c["tipo"]))}'
            f'{" " + marca.strip() if marca.strip() else ""}{marca_uq}</font></td></tr>')
    if omitidas:
        filas.append(f'<tr><td colspan="2" align="left"><font color="#555555" point-size="8">'
                     f'<i>+ {omitidas} atributo{"s" if omitidas > 1 else ""}</i></font></td></tr>')
    return ('<<table border="0" cellborder="1" cellspacing="0" cellpadding="2">'
            + "".join(filas) + "</table>>")


def dot_esquema(datos: dict, esquema: str) -> str:
    propias = [t for t in datos["tablas"] if t["esquema"] == esquema]
    externas: set[str] = set()
    entrantes: dict[str, int] = {}
    for t in propias:
        for k in fks(t):
            destino = f"{k['ref_esquema']}.{k['ref_tabla']}"
            entrantes[destino] = entrantes.get(destino, 0) + 1
    vistos: dict[str, int] = {}
    aristas = []
    for t in propias:
        origen = f"{t['esquema']}.{t['tabla']}"
        for k in fks(t):
            destino = f"{k['ref_esquema']}.{k['ref_tabla']}"
            if k["ref_esquema"] != esquema:
                # Las tablas de otros esquemas se dibujan como un nodo de referencia por
                # cada tabla que las usa, para no cruzar todo el diagrama.
                destino = f"{destino}#{t['tabla']}"
                externas.add(destino)
            col = k["columnas"][0]
            hijo, padre = extremos_arista(t, k)
            # Una tabla con muchas referencias entrantes (identidad.usuarios) queda en el
            # centro: la mitad de las tablas que la referencian se dibuja a cada lado.
            n = vistos.get(destino, 0)
            vistos[destino] = n + 1
            if origen == destino:
                ref = k["ref_columnas"][0]
                aristas.append(f'  "{origen}":"{col}":w -> "{destino}":"{ref}":w '
                               f'[dir=both, arrowtail="{hijo}", arrowhead="{padre}"];')
            elif entrantes.get(destino, 0) >= 5 and n % 2 == 1:
                aristas.append(f'  "{destino}" -> "{origen}":"{col}" '
                               f'[dir=both, arrowtail="{padre}", arrowhead="{hijo}"];')
            else:
                aristas.append(f'  "{origen}":"{col}" -> "{destino}" '
                               f'[dir=both, arrowtail="{hijo}", arrowhead="{padre}"];')
    lineas = [
        f'digraph "{esquema}" {{',
        '  graph [rankdir=LR, fontname="Helvetica", fontsize=10, nodesep=0.2, ranksep=0.7,'
        ' splines=spline, pad=0.1];',
        '  node [shape=plaintext, fontname="Helvetica", fontsize=10];',
        '  edge [color="#444444", arrowsize=0.8, penwidth=0.8];',
    ]
    color = COLOR_ESQUEMA[esquema]
    for t in propias:
        lineas.append(f'  "{t["esquema"]}.{t["tabla"]}" [label={nodo_completo(t, color)}];')
    for ext in sorted(externas):
        e, nombre = ext.split("#")[0].split(".")
        lineas.append(
            f'  "{ext}" [shape=box, style="rounded,filled,dashed", '
            f'fillcolor="{COLOR_ESQUEMA.get(e, "#ffffff")}", label="{e}.\\n{nombre}"];')
    lineas += aristas
    lineas.append("}")
    return "\n".join(lineas) + "\n"


# Disposición del diagrama general: filas de esquemas y tablas por columna en cada uno.
GRILLA_GENERAL = [["identidad", "matching", "aula"],
                  ["reservas", "pagos", "resumen", "reputacion"],
                  ["admin", "seguridad"]]
ALTO_COLUMNA = {"identidad": 6}


def dot_general(datos: dict) -> str:
    propias = [t for t in datos["tablas"] if t["esquema"] in ORDEN_ESQUEMAS]
    lineas = [
        'digraph "tinku" {',
        '  graph [rankdir=TB, fontname="Helvetica", fontsize=13, nodesep=0.12, ranksep=0.18,'
        ' splines=true, newrank=true, pad=0.1];',
        '  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11,'
        ' margin="0.06,0.02", height=0.28];',
        '  edge [color="#555555", arrowsize=0.6, penwidth=0.7];',
    ]
    ultimo: dict[str, str] = {}
    primero: dict[str, list[str]] = {}
    alto: dict[str, int] = {}
    for e in ORDEN_ESQUEMAS:
        nombres = sorted((f"{e}.{t['tabla']}" for t in propias if t["esquema"] == e),
                         key=lambda n: (n != "identidad.usuarios", n))
        lineas.append(f'  subgraph "cluster_{e}" {{')
        lineas.append(f'    label=<<b>{e}</b>>; style="rounded"; color="#888888"; margin=6;')
        for nom in nombres:
            t = next(x for x in propias if f"{x['esquema']}.{x['tabla']}" == nom)
            n_usr = sum(1 for k in fks(t)
                        if (k["ref_esquema"], k["ref_tabla"]) == ("identidad", "usuarios")
                        and nom != "identidad.usuarios")
            if n_usr:
                etiqueta = (f'<{_h(t["tabla"])}<font point-size="10" color="#1f4e79">'
                            f' \u25cf{n_usr}</font>>')
            else:
                etiqueta = f'"{t["tabla"]}"'
            pen = ', penwidth=2.2' if nom == "identidad.usuarios" else ""
            lineas.append(f'    "{nom}" [label={etiqueta}, fillcolor="{COLOR_ESQUEMA[e]}"{pen}];')
        h = ALTO_COLUMNA.get(e, 4)
        for i in range(len(nombres) - 1):
            if (i + 1) % h:
                lineas.append(f'    "{nombres[i]}" -> "{nombres[i + 1]}" [style=invis, weight=10];')
        lineas.append("  }")
        primero[e] = nombres[::h]
        ultimo[e] = nombres[min(h, len(nombres)) - 1]
        alto[e] = min(h, len(nombres))
    for fila, siguiente in zip(GRILLA_GENERAL, GRILLA_GENERAL[1:]):
        mas_alto = max(fila, key=lambda e: alto[e])
        for e in siguiente:
            for cabeza in primero[e]:
                lineas.append(f'  "{ultimo[mas_alto]}" -> "{cabeza}" [style=invis];')
    vistos = set()
    for t in propias:
        origen = f"{t['esquema']}.{t['tabla']}"
        for k in fks(t):
            destino = f"{k['ref_esquema']}.{k['ref_tabla']}"
            if destino == "identidad.usuarios" and origen != "identidad.usuarios":
                continue
            if (origen, destino) in vistos or origen == destino:
                continue
            vistos.add((origen, destino))
            lineas.append(f'  "{origen}" -> "{destino}" [constraint=false];')
    lineas.append("}")
    return "\n".join(lineas) + "\n"


TITULO_DER = {
    "identidad": "esquema \\texttt{identidad} (M1)",
    "matching": "esquema \\texttt{matching} (M2)",
    "aula": "esquema \\texttt{aula} (M3)",
    "reservas": "esquema \\texttt{reservas} (M4)",
    "pagos": "esquema \\texttt{pagos} (M5)",
    "resumen": "esquema \\texttt{resumen} (M6)",
    "reputacion": "esquema \\texttt{reputacion} (M7)",
    "admin": "esquema \\texttt{admin} (M8)",
    "seguridad": "esquema \\texttt{seguridad} (M9)",
}

# Área útil para una figura (pt): A4 con los márgenes de la clase (150 mm x 243 mm),
# descontando el epígrafe.
AREA_VERTICAL = (425.0, 0.78 * 689.0)
AREA_APAISADA = (0.95 * 689.0, 0.9 * 425.0)


def tamano_pdf(ruta: Path) -> tuple[float, float]:
    info = subprocess.run(["pdfinfo", str(ruta)], check=True, capture_output=True,
                          text=True).stdout
    m = re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", info)
    return float(m.group(1)), float(m.group(2))


def figura_tex(nombre: str, epigrafe: str, etiqueta: str, cuerpo_pt: float) -> tuple[str, float]:
    """Elige vertical o apaisada según dónde la letra queda más grande."""
    ancho, alto = tamano_pdf(DIR_DER / f"{nombre}.pdf")
    esc_v = min(AREA_VERTICAL[0] / ancho, AREA_VERTICAL[1] / alto, 1.0)
    esc_a = min(AREA_APAISADA[0] / ancho, AREA_APAISADA[1] / alto, 1.0)
    apaisada = cuerpo_pt * esc_v < 7.0 and esc_a > esc_v
    escala = esc_a if apaisada else esc_v
    ancho_fig = ancho * escala
    fig = [r"\begin{figure}[p]" if apaisada else r"\begin{figure}[htbp]",
           r"\centering",
           r"\includegraphics[width=%.1fpt]{figuras/der/%s}" % (ancho_fig, nombre),
           r"\caption{%s}\label{%s}" % (epigrafe, etiqueta),
           r"\end{figure}"]
    fig = [l for l in fig if l]
    if apaisada:
        fig = [r"\begin{landscape}"] + fig + [r"\end{landscape}"]
    return "\n".join(fig), cuerpo_pt * escala


def generar_der(datos: dict) -> None:
    DIR_DER.mkdir(parents=True, exist_ok=True)
    archivos = {"der-general": dot_general(datos)}
    for e in ORDEN_ESQUEMAS:
        archivos[f"der-{e}"] = dot_esquema(datos, e)
    for nombre, contenido in archivos.items():
        ruta = DIR_DER / f"{nombre}.dot"
        ruta.write_text(contenido)
        subprocess.run(["dot", "-Tpdf", str(ruta), "-o", str(DIR_DER / f"{nombre}.pdf")],
                       check=True)
    um = datos.get("ultima_migracion", {})
    out = ["% ARCHIVO GENERADO por scripts/diccionario_datos.py — no editar a mano.",
           f"% Esquema: {um.get('archivo', '?')} ({um.get('fecha', '?')}).", ""]
    fig, letra = figura_tex(
        "der-general",
        r"Diagrama entidad-relación general: tablas por esquema y claves foráneas entre "
        r"ellas, salvo las que apuntan a \texttt{identidad.usuarios}, que se indican con "
        r"\textbullet{} y la cantidad de columnas que la referencian",
        "fig:der-general", 11.0)
    print(f"  der-general: letra efectiva {letra:.1f} pt")
    out += [fig, ""]
    for e in ORDEN_ESQUEMAS:
        fig, letra = figura_tex(
            f"der-{e}", "Diagrama entidad-relación del " + TITULO_DER[e],
            f"fig:der-{e}", 10.0)
        print(f"  der-{e}: letra efectiva {letra:.1f} pt")
        out += [fig, ""]
    (RAIZ / "apendices" / "C-der.tex").write_text("\n".join(out))


# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paso", choices=["introspectar", "generar", "todo"])
    ap.add_argument("--repo", type=Path, help="ruta del repositorio del sistema (usal-tinku)")
    args = ap.parse_args()
    if args.paso in ("introspectar", "todo"):
        datos = introspectar(args.repo)
        JSON_ESQUEMA.write_text(json.dumps(datos, ensure_ascii=False, indent=1) + "\n")
        print(f"esquema guardado en {JSON_ESQUEMA.relative_to(RAIZ)}")
    if args.paso in ("generar", "todo"):
        datos = json.loads(JSON_ESQUEMA.read_text())
        TEX_SALIDA.write_text(generar_tex(datos))
        print(f"diccionario en {TEX_SALIDA.relative_to(RAIZ)}")
        generar_der(datos)
        print(f"diagramas en {DIR_DER.relative_to(RAIZ)}/")


if __name__ == "__main__":
    main()

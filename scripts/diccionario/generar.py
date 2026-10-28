#!/usr/bin/env python3
"""Genera el diccionario de datos y los diagramas entidad-relación del apéndice C.

La estructura sale del catálogo de PostgreSQL, no de leer los .sql: así quedan aplicados los
ALTER, DROP CONSTRAINT y RENAME de las migraciones posteriores. Las descripciones salen de
descripciones.py.

Uso (desde la raíz de usal-tinku-docs):

    # 1. Base vacía con todas las migraciones aplicadas, por ejemplo con el compose del sistema:
    #      docker compose up -d db   (en usal-tinku)
    #      createdb -h localhost -U tinku_dev tinku_diccionario
    #      for f in $(ls $MIG/V*.sql | sort -V); do psql ... -1 -f "$f"; done
    # 2. Generar:
    python3 scripts/diccionario/generar.py \\
        --db "postgresql://tinku_dev:changeme@localhost:5432/tinku_diccionario" \\
        --migraciones ../usal-tinku/backend/src/main/resources/db/migration

Escribe apendices/C-diccionario-datos.tex y figuras/der/*.{dot,pdf}. Requiere psql, Graphviz (dot) y pdfinfo (poppler).
"""

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from descripciones import ESQUEMAS, TABLAS  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
SALIDA_TEX = RAIZ / "apendices" / "C-diccionario-datos.tex"
SALIDA_DER = RAIZ / "figuras" / "der"

# Mismos colores que figuras/uml/_estilo.iuml.
AZUL = "#2F5A9E"
CELESTE = "#EEF3FB"
GRIS = "#777777"

CONSULTA = r"""
with t as (
  select c.oid, n.nspname as esquema, c.relname as tabla
    from pg_class c join pg_namespace n on n.oid = c.relnamespace
   where c.relkind = 'r' and n.nspname = any(:'esquemas'::text[])
)
select json_agg(json_build_object(
  'esquema', t.esquema, 'tabla', t.tabla,
  'columnas', (select json_agg(json_build_object(
                  'nombre', a.attname,
                  'tipo', format_type(a.atttypid, a.atttypmod),
                  'nulo', not a.attnotnull,
                  'defecto', pg_get_expr(d.adbin, d.adrelid)) order by a.attnum)
                 from pg_attribute a
                 left join pg_attrdef d on d.adrelid = a.attrelid and d.adnum = a.attnum
                where a.attrelid = t.oid and a.attnum > 0 and not a.attisdropped),
  'restricciones', (select coalesce(json_agg(json_build_object(
                  'nombre', co.conname, 'tipo', co.contype,
                  'definicion', pg_get_constraintdef(co.oid),
                  'columnas', (select json_agg(a.attname order by k.i)
                                 from unnest(co.conkey) with ordinality k(n, i)
                                 join pg_attribute a on a.attrelid = co.conrelid and a.attnum = k.n),
                  'destino', case when co.contype = 'f'
                                  then (select n2.nspname || '.' || c2.relname
                                          from pg_class c2 join pg_namespace n2 on n2.oid = c2.relnamespace
                                         where c2.oid = co.confrelid) end)
                  order by co.contype, co.conname), '[]')
                 from pg_constraint co
                where co.conrelid = t.oid and co.contype in ('p', 'f', 'u', 'c', 'x')),
  'indices', (select coalesce(json_agg(json_build_object(
                  'nombre', ic.relname, 'unico', i.indisunique,
                  'definicion', pg_get_indexdef(i.indexrelid),
                  'columnas', (select json_agg(a.attname)
                                 from unnest(i.indkey) k(n)
                                 join pg_attribute a on a.attrelid = i.indrelid and a.attnum = k.n),
                  'parcial', i.indpred is not null) order by ic.relname), '[]')
                 from pg_index i join pg_class ic on ic.oid = i.indexrelid
                where i.indrelid = t.oid
                  and not exists (select 1 from pg_constraint co where co.conindid = i.indexrelid))
) order by t.esquema, t.tabla)
from t;
"""


def leer_catalogo(db):
    esquemas = "{" + ",".join(ESQUEMAS) + "}"
    salida = subprocess.run(
        ["psql", db, "-X", "-At", "-v", "ON_ERROR_STOP=1", "-v", f"esquemas={esquemas}"],
        input=CONSULTA, capture_output=True, text=True, check=True,
    ).stdout
    return json.loads(salida)


def versiones_por_tabla(dir_migraciones, nombres):
    """Migraciones que crean o modifican cada tabla (se ignoran los comentarios SQL)."""
    versiones = defaultdict(set)
    for archivo in dir_migraciones.glob("V*.sql"):
        version = int(re.match(r"V(\d+)__", archivo.name).group(1))
        texto = re.sub(r"--[^\n]*", "", archivo.read_text(encoding="utf-8"))
        for nombre in nombres:
            if re.search(r"\b" + re.escape(nombre) + r"\b", texto):
                versiones[nombre].add(version)
    return {n: sorted(v) for n, v in versiones.items()}


# ------------------------------------------------------------------ formato SQL

def tipo_corto(tipo):
    return (tipo.replace("character varying", "varchar")
                .replace("timestamp with time zone", "timestamptz")
                .replace("time without time zone", "time"))


CASTS = r"::(?:text|character varying|varchar|jsonb|uuid|numeric|timestamp with time zone)(?:\[\])?"


def sql_simple(expr):
    """Vuelve legible lo que devuelve pg_get_constraintdef / pg_get_expr: sin casts, con IN
    en lugar de = ANY (ARRAY[...]) y sin paréntesis redundantes."""
    expr = re.sub(r"\(ARRAY\[([^\]]*)\]\)" + CASTS, r"ARRAY[\1]", expr)
    expr = re.sub(CASTS, "", expr)
    expr = re.sub(r"\((\w+)\) = ANY \(ARRAY\[([^\]]*)\]\)", r"\1 IN (\2)", expr)
    expr = re.sub(r"(\w+) = ANY \(ARRAY\[([^\]]*)\]\)", r"\1 IN (\2)", expr)
    anterior = None
    while anterior != expr:
        anterior = expr
        expr = re.sub(r"\((\w+)\)", r"\1", expr)
        expr = re.sub(r"\('([^']*)'\)", r"'\1'", expr)
        expr = _sin_parentesis_dobles(expr)
    return _sin_parentesis_exteriores(expr)


def _pares(expr):
    pares, pila, en_literal = {}, [], False
    for i, c in enumerate(expr):
        if c == "'":
            en_literal = not en_literal
        elif en_literal:
            continue
        elif c == "(":
            pila.append(i)
        elif c == ")":
            pares[pila.pop()] = i
    assert not pila, f"paréntesis desbalanceados: {expr}"
    return pares


def _sin_parentesis_dobles(expr):
    pares = _pares(expr)
    sobran = set()
    for a, b in pares.items():
        if expr[a + 1:a + 2] == "(" and pares.get(a + 1) == b - 1:
            sobran.update((a, b))
    return "".join(c for i, c in enumerate(expr) if i not in sobran)


def _sin_parentesis_exteriores(expr):
    while expr.startswith("(") and _pares(expr)[0] == len(expr) - 1:
        expr = expr[1:-1]
    return expr


def tex(texto):
    """Escapa SQL para \\texttt y permite cortar la línea en lugares naturales."""
    reemplazos = {"\\": r"\textbackslash{}", "_": r"\_\allowbreak{}", "%": r"\%",
                  "&": r"\&", "#": r"\#", "$": r"\$", "{": r"\{", "}": r"\}",
                  "'": r"\textquotesingle{}", "~": r"\textasciitilde{}",
                  "^": r"\textasciicircum{}", "<": r"\textless{}", ">": r"\textgreater{}",
                  ",": r",\allowbreak{}", "(": r"(\allowbreak{}"}
    return "".join(reemplazos.get(c, c) for c in texto)


def tt(texto):
    return r"\texttt{" + tex(texto) + "}"


# ------------------------------------------------------------------ LaTeX

TIPO_RESTRICCION = {"p": "PK", "f": "FK", "u": "UNIQUE", "c": "CHECK", "x": "EXCLUDE"}


def claves_por_columna(tabla):
    claves = defaultdict(list)
    for r in tabla["restricciones"]:
        if r["tipo"] == "p":
            for c in r["columnas"]:
                claves[c].append("PK")
        elif r["tipo"] == "f":
            for c in r["columnas"]:
                claves[c].append("FK")
        elif r["tipo"] == "u" and len(r["columnas"]) == 1:
            claves[r["columnas"][0]].append("UQ")
    for i in tabla["indices"]:
        if i["unico"] and not i["parcial"] and len(i["columnas"] or []) == 1:
            claves[i["columnas"][0]].append("UQ")
    return {c: ", ".join(dict.fromkeys(v)) for c, v in claves.items()}


def definicion_restriccion(r):
    d = r["definicion"]
    if r["tipo"] == "f":
        m = re.match(r"FOREIGN KEY \(([^)]*)\) REFERENCES ([\w.]+)\(([^)]*)\)(.*)", d)
        cols, destino, cols_destino, resto = m.groups()
        texto = f"({cols}) → {destino}({cols_destino})"
        accion = resto.strip()
        return tt(texto.replace("→", "@@")).replace("@@", r"$\rightarrow$") + \
            (" " + tt(accion) if accion else "")
    d = re.sub(r"^(PRIMARY KEY|UNIQUE) ", "", d)
    if r["tipo"] == "c":
        d = sql_simple(re.sub(r"^CHECK ", "", d))
    if r["tipo"] == "x":
        d = sql_simple(re.sub(r"^EXCLUDE USING gist ", "gist ", d))
    return tt(d)


def definicion_indice(i):
    metodo, columnas, _, condicion = re.search(
        r" USING (\w+) (\(.*?\))( WHERE (.*))?$", i["definicion"]).groups()
    texto = columnas + ("" if metodo == "btree" else f" USING {metodo}")
    if condicion:
        texto += " WHERE " + sql_simple(condicion)
    return tt(texto)


def latex_tabla(tabla, versiones):
    nombre = f"{tabla['esquema']}.{tabla['tabla']}"
    descripcion, columnas = TABLAS[nombre]
    claves = claves_por_columna(tabla)
    v = ", ".join(f"V{n}" for n in versiones.get(nombre, []))
    out = [
        r"\subsubsection{\texorpdfstring{" + tt(nombre) + "}{" + nombre.replace("_", r"\_") + "}}"
        r"\label{dd:" + nombre + "}",
        "",
        descripcion + r" \emph{Migraciones:} " + v + ".",
        "",
        r"{\small",
        r"\begin{xltabular}{\textwidth}{@{}>{\raggedright\arraybackslash}p{3.6cm} "
        r">{\raggedright\arraybackslash}p{2.3cm} >{\raggedright\arraybackslash}p{1cm} "
        r">{\centering\arraybackslash}p{0.85cm} L@{}}",
        r"    \toprule",
        r"    \tb{Atributo} & \tb{Tipo} & \tb{Clave} & \tb{Nulo} & \tb{Descripción} \\",
        r"    \midrule",
        r"    \endfirsthead",
        r"    \toprule",
        r"    \tb{Atributo} & \tb{Tipo} & \tb{Clave} & \tb{Nulo} & \tb{Descripción} \\",
        r"    \midrule",
        r"    \endhead",
        r"    \bottomrule",
        r"    \endfoot",
    ]
    for c in tabla["columnas"]:
        desc = columnas[c["nombre"]]
        defecto = c["defecto"]
        if defecto and defecto != "gen_random_uuid()":
            desc += r". Por defecto: " + tt(sql_simple(defecto))
        out.append(f"    {tt(c['nombre'])} & {tt(tipo_corto(c['tipo']))} & "
                   f"{claves.get(c['nombre'], '')} & {'sí' if c['nulo'] else 'no'} & {desc} \\\\")
    out += [r"\end{xltabular}", "}", ""]

    filas = [(TIPO_RESTRICCION[r["tipo"]], r["nombre"], definicion_restriccion(r))
             for r in tabla["restricciones"]]
    filas += [("UNIQUE" if i["unico"] else "Índice", i["nombre"], definicion_indice(i))
              for i in tabla["indices"]]
    out += [
        r"{\small",
        r"\begin{xltabular}{\textwidth}{@{}>{\raggedright\arraybackslash}p{1.7cm} "
        r">{\raggedright\arraybackslash}p{4.6cm} L@{}}",
        r"    \toprule",
        r"    \tb{Tipo} & \tb{Nombre} & \tb{Definición} \\",
        r"    \midrule",
        r"    \endfirsthead",
        r"    \toprule",
        r"    \tb{Tipo} & \tb{Nombre} & \tb{Definición} \\",
        r"    \midrule",
        r"    \endhead",
        r"    \bottomrule",
        r"    \endfoot",
    ]
    out += [f"    {t} & {tt(n)} & {d} \\\\" for t, n, d in filas]
    out += [r"\end{xltabular}", "}", ""]
    return out


def latex(catalogo, versiones, escalas):
    por_esquema = defaultdict(list)
    for t in catalogo:
        por_esquema[t["esquema"]].append(t)
    total_cols = sum(len(t["columnas"]) for t in catalogo)
    out = [
        "%!TEX root = ../main.tex",
        "% GENERADO por scripts/diccionario/generar.py — no editar a mano.",
        "",
        f"% {len(catalogo)} tablas, {total_cols} columnas.",
        "",
    ]
    for esquema in ESQUEMAS:
        tablas = por_esquema[esquema]
        modulo, descripcion = ESQUEMAS[esquema]
        out += [
            r"\subsection{Esquema \texttt{" + esquema + "} (" + modulo + ")}"
            r"\label{dd:" + esquema + "}",
            "",
            descripcion + f" Tablas: {len(tablas)}. Su diagrama entidad-relación es la "
            r"figura~\ref{fig:der-" + esquema + "}.",
            "",
            r"\begin{figure}[htbp]",
            r"    \centering",
            f"    \\includegraphics[scale={escalas[esquema]:.3f}]{{figuras/der/{esquema}}}",
            r"    \caption{Diagrama entidad-relación del esquema \texttt{" + esquema + "} (" + modulo + ")}",
            r"    \label{fig:der-" + esquema + "}",
            r"\end{figure}",
            "",
        ]
        for t in tablas:
            out += latex_tabla(t, versiones)
    return "\n".join(out) + "\n"


# ------------------------------------------------------------------ Graphviz

def html(texto):
    return texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def nodo_tabla(t, claves):
    """Solo los atributos que son clave (PK, FK, UQ) y cuántos más hay: con los 375 atributos
    el diagrama de identidad no entra legible en una página. El resto está en el diccionario."""
    filas = [f'<TR><TD COLSPAN="2" BGCOLOR="{CELESTE}" ALIGN="CENTER"><B>{t["tabla"]}</B></TD></TR>']
    otros = 0
    for c in t["columnas"]:
        clave = claves.get(c["nombre"], "")
        if not clave:
            otros += 1
            continue
        nombre = html(c["nombre"])
        if "PK" in clave:
            nombre = f"<U>{nombre}</U>"
        filas.append(f'<TR><TD ALIGN="LEFT">{nombre}</TD>'
                     f'<TD ALIGN="LEFT"><FONT COLOR="{AZUL}">{clave}</FONT></TD></TR>')
    if otros:
        texto = "+ 1 atributo" if otros == 1 else f"+ {otros} atributos"
        filas.append(f'<TR><TD COLSPAN="2" ALIGN="LEFT"><FONT COLOR="{GRIS}"><I>{texto}</I></FONT></TD></TR>')
    return (f'"{t["esquema"]}.{t["tabla"]}" [label=<<TABLE BORDER="1" CELLBORDER="0" '
            f'CELLSPACING="0" CELLPADDING="2" COLOR="{AZUL}">{"".join(filas)}</TABLE>>];')


def extremos(fk, tabla, cols_nulas, unicas):
    """Notación pata de gallo: el símbolo más cercano a la entidad es la cardinalidad máxima."""
    hijo = "teeodot" if tuple(fk["columnas"]) in unicas else "crowodot"
    padre = "teeodot" if any(c in cols_nulas for c in fk["columnas"]) else "teetee"
    return hijo, padre


def columnas_unicas(t):
    unicas = {tuple(r["columnas"]) for r in t["restricciones"] if r["tipo"] in "pu"}
    unicas |= {tuple(i["columnas"]) for i in t["indices"] if i["unico"] and not i["parcial"]}
    return unicas


ENCABEZADO = f"""  graph [fontname="Helvetica", rankdir=LR, nodesep=0.35, ranksep=0.9, pad=0.2];
  node [shape=plain, fontname="Helvetica", fontsize=10];
  edge [fontname="Helvetica", fontsize=9, color="#333333", dir=both, arrowsize=0.9];"""


def dot_esquema(esquema, tablas, rankdir, por_fila):
    """Una arista por par (tabla hija, tabla padre), rotulada con las columnas de la FK: con
    una arista por FK, las tablas que referencian varias veces a usuarios se vuelven ilegibles."""
    propias = {f"{t['esquema']}.{t['tabla']}" for t in tablas}
    externas = set()
    agrupadas = defaultdict(list)
    for t in tablas:
        nulas = {c["nombre"] for c in t["columnas"] if c["nulo"]}
        unicas = columnas_unicas(t)
        for fk in (r for r in t["restricciones"] if r["tipo"] == "f"):
            agrupadas[(f"{t['esquema']}.{t['tabla']}", fk["destino"])].append(
                (", ".join(fk["columnas"]), extremos(fk, t, nulas, unicas)))
            if fk["destino"] not in propias:
                externas.add(fk["destino"])
    aristas = []
    for (origen, destino), fks in agrupadas.items():
        if len({e for _, e in fks}) == 1:
            grupos = [(fks[0][1], [c for c, _ in fks])]
        else:  # cardinalidades distintas hacia la misma tabla: una arista por FK
            grupos = [(e, [c]) for c, e in fks]
        for (hijo, padre), cols in grupos:
            etiqueta = "\\n".join(cols)
            aristas.append(f'  "{origen}" -> "{destino}" [arrowtail={hijo}, arrowhead={padre}, '
                           f'label="{etiqueta}"];')
    lineas = [f'digraph "{esquema}" {{', ENCABEZADO.replace("rankdir=LR", f"rankdir={rankdir}")]
    for t in tablas:
        lineas.append("  " + nodo_tabla(t, claves_por_columna(t)))
    for e in sorted(externas):
        lineas.append(f'  "{e}" [shape=box, style="dashed,rounded", color="{GRIS}", '
                      f'fontcolor="{GRIS}", label="{e}"];')
    lineas += aristas + filas_invisibles(tablas, agrupadas, por_fila) + ["}"]
    return "\n".join(lineas) + "\n"


def filas_invisibles(tablas, agrupadas, por_fila):
    """Las tablas que nadie referencia quedan todas en el mismo rango y el diagrama se vuelve
    muy ancho (o muy alto). Con aristas invisibles se reparten en grupos de `por_fila`."""
    if not por_fila:
        return []
    referenciadas = {destino for _, destino in agrupadas}
    hojas = [f"{t['esquema']}.{t['tabla']}" for t in tablas
             if f"{t['esquema']}.{t['tabla']}" not in referenciadas]
    return [f'  "{a}" -> "{b}" [style=invis, dir=none];'
            for a, b in zip(hojas, hojas[por_fila:])]


def dot_general(catalogo):
    por_esquema = defaultdict(list)
    for t in catalogo:
        por_esquema[t["esquema"]].append(t["tabla"])
    conteo = defaultdict(int)
    for t in catalogo:
        for fk in (r for r in t["restricciones"] if r["tipo"] == "f"):
            destino = fk["destino"].split(".")[0]
            if destino != t["esquema"]:
                conteo[(t["esquema"], destino)] += 1
    lineas = ['digraph "general" {', ENCABEZADO.replace("rankdir=LR", "rankdir=TB"),
              '  edge [dir=forward, arrowhead=vee];']
    for esquema, (modulo, _) in ESQUEMAS.items():
        filas = "".join(f'<TR><TD ALIGN="LEFT">{t}</TD></TR>' for t in por_esquema[esquema])
        lineas.append(
            f'  "{esquema}" [label=<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" '
            f'CELLPADDING="3" COLOR="{AZUL}"><TR><TD BGCOLOR="{CELESTE}"><B>{esquema}</B> '
            f'({modulo})</TD></TR>{filas}</TABLE>>];')
    for (origen, destino), n in sorted(conteo.items()):
        lineas.append(f'  "{origen}" -> "{destino}" [label=" {n} FK", penwidth={min(1 + n / 4, 3):.1f}];')
    lineas.append("}")
    return "\n".join(lineas) + "\n", conteo


# Caja de texto de la página A4 (usal-proyecto-final.cls), menos el espacio del epígrafe.
ANCHO_PT, ALTO_PT = 425, 620


def escala(dot):
    """Factor con el que el diagrama entra en la página; más alto = letra más grande."""
    plano = subprocess.run(["dot", "-Tplain"], input=dot, capture_output=True, text=True,
                           check=True).stdout
    _, _, ancho, alto = plano.split("\n", 1)[0].split()
    return min(ANCHO_PT / (float(ancho) * 72), ALTO_PT / (float(alto) * 72))


def mejor_distribucion(esquema, tablas):
    """Prueba de arriba abajo y de izquierda a derecha, con distintos agrupamientos, y se queda
    con la que entra en la página con la letra más grande. Devuelve (dot, escala)."""
    candidatos = [dot_esquema(esquema, tablas, rankdir, por_fila)
                  for rankdir in ("TB", "LR") for por_fila in (None, 2, 3, 4)]
    return max(((d, escala(d)) for d in candidatos), key=lambda c: c[1])


def render(nombre, dot):
    SALIDA_DER.mkdir(parents=True, exist_ok=True)
    fuente = SALIDA_DER / f"{nombre}.dot"
    fuente.write_text(dot, encoding="utf-8")
    pdf = SALIDA_DER / f"{nombre}.pdf"
    subprocess.run(["dot", "-Tpdf", "-o", str(pdf), str(fuente)], check=True)
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, check=True).stdout
    ancho, alto = map(float, re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", info).groups())
    return min(1.0, ANCHO_PT / ancho, ALTO_PT / alto)


# ------------------------------------------------------------------ verificación

def verificar(catalogo):
    errores = []
    en_base = {f"{t['esquema']}.{t['tabla']}": t for t in catalogo}
    for nombre in sorted(set(TABLAS) - set(en_base)):
        errores.append(f"descripción de una tabla que no existe: {nombre}")
    for nombre, t in en_base.items():
        if nombre not in TABLAS:
            errores.append(f"tabla sin descripción: {nombre}")
            continue
        cols_base = [c["nombre"] for c in t["columnas"]]
        cols_desc = TABLAS[nombre][1]
        errores += [f"columna sin descripción: {nombre}.{c}" for c in cols_base if c not in cols_desc]
        errores += [f"descripción de una columna que no existe: {nombre}.{c}"
                    for c in cols_desc if c not in cols_base]
    if errores:
        sys.exit("\n".join(errores))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--db", required=True, help="URL de una base con todas las migraciones aplicadas")
    p.add_argument("--migraciones", required=True, type=Path, help="carpeta db/migration del backend")
    a = p.parse_args()

    catalogo = leer_catalogo(a.db)
    verificar(catalogo)
    versiones = versiones_por_tabla(a.migraciones, [f"{t['esquema']}.{t['tabla']}" for t in catalogo])
    general, conteo = dot_general(catalogo)
    render("00-general", general)
    escalas = {}
    for esquema in ESQUEMAS:
        dot, _ = mejor_distribucion(esquema, [t for t in catalogo if t["esquema"] == esquema])
        escalas[esquema] = render(esquema, dot)
    SALIDA_TEX.write_text(latex(catalogo, versiones, escalas), encoding="utf-8")

    columnas = sum(len(t["columnas"]) for t in catalogo)
    fks = sum(1 for t in catalogo for r in t["restricciones"] if r["tipo"] == "f")
    print(f"{len(catalogo)} tablas, {columnas} columnas, {fks} claves foráneas "
          f"({sum(conteo.values())} entre esquemas) -> {SALIDA_TEX.relative_to(RAIZ)}, "
          f"{SALIDA_DER.relative_to(RAIZ)}/")


if __name__ == "__main__":
    main()

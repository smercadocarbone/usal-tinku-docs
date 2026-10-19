#!/usr/bin/env python3
"""Modelo financiero del capítulo 5 (anexo II), reproducible.

Recalcula los flujos, el VAN, la TIR y los repagos de los tres escenarios
con los parámetros declarados en el capítulo 5, y agrega la variante que
valoriza el tiempo del fundador en soporte, moderación y revisión de
credenciales (CAP y credencial académica).

Uso:  python3 anexos/modelo_financiero.py
Solo usa la biblioteca estándar.
"""

# ---------------------------------------------------------------------------
# Parámetros del modelo vigente (capítulo 5, tabla de parámetros del anexo II)
# ---------------------------------------------------------------------------
TICKET = 7.42                 # USD por sesión de 51 min (ecuación del ticket)
COMISION = 0.27               # comisión de la plataforma (BR-PAG-01)
MARGEN = TICKET * COMISION    # 2,0034 USD por sesión
INVERSION = 25_730            # USD, Año 0 (tabla de inversión inicial)
COSTOS_FIJOS = [3_555, 3_675, 3_915, 4_155, 4_395]   # USD por año
TASA = 0.15                   # tasa de descuento anual en USD

ALUMNOS = {                   # alumnos activos por año (tabla de demanda)
    "Pesimista": [130, 110, 160, 140, 190],
    "Base":      [200, 260, 210, 290, 250],
    "Optimista": [280, 420, 340, 480, 400],
}
CLASES_POR_ALUMNO_MES = 3

# ---------------------------------------------------------------------------
# Costo del tiempo del fundador (supuestos declarados en el capítulo 5)
# ---------------------------------------------------------------------------
# Salario: Administrativo A, CCT 130/75 (empleados de comercio), octubre de
# 2026, jornada completa: $1.316.632 (básico + suma fija), según iProfesional,
# 01/10/2026. Jornada máxima de 48 horas semanales (Ley 11.544, art. 1).
# Sueldo anual complementario: un sueldo más por año (Ley 20.744, art. 121).
SALARIO_MENSUAL_ARS = 1_316_632
HORAS_MES_JORNADA_COMPLETA = 48 * 52 / 12      # 208 horas
FACTOR_SAC = 13 / 12
TIPO_CAMBIO = 1_535                             # ARS por USD (BNA, 09/09/2026)
VALOR_HORA_USD = SALARIO_MENSUAL_ARS / HORAS_MES_JORNADA_COMPLETA * FACTOR_SAC / TIPO_CAMBIO

# Tiempos por tarea (supuestos propios, declarados en el capítulo 5)
TASA_CONSULTA = 0.05          # consultas de soporte por sesión
MIN_CONSULTA = 10
TASA_DISPUTA = 0.01           # disputas o reembolsos manuales por sesión
MIN_DISPUTA = 20
TASA_DENUNCIA = 0.005         # denuncias por sesión
MIN_DENUNCIA = 45
ALUMNOS_POR_TUTOR = 4         # tutores activos = alumnos activos / 4
DOCUMENTOS_POR_TUTOR_ANIO = 2  # CAP (vigencia 12 meses) + credencial académica
MIN_DOCUMENTO = 15
HORAS_FIJAS_MES = 52 / 12     # 1 hora semanal de revisión de paneles y colas


def horas_fundador_mes(alumnos):
    """Horas mensuales de soporte, moderación y revisión para un año."""
    sesiones_mes = alumnos * CLASES_POR_ALUMNO_MES
    tutores = alumnos / ALUMNOS_POR_TUTOR
    soporte = sesiones_mes * TASA_CONSULTA * MIN_CONSULTA / 60
    financiero = sesiones_mes * TASA_DISPUTA * MIN_DISPUTA / 60
    moderacion = sesiones_mes * TASA_DENUNCIA * MIN_DENUNCIA / 60
    credenciales = tutores * DOCUMENTOS_POR_TUTOR_ANIO / 12 * MIN_DOCUMENTO / 60
    return {
        "soporte": soporte,
        "financiero": financiero,
        "moderacion": moderacion,
        "credenciales": credenciales,
        "fijas": HORAS_FIJAS_MES,
        "total": soporte + financiero + moderacion + credenciales + HORAS_FIJAS_MES,
    }


def van(flujos, tasa=TASA):
    return sum(f / (1 + tasa) ** t for t, f in enumerate(flujos))


def tir(flujos):
    bajo, alto = -0.99, 10.0
    for _ in range(300):
        medio = (bajo + alto) / 2
        if van(flujos, medio) > 0:
            bajo = medio
        else:
            alto = medio
    return medio


def repago(flujos):
    acumulado = flujos[0]
    for m in range(1, len(flujos)):
        if acumulado + flujos[m] >= 0:
            return m - 1 + abs(acumulado) / flujos[m]
        acumulado += flujos[m]
    return None


def flujos(alumnos, factor_horas=None):
    serie = [-INVERSION]
    for a, fijo in zip(alumnos, COSTOS_FIJOS):
        sesiones = a * CLASES_POR_ALUMNO_MES * 12
        costo_fundador = 0.0
        if factor_horas is not None:
            costo_fundador = horas_fundador_mes(a)["total"] * factor_horas * 12 * VALOR_HORA_USD
        serie.append(sesiones * MARGEN - fijo - costo_fundador)
    return serie


def fmt(x, dec=0):
    s = f"{x:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def main():
    print(f"Margen por sesión: USD {fmt(MARGEN, 4)}")
    print(f"Valor hora (Administrativo A + SAC): ARS {fmt(VALOR_HORA_USD * TIPO_CAMBIO)} = USD {fmt(VALOR_HORA_USD, 2)}")
    print()
    print("Horas mensuales del fundador, escenario base:")
    for anio, a in enumerate(ALUMNOS["Base"], start=1):
        h = horas_fundador_mes(a)
        detalle = ", ".join(f"{k} {fmt(v, 1)}" for k, v in h.items() if k != "total")
        print(f"  Año {anio}: {fmt(h['total'], 1)} h ({detalle}) -> USD {fmt(h['total'] * VALOR_HORA_USD, 0)}/mes")
    print()
    print("Escenario | Variante | Flujos | VAN | TIR | Repago simple | Repago descontado")
    for esc, alumnos in ALUMNOS.items():
        for nombre, factor in (("sin costo del fundador", None),
                               ("con costo del fundador", 1.0),
                               ("con el doble de horas", 2.0)):
            f = flujos(alumnos, factor)
            desc = [x / (1 + TASA) ** t for t, x in enumerate(f)]
            rs, rd = repago(f), repago(desc)
            print(f"{esc} | {nombre} | {[round(x) for x in f]} | {fmt(van(f))} | "
                  f"{fmt(tir(f) * 100, 2)} % | {fmt(rs, 2) if rs else 'no'} | {fmt(rd, 2) if rd else 'no'}")
    # Horas mensuales constantes que anulan el VAN base
    base = flujos(ALUMNOS["Base"])
    anualidad = sum(1 / (1 + TASA) ** t for t in range(1, 6))
    excedente_mensual = van(base) / anualidad / 12
    print()
    print(f"Costo mensual constante que anula el VAN base: USD {fmt(excedente_mensual)} "
          f"= {fmt(excedente_mensual / VALOR_HORA_USD)} h/mes al valor hora de convenio")


if __name__ == "__main__":
    main()

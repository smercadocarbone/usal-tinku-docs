#!/usr/bin/env python3
"""Modelo financiero del capítulo 5 (anexo II), reproducible.

Recalcula los flujos, el VAN, la TIR y los repagos de los tres escenarios
con los parámetros declarados en el capítulo 5, agrega la variante que
valoriza el tiempo del fundador en soporte, moderación y revisión de
credenciales (CAP y credencial académica), los análisis de sensibilidad
del capítulo 5 y del apéndice de precio, y una cota con la inversión
valorizada a tarifas de contratista (USD 25.730).

Uso:  python3 anexos/modelo_financiero.py
Solo usa la biblioteca estándar.
"""

# ---------------------------------------------------------------------------
# Parámetros del modelo vigente (capítulo 5, tabla de parámetros del anexo II)
# ---------------------------------------------------------------------------
TICKET = 7.42                 # USD por sesión de 51 min (ecuación del ticket)
COMISION = 0.27               # comisión de la plataforma (BR-PAG-01)
MARGEN = TICKET * COMISION    # 2,0034 USD por sesión
INVERSION = 10_279            # USD, Año 0 (tabla de inversión inicial)
# Cota de referencia: inversión valorizada con las tarifas de contratista
# (USD 50/30/15 por hora) de la versión anterior del capítulo 5.
INVERSION_COTA = 25_730
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


def flujos_margen(alumnos, margen, inversion=None):
    """Flujos sin costo del fundador con un margen por sesión arbitrario."""
    serie = [-(INVERSION if inversion is None else inversion)]
    for a, fijo in zip(alumnos, COSTOS_FIJOS):
        serie.append(a * CLASES_POR_ALUMNO_MES * 12 * margen - fijo)
    return serie


def raiz(fn, bajo, alto):
    """Bisección para fn creciente: devuelve x con fn(x) = 0."""
    for _ in range(200):
        medio = (bajo + alto) / 2
        if fn(medio) > 0:
            alto = medio
        else:
            bajo = medio
    return medio


def flujos(alumnos, factor_horas=None, inversion=None):
    serie = [-(INVERSION if inversion is None else inversion)]
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
    sensibilidades()
    # Cota: los tres escenarios con la inversión a tarifas de contratista
    print()
    print(f"Cota con inversión de USD {fmt(INVERSION_COTA)} (sin costo del fundador):")
    for esc, alumnos in ALUMNOS.items():
        f = flujos(alumnos, inversion=INVERSION_COTA)
        desc = [x / (1 + TASA) ** t for t, x in enumerate(f)]
        rs, rd = repago(f), repago(desc)
        print(f"  {esc}: VAN {fmt(van(f))} | TIR {fmt(tir(f) * 100, 2)} % | "
              f"repago {fmt(rs, 2) if rs else 'no'} | descontado {fmt(rd, 2) if rd else 'no'}")
    # Inversión máxima que mantiene el VAN >= 0 en cada escenario
    print()
    for esc, alumnos in ALUMNOS.items():
        print(f"Inversión que anula el VAN {esc.lower()}: USD {fmt(van(flujos(alumnos)) + INVERSION)}")


PRECIO_HORA_ARS = 13_392.43   # promedio del relevamiento de Superprof
PISO_USD_HORA = 4             # piso de tarifa del sistema
DURACION_MIN = 51
NETO_MP = 0.0604              # comisión de MercadoPago a cargo del tutor


def sensibilidades(inversion=None):
    """Análisis de sensibilidad del capítulo 5 y del apéndice de precio.

    Los tickets alternativos se redondean a centavos, como en el texto.
    """
    base, pes = ALUMNOS["Base"], ALUMNOS["Pesimista"]
    v = lambda al, m: van(flujos_margen(al, m, inversion))
    print()
    print("Sensibilidad (escenario base salvo indicación):")
    sesiones_base = sum(base) * CLASES_POR_ALUMNO_MES * 12 / 5
    k = raiz(lambda k: v([a * k for a in base], MARGEN), 0, 1)
    print(f"  Volumen: el VAN base se anula con una caída de {fmt((1 - k) * 100, 1)} % "
          f"({fmt(k * sesiones_base)} sesiones anuales promedio, frente a {fmt(sesiones_base)})")
    m_eq = raiz(lambda m: v(base, m), 0, 5)
    t_eq = m_eq / COMISION
    print(f"  Comisión que anula el VAN base: {fmt(m_eq / TICKET * 100, 1)} %; "
          f"pesimista: {fmt(raiz(lambda m: v(pes, m), 0, 5) / TICKET * 100, 1)} %")
    print(f"  Ticket que anula el VAN base: USD {fmt(t_eq, 2)} por sesión = USD "
          f"{fmt(t_eq * 60 / DURACION_MIN, 2)} por hora = ARS {fmt(t_eq * 60 / DURACION_MIN * TIPO_CAMBIO)}; "
          f"tipo de cambio que lo anula: {fmt(PRECIO_HORA_ARS * DURACION_MIN / 60 / t_eq)} ARS/USD")
    t_piso = PISO_USD_HORA * DURACION_MIN / 60
    print(f"  Todas las sesiones al piso de tarifa (ticket USD {fmt(t_piso, 2)}): VAN base {fmt(v(base, t_piso * COMISION))}")
    for nombre, t in (("mitad en paquete con 30 %", TICKET * 0.85),
                      ("todo en paquete con 30 %", TICKET * 0.70)):
        print(f"  Paquete, {nombre}: ticket USD {fmt(t, 2)}, VAN base {fmt(v(base, t * COMISION))}")
    print(f"  Descuento medio de paquete que anula el VAN base: {fmt((1 - t_eq / TICKET) * 100, 1)} %")
    for d in (45, 60):
        t = round(PRECIO_HORA_ARS / TIPO_CAMBIO * d / 60, 2)
        print(f"  Duración {d} min: ticket USD {fmt(t, 2)}, VAN base {fmt(v(base, t * COMISION))}")
    d_eq = raiz(lambda d: v(base, TICKET * d / DURACION_MIN * COMISION), 0, 120)
    print(f"  Duración media que anula el VAN base: {fmt(d_eq, 1)} min")
    print("  Comisión | VAN base | TIR base | VAN pesimista | neto del tutor")
    for c in (m_eq / TICKET, 0.21, 0.23, 0.25, COMISION, 0.30, 0.33):
        f = flujos_margen(base, TICKET * c, inversion)
        print(f"  {fmt(c * 100, 1)} % | {fmt(van(f))} | {fmt(tir(f) * 100, 2)} % | "
              f"{fmt(v(pes, TICKET * c))} | {fmt((1 - c - NETO_MP) * 100, 2)} %")
    print("  Tipo de cambio | ticket | margen | sesiones eq. Año 1 | Año 5 | VAN base | TIR base")
    for tc in (1_400, TIPO_CAMBIO, 1_700, 1_900, 2_100):
        t = TICKET if tc == TIPO_CAMBIO else round(PRECIO_HORA_ARS * DURACION_MIN / 60 / tc, 2)
        m = t * COMISION
        f = flujos_margen(base, m, inversion)
        print(f"  {fmt(tc)} | {fmt(t, 2)} | {fmt(m, 2)} | {fmt(COSTOS_FIJOS[0] / m)} | "
              f"{fmt(COSTOS_FIJOS[-1] / m)} | {fmt(van(f))} | {fmt(tir(f) * 100, 2)} %")


# Riesgo R-09 (capítulo 6): costo de un desarrollador rentado a jornada
# completa, con las tarifas por hora de la tabla de inversión del capítulo 5
# (medianas de Sysarmy 2026.1 divididas por 160 horas mensuales).
HORAS_MES_RENTADO = 160
TARIFAS_RENTADO = {"junior": 7, "semi-senior": 11}   # USD por hora


def equipo_rentado(inversion=None):
    """VAN de cada escenario restando un desarrollador rentado (R-09)."""
    print()
    print("R-09: VAN con un desarrollador rentado a jornada completa (sin costo del fundador):")
    for perfil, tarifa in TARIFAS_RENTADO.items():
        anual = tarifa * HORAS_MES_RENTADO * 12
        print(f"  {perfil}: USD {fmt(tarifa)}/h x {HORAS_MES_RENTADO} h = USD "
              f"{fmt(tarifa * HORAS_MES_RENTADO)}/mes (USD {fmt(anual)}/año)")
        for esc, alumnos in ALUMNOS.items():
            f = flujos(alumnos, inversion=inversion)
            f = [f[0]] + [x - anual for x in f[1:]]
            print(f"    {esc}: flujos {[round(x) for x in f]} | VAN {fmt(van(f))} | "
                  f"TIR {fmt(tir(f) * 100, 2) + ' %' if van(f, -0.98) > 0 else 'no existe'}")


if __name__ == "__main__":
    main()
    equipo_rentado()

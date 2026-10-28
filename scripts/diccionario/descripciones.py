"""Descripciones del diccionario de datos (apéndice C).

La estructura (tipos, nulos, claves, restricciones e índices) NO se escribe acá: la lee
generar.py del catálogo de PostgreSQL después de aplicar todas las migraciones. Este archivo
solo aporta el significado de cada esquema, tabla y columna. generar.py falla si una tabla o
columna de la base no tiene descripción, o si acá sobra alguna que la base ya no tiene.

Los textos son LaTeX: se insertan tal cual.
"""

ESQUEMAS = {
    "identidad": ("M1", "Identidad y perfiles: cuentas de usuario, verificación del tutor "
                  "(credenciales, especialidades y \\gls{cap}), autorizaciones y consentimientos "
                  "de los menores, y control de reintentos."),
    "matching": ("M2", "Motor de \\gls{matching}: catálogo de trayectos y temas con sus "
                 "\\gls{embeddings}, perfil semántico del tutor, búsquedas guardadas, temas "
                 "buscados sin cobertura e instrumentación de la evaluación."),
    "aula": ("M3", "Aula virtual: sesión de clase asociada a cada reserva, alertas del "
             "kill-switch y confirmación de la contraparte en la rama de adultos."),
    "reservas": ("M4", "Reservas y agenda: franjas de disponibilidad, solicitudes del menor, "
                 "reservas, paquetes mensuales, pedidos previos, notas y reprogramaciones."),
    "pagos": ("M5", "Motor de pagos: transacción de cada reserva con su estado de "
              "\\gls{escrow}, tarifas, cuentas de MercadoPago de los tutores, preferencias de "
              "pago y estado global de la pasarela."),
    "resumen": ("M6", "Resumen automático de la sesión y su ciclo de reintentos."),
    "reputacion": ("M7", "Calificaciones bidireccionales y señales implícitas de "
                   "comportamiento del tutor."),
    "admin": ("M8", "Panel de administración: administradores, auditoría, tickets de soporte, "
              "notificaciones y respuestas \\gls{nps}."),
    "seguridad": ("M9", "Denuncias y sanciones."),
}

ID_BASE = "Identificador (UUID generado por la base)"
ID_APP = "Identificador (UUID generado por la aplicación)"
CREADO = "Fecha y hora de creación de la fila"

TABLAS = {
    # ---------------------------------------------------------------- identidad
    "identidad.usuarios": (
        "Cuenta de cada persona registrada. Un adulto tiene al menos una de dos capacidades "
        "(estudiante y Adulto Responsable); un menor siempre está vinculado a su Adulto "
        "Responsable. Los administradores también son usuarios (ver \\path{admin.admins}).",
        {
            "id": ID_BASE,
            "dni": "\\gls{dni} verificado por \\gls{ocr} al registrarse; es el identificador de inicio de sesión",
            "nombre": "Nombre, tal como figura en el \\gls{dni}",
            "apellido": "Apellido, tal como figura en el \\gls{dni}",
            "fecha_nacimiento": "Fecha de nacimiento; define si la cuenta es de un menor",
            "tipo": "Tipo de cuenta: ADULTO, MENOR o TUTOR",
            "capacidad_estudiante": "El adulto toma clases para sí mismo",
            "capacidad_adulto_responsable": "El adulto tiene menores a cargo",
            "adulto_responsable_id": "Adulto Responsable del menor; obligatorio solo para el tipo MENOR",
            "password_hash": "Hash de la contraseña (nunca la contraseña)",
            "estado_cuenta": "ACTIVA, SUSPENDIDA o BAJA; una baja anonimiza los datos en lugar de borrar la fila (ADR-M1-05)",
            "created_at": "Fecha y hora del alta",
            "activo_para_matching": "El tutor puede aparecer en las búsquedas; lo apagan el vencimiento del \\gls{cap} y las sanciones",
            "email": "Correo de contacto; único entre los no nulos. Es nulo en cuentas anteriores a V18",
            "bio": "Presentación del tutor en su perfil público (hasta 500 caracteres)",
            "foto_ref": "Referencia interna de la foto de perfil en el almacenamiento (nunca una URL pública)",
            "credentials_version": "Versión de las credenciales; cambia con la contraseña e invalida los \\gls{jwt} emitidos antes",
            "acepta_menores": "Preferencia del tutor de dar clases a menores; con \\texttt{false} no aparece para ningún menor",
        },
    ),
    "identidad.credenciales_academicas": (
        "Documento que respalda la formación del tutor, con su triaje automático y la "
        "decisión del administrador de moderación.",
        {
            "id": ID_BASE,
            "tutor_id": "Tutor que presenta la credencial",
            "tipo_documento": "Clase de documento; los tres primeros valores son del esquema anterior a V56 y se siguen admitiendo",
            "archivo_url": "Referencia interna del archivo subido",
            "estado": "PENDIENTE, APROBADO o RECHAZADO",
            "numero_intento": "Número de intento dentro del ciclo actual (1 a 3)",
            "ciclo_espera_hasta": "Fin de la espera tras agotar los intentos del ciclo",
            "admin_revisor_id": "Usuario administrador que resolvió la revisión; sin clave foránea declarada",
            "created_at": "Fecha y hora de presentación",
            "revisado_at": "Fecha y hora de la resolución",
            "institucion": "Institución que emitió el título",
            "denominacion": "Nombre del título o de la carrera",
            "anio_egreso": "Año de egreso (1900 a 2100)",
            "es_digital": "El documento es un título digital con enlace de verificación",
            "enlace_verificacion": "Enlace de verificación del título digital",
            "nombre_coincide": "Resultado del \\gls{ocr} contra el nombre del \\gls{dni}; nulo si no se pudo comparar. Solo marca, nunca rechaza",
            "metodo_verificacion": "Cómo se aprobó: contra el registro oficial o solo con el documento",
            "motivo_rechazo": "Motivo codificado del rechazo",
            "detalle_rechazo": "Explicación libre del rechazo para el tutor",
        },
    ),
    "identidad.autorizaciones_tutor": (
        "Tutores que el Adulto Responsable autorizó para cada uno de sus menores. Un menor "
        "solo puede tomar clase con un tutor autorizado.",
        {
            "id": ID_BASE,
            "adulto_responsable_id": "Adulto Responsable que autoriza",
            "menor_id": "Menor al que se aplica la autorización",
            "tutor_id": "Tutor autorizado",
            "no_confiable": "El adulto marcó al tutor como no confiable; bloquea nuevas reservas",
            "created_at": "Fecha y hora de la autorización",
        },
    ),
    "identidad.consentimientos_menor": (
        "Consentimiento del Adulto Responsable para el uso de la plataforma por el menor, "
        "con la versión del texto aceptado.",
        {
            "id": ID_BASE,
            "menor_id": "Menor al que se refiere el consentimiento",
            "adulto_responsable_id": "Adulto Responsable que lo otorga",
            "version_texto": "Versión del texto de consentimiento aceptado",
            "aceptado_at": "Fecha y hora de la aceptación",
            "revocado_at": "Fecha y hora de la revocación; nulo si sigue vigente",
        },
    ),
    "identidad.intentos_ocr": (
        "Reintentos de la foto del \\gls{dni} en el alta, por \\gls{dni} declarado. La "
        "espera se evalúa al leer, sin trabajo programado.",
        {
            "dni": "\\gls{dni} declarado por quien intenta registrarse",
            "intentos_consumidos": "Fotos ilegibles en el ciclo actual; el tope lo fija la aplicación (\\path{tinku.ocr.max-intentos})",
            "proximo_intento_permitido": "Fin de la espera de 24 horas; nulo si no hay espera",
            "updated_at": "Fecha y hora de la última modificación",
        },
    ),
    "identidad.intentos_credencial": (
        "Ciclos de reintento de credencial agotados por cada tutor, para escalar la espera "
        "(24, 48, 96 horas\\ldots). La comparten credenciales y \\gls{cap}.",
        {
            "tutor_id": "Tutor al que corresponde el contador",
            "veces_ciclo_agotado": "Cantidad de ciclos agotados; la espera es $24 \\cdot 2^n$ horas",
            "proximo_intento_permitido": "Fin de la espera actual; nulo si no hay espera",
            "updated_at": "Fecha y hora de la última modificación",
        },
    ),
    "identidad.certificados_antecedentes_penales": (
        "\\gls{cap} del tutor: habilita a dar clases a menores. Incluye la cola de "
        "verificación de la firma digital con el validador oficial (ADR-M1-10).",
        {
            "id": ID_BASE,
            "tutor_id": "Tutor que presenta el certificado",
            "archivo_url": "Referencia interna del archivo subido",
            "fecha_emision": "Fecha de emisión del certificado",
            "vence_at": "Fecha de vencimiento",
            "estado": "PENDIENTE, APROBADO, RECHAZADO, EN\\_REVISION\\_LEGAL (nunca se resuelve sola) o VENCIDO",
            "tiene_antecedentes": "El certificado informa antecedentes",
            "categoria_antecedente": "Categoría del antecedente informado, si lo hay",
            "numero_intento": "Número de intento dentro del ciclo actual (1 a 3)",
            "ciclo_espera_hasta": "Fin de la espera tras agotar los intentos del ciclo",
            "admin_revisor_id": "Usuario administrador que resolvió la revisión; sin clave foránea declarada",
            "created_at": "Fecha y hora de presentación",
            "revisado_at": "Fecha y hora de la resolución",
            "firma_estado": "Estado de la verificación de la firma digital en la cola",
            "firma_detalle": "Detalle corto del resultado del validador (no se guarda la respuesta completa)",
            "firma_firmante": "Firmante informado por el validador",
            "firma_sha256": "Hash del archivo enviado; el resultado solo vale si el validador informa el mismo",
            "firma_solicitud_id": "Identificador de la solicitud en el validador",
            "firma_intentos": "Intentos de verificación realizados",
            "firma_proximo_intento_at": "Momento del próximo envío o consulta de la cola",
            "firma_enviada_at": "Fecha y hora del envío al validador",
            "firma_verificada_at": "Fecha y hora del resultado del validador",
        },
    ),
    "identidad.aceptaciones_clausula": (
        "Consentimiento expreso (Ley 25.326): qué usuario aceptó qué versión de qué cláusula "
        "(Términos, grabación del audio) y cuándo.",
        {
            "id": ID_BASE,
            "usuario_id": "Usuario que acepta",
            "clausula": "Cláusula aceptada",
            "version": "Versión del texto aceptado",
            "aceptada_at": "Fecha y hora de la aceptación",
        },
    ),
    "identidad.tokens_reset_password": (
        "Recuperación de contraseña: token opaco de un solo uso. Se guarda solo su hash, de "
        "modo que una filtración de la tabla no permite restablecer cuentas.",
        {
            "id": ID_APP,
            "usuario_id": "Usuario que pidió el restablecimiento",
            "token_hash": "Hash SHA-256 (64 caracteres hexadecimales) del token enviado por correo",
            "expira_en": "Vencimiento del token",
            "usado_en": "Fecha y hora de uso; nulo si no se usó",
            "created_at": CREADO,
        },
    ),
    "identidad.especialidades_tutor": (
        "Materias que el tutor declara enseñar (de una a tres) con el nivel máximo. Su "
        "estado de verificación no se guarda: se deriva de las credenciales aprobadas que la "
        "cubren. Se usa solo con \\path{tinku.especialidades.habilitado}.",
        {
            "id": ID_BASE,
            "tutor_id": "Tutor que declara la especialidad",
            "materia": "Materia del catálogo de temas",
            "nivel_maximo": "Nivel más alto que puede enseñar: PRIMARIO, SECUNDARIO o UNIVERSITARIO",
            "created_at": CREADO,
        },
    ),
    "identidad.credencial_especialidades": (
        "Tabla asociativa: qué especialidades cubre una credencial aprobada. La elige el "
        "administrador al aprobar; si el tutor borra la especialidad, la cobertura se borra "
        "con ella.",
        {
            "credencial_id": "Credencial aprobada",
            "especialidad_id": "Especialidad cubierta",
        },
    ),
    # ---------------------------------------------------------------- matching
    "matching.materias_niveles": (
        "Catálogo inicial de materias por nivel (V7). Lo reemplazó el catálogo de trayectos "
        "y temas (V19); solo lo usa el endpoint heredado \\path{PUT /api/perfil-matching}.",
        {
            "id": ID_BASE,
            "nivel": "primario, secundario o universitario",
            "materia": "Nombre de la materia",
        },
    ),
    "matching.perfiles_tutor_matching": (
        "Perfil del tutor para el motor de \\gls{matching}: temas elegidos y "
        "\\gls{embeddings} del perfil.",
        {
            "tutor_id": "Tutor al que pertenece el perfil",
            "materias_niveles_ids": "Materias del catálogo inicial; arreglo sin clave foránea, solo lo llena el endpoint heredado",
            "embedding": "\\gls{embeddings} del perfil completo (384 dimensiones); se usa solo si ninguno de sus temas tiene \\gls{embeddings}",
            "activo_para_matching": "Bandera de V7; el filtro que se aplica es \\path{identidad.usuarios.activo_para_matching}",
            "tema_ids": "Temas del catálogo elegidos por el tutor; arreglo sin clave foránea, con índice GIN",
        },
    ),
    "matching.busquedas_guardadas": (
        "Búsquedas que el usuario guarda para volver a ejecutar; se guardan la consulta y "
        "los filtros, nunca la lista de resultados.",
        {
            "id": ID_BASE,
            "usuario_id": "Usuario que guardó la búsqueda",
            "texto_busqueda": "Texto libre de la consulta",
            "created_at": CREADO,
            "filtros": "Filtros aplicados (nivel, materia, nombre, precio máximo) en JSON",
            "huella": "SHA-256 del texto normalizado y los filtros ordenados; impide guardar dos veces la misma búsqueda",
        },
    ),
    "matching.trayectos": (
        "Catálogo cerrado de trayectos: nivel, año o carrera y materia. Lo siembra "
        "\\path{V20__m2_temas_seed.sql}.",
        {
            "id": ID_BASE,
            "nivel": "primario, secundario o universitario",
            "anio_o_carrera": "Año o curso (por ejemplo, ``4°'') o carrera",
            "materia": "Nombre de la materia",
        },
    ),
    "matching.temas": (
        "Temas de cada trayecto: la unidad que elige el tutor y con la que se calcula la "
        "similitud de una búsqueda (ADR-M2-03).",
        {
            "id": ID_BASE,
            "trayecto_id": "Trayecto al que pertenece el tema",
            "nombre": "Nombre del tema",
            "descripcion": "Qué se trabaja en el tema; es el texto que se convierte en \\gls{embeddings}",
            "orden": "Posición del tema dentro del trayecto",
            "embedding": "\\gls{embeddings} del tema (384 dimensiones); nulo si ningún tutor lo eligió todavía",
            "embedding_fuente": "Texto con el que se calculó el \\gls{embeddings}; si cambia, se recalcula",
        },
    ),
    "matching.temas_sugeridos": (
        "Contador agregado de temas buscados que el catálogo no cubre (ADR-M2-04). No "
        "guarda quién buscó ni una fila por búsqueda, y excluye las búsquedas de menores. "
        "El servicio la mantiene en 500 filas como máximo.",
        {
            "id": ID_BASE,
            "texto": "Texto de búsqueda normalizado",
            "veces": "Cantidad de veces que se buscó",
            "nivel": "Nivel del tema del catálogo más parecido",
            "materia": "Materia del tema del catálogo más parecido",
            "ultima_vez": "Fecha y hora de la última búsqueda",
        },
    ),
    "matching.evaluacion_busquedas": (
        "Instrumentación de la evaluación del \\gls{matching} (indicador I-01): qué tutores "
        "se mostraron y en qué orden. No guarda el texto buscado ni las búsquedas de "
        "menores. Solo se escribe con \\path{tinku.evaluacion.habilitada}.",
        {
            "id": ID_BASE,
            "usuario_id": "Usuario que buscó",
            "longitud_texto": "Longitud del texto buscado, en caracteres",
            "cantidad_resultados": "Cantidad de tutores devueltos",
            "tutor_ids": "Tutores mostrados, en el orden del ranking",
            "created_at": "Fecha y hora de la búsqueda",
        },
    ),
    "matching.evaluacion_aceptaciones": (
        "Instrumentación de la evaluación (I-01): el usuario abrió el perfil o reservó a un "
        "tutor sugerido en una búsqueda registrada.",
        {
            "id": ID_BASE,
            "busqueda_id": "Búsqueda registrada en la que apareció el tutor",
            "tutor_id": "Tutor aceptado",
            "posicion": "Posición del tutor en el ranking (1 es el primero); la calcula el servidor",
            "tipo": "PERFIL (abrió el perfil) o RESERVA (reservó)",
            "created_at": "Fecha y hora de la aceptación",
        },
    ),
    # ---------------------------------------------------------------- aula
    "aula.sesiones_aprendizaje": (
        "Sesión de aula de una reserva (relación 1 a 1): sala de video, asistencia, "
        "conexión y duración. No guarda grabaciones de video.",
        {
            "id": ID_BASE,
            "reserva_id": "Reserva a la que corresponde la sesión",
            "livekit_room_id": "Sala de LiveKit; nula hasta que se crea, 5 minutos antes del inicio",
            "estado": "Estado de la clase",
            "inicio_real": "Momento en que empezó la clase",
            "fin_real": "Momento en que terminó la clase",
            "duracion_efectiva_segundos": "Duración efectiva, calculada al finalizar; decide la regla del 50\\,\\% y el umbral del resumen",
            "created_at": CREADO,
            "updated_at": "Fecha y hora de la última modificación",
            "estudiante_joined_at": "Primera entrada del estudiante a la sala (webhook de LiveKit)",
            "tutor_joined_at": "Primera entrada del tutor a la sala (webhook de LiveKit)",
            "duracion_agendada_segundos": "Duración agendada, congelada al programar la sesión",
            "tutor_conectado": "El tutor está conectado en este momento",
            "estudiante_conectado": "El estudiante está conectado en este momento",
            "par_roto_at": "Desde cuándo falta alguno de los dos; nulo si están ambos o no empezó",
            "audio_referencia": "Referencia interna del audio para el resumen contratado",
            "audio_recibido_at": "Fecha y hora de recepción del audio",
            "audio_borrado_at": "Fecha y hora del borrado del audio",
            "estudiante_admitido_at": "Momento en que el tutor admitió al estudiante desde la sala de espera",
        },
    ),
    "aula.alertas_seguridad": (
        "Alerta del kill-switch. Es una entidad distinta de la denuncia: la revisa "
        "moderación dentro de 12 horas, sin esperar descargo.",
        {
            "id": ID_BASE,
            "sesion_id": "Sesión en la que se detectó el contenido",
            "rama": "menor o adultos; la decide el backend con datos de M1, nunca el cliente",
            "detectado_id": "Usuario cuyo video disparó la detección",
            "clip_url": "Referencia al clip de evidencia",
            "clip_retencion_hasta": "Fin de la retención del clip: 30 días desde la resolución",
            "estado": "Estado de la revisión",
            "created_at": "Fecha y hora de la detección",
            "descargo_texto": "Descargo del usuario detectado (hasta 300 caracteres); no bloquea la resolución",
            "descargo_recibido_at": "Fecha y hora del descargo",
        },
    ),
    "aula.confirmaciones_killswitch": (
        "Pregunta a la contraparte en la rama de adultos del kill-switch, antes de cortar "
        "la clase (ADR-M3-07). Sin respuesta en plazo, cuenta como ``No''.",
        {
            "id": ID_BASE,
            "sesion_id": "Sesión en la que se hizo la pregunta (una por sesión)",
            "detectado_id": "Usuario cuyo video disparó la detección",
            "respondido_id": "Usuario que respondió; nulo mientras se espera la respuesta",
            "vio": "Respuesta: si la contraparte vio el contenido; nula hasta que responda",
            "created_at": "Fecha y hora de la pregunta",
            "responded_at": "Fecha y hora de la respuesta",
            "vence_at": "Fin del plazo para responder",
            "vencida": "El plazo venció sin respuesta",
        },
    ),
    # ---------------------------------------------------------------- reservas
    "reservas.franjas_disponibilidad": (
        "Franjas que publica el tutor: semanales (día de la semana) o puntuales (fecha). Solo "
        "se reserva dentro de una franja activa.",
        {
            "id": ID_BASE,
            "tutor_id": "Tutor que publica la franja",
            "dia_semana": "Día de la semana de una franja semanal (0 = domingo a 6 = sábado)",
            "fecha_especifica": "Fecha de una franja puntual",
            "hora_inicio": "Hora de inicio (hora de Argentina)",
            "hora_fin": "Hora de fin, posterior al inicio",
            "activa": "La franja está publicada",
        },
    ),
    "reservas.solicitudes_sesion": (
        "Pedido de clase que hace un menor. No bloquea el horario ni genera cobro: el Adulto "
        "Responsable la aprueba y paga para convertirla en reserva. Vence a las 48 horas.",
        {
            "id": ID_BASE,
            "menor_id": "Menor que pide la clase",
            "tutor_id": "Tutor pedido",
            "horario_propuesto": "Inicio propuesto para la clase",
            "estado": "pendiente, convertida, expirada o rechazada",
            "created_at": CREADO,
            "expira_at": "Vencimiento de la solicitud",
            "duracion_minutos": "Duración pedida (30 a 180 minutos, en bloques de 30)",
        },
    ),
    "reservas.reservas": (
        "Clase reservada. Distingue a quien paga, a quien recibe la clase y al tutor, y "
        "congela el precio y la duración al crearse.",
        {
            "id": ID_BASE,
            "pagador_id": "Quien paga: el estudiante adulto o el Adulto Responsable",
            "beneficiario_id": "Quien recibe la clase",
            "tutor_id": "Tutor que dicta la clase",
            "solicitud_origen_id": "Solicitud del menor que originó la reserva, si la hubo",
            "horario": "Inicio de la clase",
            "precio": "Precio de la clase, congelado al reservar",
            "estado": "Estado de la reserva",
            "motivo_cancelacion": "Motivo de la cancelación; obligatorio solo en estado \\texttt{cancelada}",
            "created_at": CREADO,
            "duracion_minutos": "Duración (30 a 180 minutos, en bloques de 30)",
            "horario_fin": "Fin de la clase; existe porque una restricción EXCLUDE no admite \\texttt{horario + intervalo}",
            "resumen_contratado": "Se contrató el adicional de resumen",
            "precio_adicional_resumen": "Precio congelado del adicional; presente si y solo si se contrató",
            "paquete_id": "Paquete mensual al que pertenece la clase, si lo hay",
        },
    ),
    "reservas.paquetes": (
        "Paquete mensual: varias clases semanales con un solo pago (ADR-M5-03). Cada clase "
        "es una reserva con \\path{paquete_id}; la primera es el ancla del pago.",
        {
            "id": ID_APP,
            "pagador_id": "Quien paga el paquete",
            "beneficiario_id": "Quien recibe las clases",
            "tutor_id": "Tutor que dicta las clases",
            "reserva_ancla_id": "Primera reserva del paquete; es la referencia del pago en MercadoPago",
            "cantidad_clases": "Cantidad de clases del paquete",
            "duracion_minutos": "Duración de cada clase",
            "descuento_porcentaje": "Descuento aplicado (0 a 30\\,\\%)",
            "precio_total": "Precio total congelado del paquete",
            "estado": "pendiente\\_pago, confirmado o cancelado",
            "vigente_hasta": "Fin de la vigencia del paquete",
            "created_at": CREADO,
        },
    ),
    "reservas.pedidos_previos": (
        "Texto que el alumno o su Adulto Responsable deja antes de la clase para el tutor "
        "(una fila por reserva).",
        {
            "reserva_id": "Reserva a la que corresponde el pedido",
            "texto": "Contenido del pedido (hasta 1000 caracteres)",
            "created_at": CREADO,
            "updated_at": "Fecha y hora de la última edición",
        },
    ),
    "reservas.notas_clase": (
        "Nota del tutor al Adulto Responsable sobre la clase (una fila por reserva).",
        {
            "reserva_id": "Reserva a la que corresponde la nota",
            "texto": "Contenido de la nota (hasta 1000 caracteres)",
            "created_at": CREADO,
            "updated_at": "Fecha y hora de la última edición",
        },
    ),
    "reservas.pedidos_reprogramacion": (
        "Pedido del tutor para cambiar el horario de una reserva. Puede haber uno solo "
        "pendiente por reserva; los resueltos quedan como historial.",
        {
            "id": ID_APP,
            "reserva_id": "Reserva que se quiere reprogramar",
            "horario_original": "Horario de la reserva al hacer el pedido",
            "horario_propuesto": "Nuevo horario propuesto",
            "motivo": "Motivo informado por el tutor",
            "estado": "pendiente, aceptado, rechazado, vencido o retirado",
            "created_at": CREADO,
            "resuelto_at": "Fecha y hora de la resolución",
        },
    ),
    # ---------------------------------------------------------------- pagos
    "pagos.transacciones": (
        "Cobro de una reserva (una por reserva) con la comisión de la plataforma y el estado "
        "del \\gls{escrow}. Con el modelo de cobro A (ADR-M5-02) el dinero ya está en la "
        "cuenta del tutor y \\path{retenido_escrow} indica que sigue abierta la ventana en la "
        "que se puede reembolsar.",
        {
            "id": ID_BASE,
            "reserva_id": "Reserva cobrada",
            "mp_payment_id": "Identificador del pago en MercadoPago",
            "monto_bruto": "Monto cobrado",
            "comision_plataforma": "Comisión de la plataforma; no supera el monto bruto",
            "estado": "Estado del \\gls{escrow}",
            "liberar_at": "Momento de liberación: fin de la clase más 24 horas",
            "intentos_liberacion": "Fallos del trabajo de liberación (con 3 pasa a intervención manual)",
            "created_at": "Fecha y hora del pago aprobado",
            "en_bypass": "Nació con la pasarela deshabilitada: sin dinero real, liberar y reembolsar no llaman a MercadoPago",
            "monto_adicional_resumen": "Parte del cobro que corresponde al adicional de resumen",
            "adicional_reembolsado_at": "Fecha y hora del reembolso del adicional",
            "adicional_reembolso_estado": "Estado del reembolso del adicional cuando el resumen falla",
            "adicional_reembolso_intentos": "Intentos del reembolso del adicional",
            "adicional_reembolso_error": "Último error del reembolso del adicional",
            "adicional_reembolso_nota": "Nota de Soporte Financiero al resolverlo a mano",
            "reembolso_parcial_monto": "Monto del reembolso parcial manual (uno por transacción)",
            "reembolso_parcial_at": "Fecha y hora del reembolso parcial manual",
        },
    ),
    "pagos.precios_referencia_regional": (
        "Precio de referencia por provincia, versionado: una versión nueva nunca pisa la "
        "anterior. Se toma como vigente la de mayor versión.",
        {
            "provincia": "Provincia",
            "version": "Número de versión (desde 1)",
            "valor_sugerido": "Precio sugerido",
            "vigente_desde": "Inicio de la vigencia",
        },
    ),
    "pagos.tarifas_tutor": (
        "Tarifa vigente de cada tutor y configuración de su paquete mensual. Solo rige hacia "
        "adelante: las reservas existentes conservan su precio.",
        {
            "tutor_id": "Tutor al que pertenece la tarifa",
            "precio_hora": "Precio por hora; la reserva cotiza \\texttt{precio\\_hora} $\\times$ duración / 60",
            "updated_at": "Fecha y hora del último cambio",
            "paquete_habilitado": "El tutor ofrece paquete mensual",
            "paquete_descuento_porcentaje": "Descuento del paquete (0 a 30\\,\\%)",
        },
    ),
    "pagos.pasarela_estado": (
        "Estado global de la pasarela de pagos, en una única fila. Si falta, se asume "
        "habilitada: la falta del dato nunca hace pasar un cobro por bypass.",
        {
            "id": "Siempre 1 (fila única)",
            "habilitada": "Cobro real con MercadoPago; con \\texttt{false}, modo bypass",
            "updated_at": "Fecha y hora del último cambio",
            "updated_by": "Usuario administrador que hizo el cambio",
        },
    ),
    "pagos.preferencias_pago": (
        "Preferencia de pago de MercadoPago generada para cada reserva, para conciliar el "
        "pago aunque no vuelva el navegador ni llegue el webhook.",
        {
            "reserva_id": "Reserva a la que corresponde la preferencia",
            "preference_id": "Identificador de la preferencia en MercadoPago",
            "created_at": CREADO,
            "conciliado_at": "Momento en que la reserva ya tiene su transacción; el barrido deja de mirarla",
            "intentos_conciliacion": "Intentos del barrido de conciliación",
            "alertado_at": "Aviso a Soporte por un pago aprobado que no se pudo atribuir (se avisa una vez)",
        },
    ),
    "pagos.cuentas_mp_tutor": (
        "Cuenta de MercadoPago que cada tutor conecta por \\gls{oauth} (modelo A, "
        "ADR-M5-02). Los tokens se guardan cifrados con AES-256-GCM y la clave está fuera "
        "de la base.",
        {
            "tutor_id": "Tutor dueño de la cuenta",
            "mp_user_id": "Identificador del usuario en MercadoPago",
            "access_token_cifrado": "Token de acceso, cifrado",
            "refresh_token_cifrado": "Token de renovación, cifrado",
            "public_key": "Clave pública de la cuenta",
            "expira_at": "Vencimiento del token de acceso",
            "estado": "CONECTADA, REVOCADA o ERROR",
            "conectada_at": "Fecha y hora de la conexión",
            "updated_at": "Fecha y hora de la última modificación",
        },
    ),
    "pagos.oauth_estados": (
        "Estado temporal del flujo de autorización \\gls{oauth}; dura minutos.",
        {
            "state": "Valor \\texttt{state} contra CSRF",
            "tutor_id": "Tutor que inició la conexión",
            "code_verifier": "Verificador PKCE",
            "expira_at": "Vencimiento del estado",
        },
    ),
    # ---------------------------------------------------------------- resumen
    "resumen.resumenes_sesion": (
        "Resumen automático de una sesión (uno por sesión, no se regenera). Solo existe para "
        "sesiones de al menos 10 minutos efectivos con el adicional contratado.",
        {
            "id": ID_BASE,
            "sesion_id": "Sesión resumida",
            "estado": "Estado del resumen",
            "prompt_anonimizado": "Prompt enviado al modelo, ya anonimizado",
            "transcript_anonimizado": "Transcripción anonimizada; se guarda aunque no haya proveedor configurado",
            "resumen_final": "Resumen generado; nulo hasta generarlo",
            "intentos": "Intentos de generación",
            "proximo_reintento_at": "Momento del próximo reintento (espera de 5, 15 y 60 minutos)",
            "recordatorio_pendiente": "Falta enviar el recordatorio único de 24 horas",
            "suspendido_seguridad": "Hay una denuncia o alerta activa sobre la sesión",
            "created_at": CREADO,
        },
    ),
    # ---------------------------------------------------------------- reputacion
    "reputacion.calificaciones": (
        "Calificación de una sesión. Es bidireccional: el estudiante califica al tutor y el "
        "tutor al estudiante; la dirección se deriva del rol del autor.",
        {
            "id": ID_BASE,
            "sesion_id": "Sesión calificada",
            "autor_id": "Usuario que califica",
            "direccion": "estudiante\\_a\\_tutor o tutor\\_a\\_estudiante",
            "estrellas": "Puntaje de 1 a 5",
            "comentario": "Comentario; solo en la dirección estudiante\\_a\\_tutor",
            "editable_hasta": "Fin del plazo de edición: 48 horas desde la creación",
            "created_at": CREADO,
        },
    ),
    "reputacion.senales_implicitas_tutor": (
        "Señales de comportamiento del tutor, agregadas y recalculadas de forma incremental "
        "(ADR-M7-01). No es un registro de eventos.",
        {
            "tutor_id": "Tutor al que corresponden las señales",
            "puntualidad_promedio": "Puntualidad promedio (0 a 1)",
            "tasa_recontratacion": "Proporción de alumnos que vuelven a reservar",
            "tasa_cancelacion_noshow": "Proporción de clases canceladas o con ausencia del tutor",
            "tiempo_respuesta_promedio_min": "Tiempo promedio de respuesta, en minutos",
            "sesiones_dictadas_total": "Cantidad de sesiones dictadas",
            "updated_at": "Fecha y hora del último recálculo",
        },
    ),
    # ---------------------------------------------------------------- admin
    "admin.admins": (
        "Personal interno con acceso al panel. Cada administrador está vinculado a un "
        "usuario y tiene exactamente uno de dos roles.",
        {
            "id": ID_BASE,
            "usuario_id": "Usuario vinculado (uno por administrador)",
            "rol": "MODERACION\\_SEGURIDAD o SOPORTE\\_FINANCIERO",
            "activo": "El administrador puede operar",
            "created_at": CREADO,
        },
    ),
    "admin.mapeo_origen_rol": (
        "Configuración del enrutamiento de tickets: qué rol atiende cada origen. Se edita "
        "sin desplegar código.",
        {
            "origen_modulo": "Origen del ticket (por ejemplo, \\path{M5.pago_fallido})",
            "rol_asignado": "Rol que atiende los tickets de ese origen",
        },
    ),
    "admin.tickets_soporte": (
        "Pedidos del canal ``contactar a soporte''. El origen debe existir en el mapeo, de "
        "modo que siempre se puede derivar el rol.",
        {
            "id": ID_BASE,
            "usuario_id": "Usuario que abre el ticket",
            "origen_modulo": "Origen del ticket",
            "asunto": "Asunto",
            "detalle": "Descripción del problema",
            "estado": "ABIERTO, EN\\_PROCESO, RESUELTO o CERRADO",
            "rol_asignado": "Rol que lo atiende, derivado del origen",
            "creado_en": CREADO,
            "resuelto_en": "Fecha y hora de la resolución",
        },
    ),
    "admin.log_auditoria_admin": (
        "Auditoría de cada acción de un administrador. Es de solo agregado a nivel del "
        "motor: la tabla pertenece a un rol sin inicio de sesión y la aplicación solo tiene "
        "permisos de SELECT e INSERT.",
        {
            "id": ID_BASE,
            "admin_id": "Administrador que actuó",
            "accion": "Acción realizada",
            "entidad_tipo": "Tipo de la entidad afectada",
            "entidad_id": "Identificador de la entidad afectada",
            "detalle": "Datos adicionales de la acción, en JSON",
            "created_at": "Fecha y hora de la acción",
        },
    ),
    "admin.notificaciones": (
        "Avisos a los usuarios: es a la vez la bandeja dentro de la aplicación y la cola de "
        "salida del correo (ADR-000-06). Se escribe en la misma transacción que el hecho que "
        "la origina.",
        {
            "id": ID_APP,
            "destinatario_id": "Usuario destinatario",
            "tipo": "Tipo de aviso",
            "datos": "Datos del aviso, en JSON",
            "creada_at": CREADO,
            "leida_at": "Fecha y hora en que el usuario la leyó",
            "enviada_email_at": "Fecha y hora del envío por correo",
            "intentos_email": "Intentos de envío por correo",
            "proximo_intento_email_at": "Momento del próximo intento (espera de 5, 15 y 60 minutos)",
            "email_descartado_at": "Se descartó el correo: intentos agotados o destinatario sin correo",
        },
    ),
    "admin.nps_respuestas": (
        "Respuesta a la pregunta \\gls{nps} de intención (indicador I-04), una por usuario.",
        {
            "usuario_id": "Usuario que respondió",
            "puntaje": "Puntaje de 0 a 10",
            "created_at": "Fecha y hora de la respuesta",
        },
    ),
    # ---------------------------------------------------------------- seguridad
    "seguridad.denuncias": (
        "Denuncia de un usuario contra otro. El denunciado tiene 48 horas para el descargo y "
        "moderación tiene 5 días hábiles más para resolver.",
        {
            "id": ID_BASE,
            "denunciante_id": "Usuario que denuncia",
            "denunciado_id": "Usuario denunciado",
            "sesion_id": "Sesión en la que ocurrió el hecho, si la hay",
            "motivo": "Motivo codificado de la denuncia",
            "evidencia_url": "Referencia a la evidencia adjunta, si la hay",
            "estado": "Estado de la denuncia",
            "descargo_texto": "Último descargo del denunciado (hasta 300 caracteres)",
            "descargo_recibido_at": "Fecha y hora del último descargo",
            "descargo_vence_at": "Fin del plazo de descargo: 48 horas desde que entra en revisión",
            "sla_resolucion_vence_at": "Fin del plazo de resolución: 5 días hábiles desde el vencimiento del descargo",
            "prioridad_alta": "La marcó el trabajo de plazos por vencer; no se resuelve sola",
            "admin_resolutor_id": "Usuario administrador que resolvió",
            "resuelta_at": "Fecha y hora de la resolución",
            "created_at": CREADO,
            "descargo_historial": "Todos los descargos con su fecha, para el administrador",
        },
    ),
    "seguridad.sanciones": (
        "Sanción aplicada a un usuario. Se origina en exactamente una denuncia o una alerta "
        "del kill-switch.",
        {
            "id": ID_BASE,
            "usuario_sancionado_id": "Usuario sancionado",
            "origen": "DENUNCIA o ALERTA\\_SEGURIDAD",
            "denuncia_id": "Denuncia de origen; presente solo si el origen es DENUNCIA",
            "alerta_id": "Alerta de origen; presente solo si el origen es ALERTA\\_SEGURIDAD",
            "tipo": "Tipo de sanción",
            "dias_suspension": "Días de suspensión (7, 15 o 30); solo en la suspensión temporal",
            "vigente_desde": "Inicio de la sanción",
            "vigente_hasta": "Fin de la sanción; nulo en la suspensión definitiva y el baneo",
            "admin_id": "Usuario administrador que la aplicó",
            "created_at": CREADO,
        },
    ),
}

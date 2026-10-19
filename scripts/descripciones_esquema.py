"""Descripciones en castellano de los esquemas, tablas y columnas de la base de Tinku.

Las usa scripts/diccionario_datos.py. Cada descripción se apoya en los comentarios de
las migraciones Flyway (backend/src/main/resources/db/migration), en las
especificaciones docs/specs/Spec_M*.md y en la documentación (Javadoc) de las
entidades JPA del repositorio del sistema. Entre acentos graves (`así`) va texto que
se imprime en monoespaciado. Si una migración nueva agrega una tabla o columna, el
generador se detiene hasta que se agregue aquí su descripción.
"""

ESQUEMAS = {
    "identidad": "Módulo M1, identidad y perfiles: cuentas, vínculo menor--adulto responsable, "
                 "autorizaciones, credenciales académicas, certificado de antecedentes penales "
                 "(CAP), consentimientos y controles de reintento.",
    "matching": "Módulo M2, motor de matching semántico: catálogo de trayectos y temas con sus "
                "embeddings, perfil de matching del tutor, búsquedas guardadas, temas "
                "sugeridos e instrumentación de la evaluación.",
    "aula": "Módulo M3, aula virtual: sesión de aprendizaje de cada reserva y kill-switch "
            "(alertas de seguridad y confirmaciones).",
    "reservas": "Módulo M4, reservas y agenda: franjas de disponibilidad, solicitudes de menores, "
                "reservas, paquetes mensuales, pedidos previos, notas de clase y pedidos de "
                "reprogramación.",
    "pagos": "Módulo M5, motor de pagos: transacciones y retención, tarifas, preferencias y "
             "cuentas de MercadoPago, estado de la pasarela y precios de referencia.",
    "resumen": "Módulo M6, resumen automático de la sesión.",
    "reputacion": "Módulo M7, calificaciones y reputación.",
    "admin": "Módulo M8, panel de administración: administradores, auditoría, soporte, "
             "notificaciones y NPS.",
    "seguridad": "Módulo M9, denuncias, seguridad y moderación: denuncias y sanciones.",
}

TABLAS = {
    # identidad
    "identidad.usuarios": "cuenta de cada persona registrada (adulto, menor o tutor)",
    "identidad.credenciales_academicas": "credencial académica que carga el tutor y su revisión",
    "identidad.autorizaciones_tutor": "tutores que un adulto responsable autorizó para cada menor",
    "identidad.consentimientos_menor": "consentimiento del adulto responsable para el tratamiento "
                                       "de datos del menor, separado de los Términos",
    "identidad.intentos_ocr": "fotos de DNI ilegibles por DNI declarado y espera entre ciclos",
    "identidad.intentos_credencial": "ciclos de carga de credencial agotados por tutor, para "
                                     "escalar la espera",
    "identidad.certificados_antecedentes_penales": "certificado de antecedentes penales (CAP) del "
                                                   "tutor, su revisión y la verificación de la firma",
    "identidad.tokens_reset_password": "tokens de un solo uso para recuperar la contraseña",
    "identidad.aceptaciones_clausula": "quién aceptó qué versión de cada cláusula y cuándo",
    "identidad.especialidades_tutor": "especialidades del tutor: materia y nivel máximo",
    "identidad.credencial_especialidades": "especialidades que cubre una credencial aprobada",
    # matching
    "matching.materias_niveles": "catálogo original de materias por nivel (V7)",
    "matching.perfiles_tutor_matching": "datos del tutor para el matching",
    "matching.busquedas_guardadas": "búsquedas guardadas, que se vuelven a ejecutar",
    "matching.trayectos": "trayectos del catálogo: nivel, curso o carrera y materia",
    "matching.temas": "temas del catálogo, unidad del matching, con su embedding",
    "matching.temas_sugeridos": "contador de temas buscados que el catálogo no cubre",
    "matching.evaluacion_busquedas": "tutores mostrados en cada búsqueda (evaluación)",
    "matching.evaluacion_aceptaciones": "tutores sugeridos cuyo perfil se abrió o que se "
                                        "reservaron (evaluación)",
    # aula
    "aula.sesiones_aprendizaje": "sesión de aula de cada reserva",
    "aula.alertas_seguridad": "alertas del kill-switch",
    "aula.confirmaciones_killswitch": "confirmación de la contraparte en la rama de adultos del "
                                      "kill-switch",
    # reservas
    "reservas.franjas_disponibilidad": "franjas de disponibilidad del tutor",
    "reservas.solicitudes_sesion": "pedidos de clase de un menor",
    "reservas.reservas": "clases reservadas",
    "reservas.paquetes": "paquetes mensuales de clases",
    "reservas.pedidos_previos": "pedido previo del pagador al tutor",
    "reservas.notas_clase": "nota del tutor al adulto responsable",
    "reservas.pedidos_reprogramacion": "pedidos de reprogramación del tutor",
    # pagos
    "pagos.transacciones": "cobro de cada reserva y estado de la retención",
    "pagos.precios_referencia_regional": "precio de referencia por provincia, versionado",
    "pagos.tarifas_tutor": "tarifa vigente del tutor y configuración del paquete",
    "pagos.pasarela_estado": "estado global de la pasarela de pagos (fila única)",
    "pagos.preferencias_pago": "preferencias de MercadoPago generadas por reserva",
    "pagos.cuentas_mp_tutor": "cuenta de MercadoPago conectada por cada tutor",
    "pagos.oauth_estados": "estado transitorio del flujo OAuth con MercadoPago",
    # resumen
    "resumen.resumenes_sesion": "resumen automático de cada sesión",
    # reputacion
    "reputacion.calificaciones": "calificaciones bidireccionales por sesión",
    "reputacion.senales_implicitas_tutor": "señales implícitas agregadas por tutor",
    # admin
    "admin.admins": "personal interno con rol de administración",
    "admin.mapeo_origen_rol": "rol que atiende cada origen de ticket de soporte",
    "admin.tickets_soporte": "pedidos de contacto con soporte",
    "admin.log_auditoria_admin": "registro de auditoría de acciones administrativas (solo inserción)",
    "admin.notificaciones": "bandeja de avisos y cola de envío por correo",
    "admin.nps_respuestas": "respuestas de NPS de intención (evaluación)",
    # seguridad
    "seguridad.denuncias": "denuncias estándar entre usuarios",
    "seguridad.sanciones": "sanciones aplicadas a usuarios",
}

_ID = "Identificador de la fila (UUID)."
_CREADO = "Fecha y hora de creación."
_ACTUALIZADO = "Fecha y hora de la última modificación."

COLUMNAS = {
    # ------------------------------------------------------------- identidad
    "identidad.usuarios.id": "Identificador de la cuenta (UUID).",
    "identidad.usuarios.dni": "DNI de la persona; único.",
    "identidad.usuarios.nombre": "Nombre.",
    "identidad.usuarios.apellido": "Apellido.",
    "identidad.usuarios.fecha_nacimiento": "Fecha de nacimiento.",
    "identidad.usuarios.tipo": "Tipo de cuenta: `ADULTO`, `MENOR` o `TUTOR`.",
    "identidad.usuarios.capacidad_estudiante": "El adulto toma clases como estudiante. Un "
        "`ADULTO` tiene al menos una de las dos capacidades.",
    "identidad.usuarios.capacidad_adulto_responsable": "El adulto es adulto responsable de uno o "
        "más menores.",
    "identidad.usuarios.adulto_responsable_id": "Adulto responsable del menor; obligatorio si y "
        "solo si el tipo es `MENOR`.",
    "identidad.usuarios.password_hash": "Hash de la contraseña.",
    "identidad.usuarios.estado_cuenta": "`ACTIVA`, `SUSPENDIDA` o `BAJA`; la baja anonimiza la "
        "cuenta en lugar de borrarla (ADR-M1-05).",
    "identidad.usuarios.created_at": "Fecha y hora del alta.",
    "identidad.usuarios.activo_para_matching": "El tutor aparece en el matching; lo apagan el "
        "vencimiento del CAP y las suspensiones (M9).",
    "identidad.usuarios.email": "Correo de contacto; único entre los no nulos.",
    "identidad.usuarios.bio": "Presentación del perfil público del tutor (hasta 500 caracteres).",
    "identidad.usuarios.foto_ref": "Referencia interna de la foto del perfil del tutor (no es una "
        "URL pública).",
    "identidad.usuarios.credentials_version": "Versión de credenciales: cambia al cambiar la "
        "contraseña e invalida los JWT emitidos antes.",
    "identidad.usuarios.acepta_menores": "Preferencia del tutor de dar clases a menores; el "
        "requisito sigue siendo el CAP vigente.",

    "identidad.credenciales_academicas.id": _ID,
    "identidad.credenciales_academicas.tutor_id": "Tutor que cargó la credencial.",
    "identidad.credenciales_academicas.tipo_documento": "Tipo de documento: los originales "
        "(`TITULO`, `CERTIFICADO_ANALITICO`, `MATRICULA`) y los de V56 (`SECUNDARIO`, "
        "`PROFESORADO`, `UNIVERSITARIO`, etc.).",
    "identidad.credenciales_academicas.archivo_url": "Referencia al archivo subido.",
    "identidad.credenciales_academicas.estado": "`PENDIENTE`, `APROBADO` o `RECHAZADO`.",
    "identidad.credenciales_academicas.numero_intento": "Intento dentro del ciclo actual (1 a 3).",
    "identidad.credenciales_academicas.ciclo_espera_hasta": "Mientras esté en el futuro, el tutor "
        "no puede subir otra credencial (FR-ID-012).",
    "identidad.credenciales_academicas.admin_revisor_id": "Administrador que la aprobó o rechazó "
        "(sin clave foránea).",
    "identidad.credenciales_academicas.created_at": "Fecha y hora de la carga.",
    "identidad.credenciales_academicas.revisado_at": "Fecha y hora de la revisión.",
    "identidad.credenciales_academicas.institucion": "Institución que emitió el título.",
    "identidad.credenciales_academicas.denominacion": "Denominación del título.",
    "identidad.credenciales_academicas.anio_egreso": "Año de egreso (1900 a 2100).",
    "identidad.credenciales_academicas.es_digital": "El documento es digital.",
    "identidad.credenciales_academicas.enlace_verificacion": "Enlace de verificación del documento.",
    "identidad.credenciales_academicas.nombre_coincide": "Resultado del OCR contra el nombre del "
        "DNI: nulo, no se pudo comparar; falso, no coincide (marca para el administrador).",
    "identidad.credenciales_academicas.metodo_verificacion": "`REGISTRO_OFICIAL` o "
        "`SOLO_DOCUMENTO`.",
    "identidad.credenciales_academicas.motivo_rechazo": "Motivo codificado del rechazo.",
    "identidad.credenciales_academicas.detalle_rechazo": "Detalle libre del rechazo.",

    "identidad.autorizaciones_tutor.id": _ID,
    "identidad.autorizaciones_tutor.adulto_responsable_id": "Adulto responsable que autoriza.",
    "identidad.autorizaciones_tutor.menor_id": "Menor para el que se autoriza al tutor.",
    "identidad.autorizaciones_tutor.tutor_id": "Tutor autorizado.",
    "identidad.autorizaciones_tutor.no_confiable": "Filtro privado del adulto responsable: el "
        "tutor deja de aparecerle en el matching, sin efecto en la reputación (FR-ID-009).",
    "identidad.autorizaciones_tutor.created_at": _CREADO,

    "identidad.consentimientos_menor.id": _ID,
    "identidad.consentimientos_menor.menor_id": "Menor al que se refiere el consentimiento.",
    "identidad.consentimientos_menor.adulto_responsable_id": "Adulto responsable que lo otorga.",
    "identidad.consentimientos_menor.version_texto": "Versión del texto aceptado.",
    "identidad.consentimientos_menor.aceptado_at": "Fecha y hora de la aceptación.",
    "identidad.consentimientos_menor.revocado_at": "Fecha y hora de la revocación; nulo si está "
        "vigente.",

    "identidad.intentos_ocr.dni": "DNI declarado por quien intenta registrarse.",
    "identidad.intentos_ocr.intentos_consumidos": "Fotos ilegibles en el ciclo actual; el tope lo "
        "fija la aplicación (V52).",
    "identidad.intentos_ocr.proximo_intento_permitido": "Hasta cuándo debe esperar antes de un "
        "nuevo ciclo; se compara al leer, sin trabajo programado.",
    "identidad.intentos_ocr.updated_at": _ACTUALIZADO,

    "identidad.intentos_credencial.tutor_id": "Tutor.",
    "identidad.intentos_credencial.veces_ciclo_agotado": "Veces que agotó el ciclo de reintentos; "
        "la espera se duplica en cada ciclo (24, 48, 96 h...).",
    "identidad.intentos_credencial.proximo_intento_permitido": "Hasta cuándo debe esperar antes del "
        "próximo ciclo.",
    "identidad.intentos_credencial.updated_at": _ACTUALIZADO,

    "identidad.certificados_antecedentes_penales.id": _ID,
    "identidad.certificados_antecedentes_penales.tutor_id": "Tutor titular del certificado.",
    "identidad.certificados_antecedentes_penales.archivo_url": "Referencia al archivo subido.",
    "identidad.certificados_antecedentes_penales.fecha_emision": "Fecha de emisión.",
    "identidad.certificados_antecedentes_penales.vence_at": "Fecha de vencimiento.",
    "identidad.certificados_antecedentes_penales.estado": "`PENDIENTE`, `APROBADO`, `RECHAZADO`, "
        "`EN_REVISION_LEGAL` (nunca se resuelve sola) o `VENCIDO`.",
    "identidad.certificados_antecedentes_penales.tiene_antecedentes": "El certificado registra "
        "antecedentes.",
    "identidad.certificados_antecedentes_penales.categoria_antecedente": "Categoría del antecedente "
        "registrado.",
    "identidad.certificados_antecedentes_penales.numero_intento": "Intento dentro del ciclo actual "
        "(1 a 3).",
    "identidad.certificados_antecedentes_penales.ciclo_espera_hasta": "Mientras esté en el futuro, "
        "el tutor no puede subir otro certificado.",
    "identidad.certificados_antecedentes_penales.admin_revisor_id": "Administrador que lo revisó "
        "(sin clave foránea).",
    "identidad.certificados_antecedentes_penales.created_at": "Fecha y hora de la carga.",
    "identidad.certificados_antecedentes_penales.revisado_at": "Fecha y hora de la revisión.",
    "identidad.certificados_antecedentes_penales.firma_estado": "Verificación de la firma digital "
        "con el validador oficial: `NO_VERIFICADA`, `PENDIENTE`, `EN_PROCESO`, `VALIDA`, "
        "`INVALIDA`, `FIRMANTE_NO_RECONOCIDO` o `ERROR`.",
    "identidad.certificados_antecedentes_penales.firma_detalle": "Detalle corto del resultado.",
    "identidad.certificados_antecedentes_penales.firma_firmante": "Firmante que informa el "
        "validador.",
    "identidad.certificados_antecedentes_penales.firma_sha256": "Hash del archivo enviado; el "
        "resultado vale solo si el validador informa el mismo.",
    "identidad.certificados_antecedentes_penales.firma_solicitud_id": "Identificador del pedido "
        "ante el validador.",
    "identidad.certificados_antecedentes_penales.firma_intentos": "Intentos de verificación.",
    "identidad.certificados_antecedentes_penales.firma_proximo_intento_at": "Próximo envío "
        "programado en la cola.",
    "identidad.certificados_antecedentes_penales.firma_enviada_at": "Envío al validador.",
    "identidad.certificados_antecedentes_penales.firma_verificada_at": "Recepción del resultado.",

    "identidad.tokens_reset_password.id": _ID,
    "identidad.tokens_reset_password.usuario_id": "Usuario que pidió la recuperación.",
    "identidad.tokens_reset_password.token_hash": "SHA-256 del token (64 caracteres "
        "hexadecimales); el token no se guarda.",
    "identidad.tokens_reset_password.expira_en": "Vencimiento del token.",
    "identidad.tokens_reset_password.usado_en": "Uso del token; nulo si no se usó.",
    "identidad.tokens_reset_password.created_at": _CREADO,

    "identidad.aceptaciones_clausula.id": _ID,
    "identidad.aceptaciones_clausula.usuario_id": "Usuario que aceptó.",
    "identidad.aceptaciones_clausula.clausula": "Cláusula aceptada (por ejemplo, "
        "`TERMINOS_Y_CONDICIONES` o `GRABACION_AUDIO_RESUMEN`).",
    "identidad.aceptaciones_clausula.version": "Versión aceptada de la cláusula.",
    "identidad.aceptaciones_clausula.aceptada_at": "Fecha y hora de la aceptación.",

    "identidad.especialidades_tutor.id": _ID,
    "identidad.especialidades_tutor.tutor_id": "Tutor (de 1 a 3 especialidades, control del "
        "servicio).",
    "identidad.especialidades_tutor.materia": "Materia del catálogo de temas.",
    "identidad.especialidades_tutor.nivel_maximo": "Nivel máximo que puede enseñar: `PRIMARIO`, "
        "`SECUNDARIO` o `UNIVERSITARIO`.",
    "identidad.especialidades_tutor.created_at": _CREADO,

    "identidad.credencial_especialidades.credencial_id": "Credencial aprobada.",
    "identidad.credencial_especialidades.especialidad_id": "Especialidad que cubre; se borra con "
        "la especialidad.",

    # -------------------------------------------------------------- matching
    "matching.materias_niveles.id": _ID,
    "matching.materias_niveles.nivel": "`primario`, `secundario` o `universitario`.",
    "matching.materias_niveles.materia": "Nombre de la materia.",

    "matching.perfiles_tutor_matching.tutor_id": "Tutor.",
    "matching.perfiles_tutor_matching.materias_niveles_ids": "Materias del catálogo de V7; "
        "reemplazadas por `tema_ids` (V19).",
    "matching.perfiles_tutor_matching.embedding": "Embedding del perfil (384 dimensiones); desde "
        "V42 el puntaje usa el embedding de cada tema.",
    "matching.perfiles_tutor_matching.activo_para_matching": "Indicador creado en V7; el que se "
        "consulta es `identidad.usuarios.activo_para_matching`.",
    "matching.perfiles_tutor_matching.tema_ids": "Temas del catálogo elegidos por el tutor "
        "(índice GIN).",

    "matching.busquedas_guardadas.id": _ID,
    "matching.busquedas_guardadas.usuario_id": "Usuario que guardó la búsqueda.",
    "matching.busquedas_guardadas.texto_busqueda": "Texto de la búsqueda.",
    "matching.busquedas_guardadas.created_at": _CREADO,
    "matching.busquedas_guardadas.filtros": "Filtros guardados (nivel, materia, nombre, precio "
        "máximo).",
    "matching.busquedas_guardadas.huella": "Huella del texto normalizado y los filtros; evita "
        "duplicados por usuario.",

    "matching.trayectos.id": _ID,
    "matching.trayectos.nivel": "`primario`, `secundario` o `universitario`.",
    "matching.trayectos.anio_o_carrera": "Curso o año (por ejemplo, «4°») o carrera.",
    "matching.trayectos.materia": "Materia.",

    "matching.temas.id": _ID,
    "matching.temas.trayecto_id": "Trayecto al que pertenece.",
    "matching.temas.nombre": "Nombre del tema.",
    "matching.temas.descripcion": "Qué contenidos abarca; es la fuente del embedding.",
    "matching.temas.orden": "Orden dentro del trayecto.",
    "matching.temas.embedding": "Embedding del tema (384 dimensiones, V42).",
    "matching.temas.embedding_fuente": "Texto con el que se calculó el embedding; si cambia, se "
        "recalcula.",

    "matching.temas_sugeridos.id": _ID,
    "matching.temas_sugeridos.texto": "Texto buscado, normalizado; sin datos de quién buscó.",
    "matching.temas_sugeridos.veces": "Cantidad de veces que se buscó.",
    "matching.temas_sugeridos.nivel": "Nivel del tema del catálogo más parecido.",
    "matching.temas_sugeridos.materia": "Materia del tema del catálogo más parecido.",
    "matching.temas_sugeridos.ultima_vez": "Última búsqueda.",

    "matching.evaluacion_busquedas.id": _ID,
    "matching.evaluacion_busquedas.usuario_id": "Usuario que buscó (nunca una cuenta menor).",
    "matching.evaluacion_busquedas.longitud_texto": "Longitud del texto buscado; el texto no se "
        "guarda.",
    "matching.evaluacion_busquedas.cantidad_resultados": "Cantidad de tutores devueltos.",
    "matching.evaluacion_busquedas.tutor_ids": "Tutores mostrados, en orden.",
    "matching.evaluacion_busquedas.created_at": _CREADO,

    "matching.evaluacion_aceptaciones.id": _ID,
    "matching.evaluacion_aceptaciones.busqueda_id": "Búsqueda evaluada; se borra con ella.",
    "matching.evaluacion_aceptaciones.tutor_id": "Tutor elegido.",
    "matching.evaluacion_aceptaciones.posicion": "Posición del tutor en la lista (1 = primero), "
        "calculada por el servidor.",
    "matching.evaluacion_aceptaciones.tipo": "`PERFIL` (se abrió) o `RESERVA` (se reservó).",
    "matching.evaluacion_aceptaciones.created_at": _CREADO,

    # ------------------------------------------------------------------ aula
    "aula.sesiones_aprendizaje.id": _ID,
    "aula.sesiones_aprendizaje.reserva_id": "Reserva de la sesión (relación 1 a 1).",
    "aula.sesiones_aprendizaje.livekit_room_id": "Sala de LiveKit; nula hasta 5 min antes del "
        "inicio (creación diferida).",
    "aula.sesiones_aprendizaje.estado": "`no_iniciada`, `en_curso`, `finalizada`, "
        "`finalizada_anticipada` o `interrumpida`.",
    "aula.sesiones_aprendizaje.inicio_real": "Inicio efectivo.",
    "aula.sesiones_aprendizaje.fin_real": "Fin efectivo.",
    "aula.sesiones_aprendizaje.duracion_efectiva_segundos": "Duración efectiva, calculada al "
        "finalizar; M6 usa el umbral de 10 min.",
    "aula.sesiones_aprendizaje.created_at": _CREADO,
    "aula.sesiones_aprendizaje.updated_at": _ACTUALIZADO,
    "aula.sesiones_aprendizaje.estudiante_joined_at": "Primer ingreso del estudiante (webhook de "
        "LiveKit).",
    "aula.sesiones_aprendizaje.tutor_joined_at": "Primer ingreso del tutor (webhook de LiveKit).",
    "aula.sesiones_aprendizaje.duracion_agendada_segundos": "Duración agendada, congelada al "
        "programar; base de la regla del 50 %.",
    "aula.sesiones_aprendizaje.tutor_conectado": "El tutor está conectado.",
    "aula.sesiones_aprendizaje.estudiante_conectado": "El estudiante está conectado.",
    "aula.sesiones_aprendizaje.par_roto_at": "Desde cuándo falta alguno de los dos; nulo si están "
        "ambos o la clase no empezó.",
    "aula.sesiones_aprendizaje.audio_referencia": "Referencia interna del audio grabado (solo con "
        "el adicional de resumen).",
    "aula.sesiones_aprendizaje.audio_recibido_at": "Recepción del audio.",
    "aula.sesiones_aprendizaje.audio_borrado_at": "Borrado del audio.",

    "aula.alertas_seguridad.id": _ID,
    "aula.alertas_seguridad.sesion_id": "Sesión en la que se activó el kill-switch.",
    "aula.alertas_seguridad.rama": "`menor` o `adultos`; la decide el backend con datos de M1.",
    "aula.alertas_seguridad.detectado_id": "Usuario señalado por la alerta.",
    "aula.alertas_seguridad.clip_url": "Clip de evidencia; se completa al subirlo.",
    "aula.alertas_seguridad.clip_retencion_hasta": "Fin de la retención del clip: 30 días desde la "
        "resolución.",
    "aula.alertas_seguridad.estado": "`pendiente_revision`, `resuelta_reactivacion` o "
        "`resuelta_baja`.",
    "aula.alertas_seguridad.created_at": _CREADO,
    "aula.alertas_seguridad.descargo_texto": "Descargo del tutor (hasta 300 caracteres); no "
        "bloquea la resolución.",
    "aula.alertas_seguridad.descargo_recibido_at": "Recepción del descargo.",

    "aula.confirmaciones_killswitch.id": _ID,
    "aula.confirmaciones_killswitch.sesion_id": "Sesión (una confirmación por sesión).",
    "aula.confirmaciones_killswitch.detectado_id": "Usuario señalado.",
    "aula.confirmaciones_killswitch.respondido_id": "Participante que respondió; nulo mientras se "
        "espera (sin clave foránea).",
    "aula.confirmaciones_killswitch.vio": "Respuesta: si vio contenido inapropiado; nula hasta "
        "que responda.",
    "aula.confirmaciones_killswitch.created_at": _CREADO,
    "aula.confirmaciones_killswitch.responded_at": "Fecha y hora de la respuesta.",
    "aula.confirmaciones_killswitch.vence_at": "Plazo de respuesta; sin respuesta cuenta como "
        "«No».",
    "aula.confirmaciones_killswitch.vencida": "Venció sin respuesta.",

    # -------------------------------------------------------------- reservas
    "reservas.franjas_disponibilidad.id": _ID,
    "reservas.franjas_disponibilidad.tutor_id": "Tutor que publica la franja.",
    "reservas.franjas_disponibilidad.dia_semana": "Día de la semana (0 = domingo a 6 = sábado), "
        "en franjas semanales.",
    "reservas.franjas_disponibilidad.fecha_especifica": "Fecha, en franjas puntuales.",
    "reservas.franjas_disponibilidad.hora_inicio": "Hora de inicio.",
    "reservas.franjas_disponibilidad.hora_fin": "Hora de fin, posterior al inicio.",
    "reservas.franjas_disponibilidad.activa": "La franja está publicada.",

    "reservas.solicitudes_sesion.id": _ID,
    "reservas.solicitudes_sesion.menor_id": "Menor que pide la clase.",
    "reservas.solicitudes_sesion.tutor_id": "Tutor pedido.",
    "reservas.solicitudes_sesion.horario_propuesto": "Horario propuesto.",
    "reservas.solicitudes_sesion.estado": "`pendiente`, `convertida`, `expirada` o `rechazada`.",
    "reservas.solicitudes_sesion.created_at": _CREADO,
    "reservas.solicitudes_sesion.expira_at": "Vencimiento (creación + 48 h); no bloquea horario "
        "ni genera cobro.",
    "reservas.solicitudes_sesion.duracion_minutos": "Duración pedida (30 a 180 min, múltiplo "
        "de 30).",

    "reservas.reservas.id": _ID,
    "reservas.reservas.pagador_id": "Quien paga: estudiante adulto o adulto responsable.",
    "reservas.reservas.beneficiario_id": "Quien toma la clase.",
    "reservas.reservas.tutor_id": "Tutor; distinto del pagador y del beneficiario.",
    "reservas.reservas.solicitud_origen_id": "Solicitud del menor que originó la reserva, si la "
        "hay.",
    "reservas.reservas.horario": "Inicio de la clase.",
    "reservas.reservas.precio": "Precio congelado al crear la reserva.",
    "reservas.reservas.estado": "`pendiente_pago`, `confirmada`, `en_curso`, `finalizada`, "
        "`cancelada`, `no_show_estudiante`, `no_show_tutor` o `no_show_doble`.",
    "reservas.reservas.motivo_cancelacion": "Solo si está cancelada: `voluntaria`, "
        "`timeout_pago`, `revocacion_autorizacion`, `sancion` o `cap_vencido`.",
    "reservas.reservas.created_at": _CREADO,
    "reservas.reservas.duracion_minutos": "Duración (30 a 180 min, múltiplo de 30).",
    "reservas.reservas.horario_fin": "Fin de la clase (inicio + duración); sostiene la exclusión "
        "por rango.",
    "reservas.reservas.resumen_contratado": "Se contrató el adicional de resumen.",
    "reservas.reservas.precio_adicional_resumen": "Precio congelado del adicional; presente si y "
        "solo si se contrató.",
    "reservas.reservas.paquete_id": "Paquete mensual al que pertenece, si corresponde.",

    "reservas.paquetes.id": _ID,
    "reservas.paquetes.pagador_id": "Quien paga.",
    "reservas.paquetes.beneficiario_id": "Quien toma las clases.",
    "reservas.paquetes.tutor_id": "Tutor.",
    "reservas.paquetes.reserva_ancla_id": "Primera reserva del paquete, que ancla el pago.",
    "reservas.paquetes.cantidad_clases": "Cantidad de clases (cuatro semanales).",
    "reservas.paquetes.duracion_minutos": "Duración de cada clase.",
    "reservas.paquetes.descuento_porcentaje": "Descuento aplicado (0 a 30 %).",
    "reservas.paquetes.precio_total": "Precio total del paquete.",
    "reservas.paquetes.estado": "`pendiente_pago`, `confirmado` o `cancelado`.",
    "reservas.paquetes.vigente_hasta": "Fin de la vigencia del paquete.",
    "reservas.paquetes.created_at": _CREADO,

    "reservas.pedidos_previos.reserva_id": "Reserva (un pedido por reserva).",
    "reservas.pedidos_previos.texto": "Texto del pedido, hasta 1000 caracteres; lo carga el "
        "pagador antes del inicio.",
    "reservas.pedidos_previos.created_at": _CREADO,
    "reservas.pedidos_previos.updated_at": _ACTUALIZADO,

    "reservas.notas_clase.reserva_id": "Reserva finalizada con beneficiario menor (una nota por "
        "reserva).",
    "reservas.notas_clase.texto": "Texto de la nota, hasta 1000 caracteres; la ven el adulto "
        "responsable y el tutor.",
    "reservas.notas_clase.created_at": _CREADO,
    "reservas.notas_clase.updated_at": _ACTUALIZADO,

    "reservas.pedidos_reprogramacion.id": _ID,
    "reservas.pedidos_reprogramacion.reserva_id": "Reserva a reprogramar; un solo pedido pendiente "
        "por reserva.",
    "reservas.pedidos_reprogramacion.horario_original": "Horario vigente al pedir.",
    "reservas.pedidos_reprogramacion.horario_propuesto": "Horario propuesto por el tutor.",
    "reservas.pedidos_reprogramacion.motivo": "Motivo informado (hasta 300 caracteres).",
    "reservas.pedidos_reprogramacion.estado": "`pendiente`, `aceptado`, `rechazado`, `vencido` o "
        "`retirado`.",
    "reservas.pedidos_reprogramacion.created_at": _CREADO,
    "reservas.pedidos_reprogramacion.resuelto_at": "Fecha y hora de la resolución.",

    # ----------------------------------------------------------------- pagos
    "pagos.transacciones.id": _ID,
    "pagos.transacciones.reserva_id": "Reserva cobrada (una transacción por reserva).",
    "pagos.transacciones.mp_payment_id": "Identificador del pago en MercadoPago; único.",
    "pagos.transacciones.monto_bruto": "Monto cobrado.",
    "pagos.transacciones.comision_plataforma": "Comisión de la plataforma (no mayor que el monto "
        "bruto).",
    "pagos.transacciones.estado": "`retenido_escrow`, `liberado`, `reembolsado`, "
        "`pausado_denuncia` o `pausado_alerta`.",
    "pagos.transacciones.liberar_at": "Fin de la sesión + 24 h; nulo hasta que la sesión termine.",
    "pagos.transacciones.intentos_liberacion": "Fallos del trabajo de liberación.",
    "pagos.transacciones.created_at": _CREADO,
    "pagos.transacciones.en_bypass": "Nació en modo bypass: no hay dinero real en MercadoPago.",
    "pagos.transacciones.monto_adicional_resumen": "Monto del adicional de resumen, íntegro para la "
        "plataforma.",
    "pagos.transacciones.adicional_reembolsado_at": "Reembolso del adicional.",
    "pagos.transacciones.adicional_reembolso_estado": "`PENDIENTE`, `FALLIDO`, `HECHO` o "
        "`RESUELTO_MANUAL`.",
    "pagos.transacciones.adicional_reembolso_intentos": "Intentos del reembolso del adicional.",
    "pagos.transacciones.adicional_reembolso_error": "Último error del reembolso del adicional.",
    "pagos.transacciones.adicional_reembolso_nota": "Constancia de Soporte Financiero al "
        "resolverlo manualmente.",
    "pagos.transacciones.reembolso_parcial_monto": "Monto del reembolso parcial manual (uno por "
        "transacción).",
    "pagos.transacciones.reembolso_parcial_at": "Fecha y hora del reembolso parcial.",

    "pagos.precios_referencia_regional.provincia": "Provincia.",
    "pagos.precios_referencia_regional.version": "Versión del precio (desde 1); la vigente es la "
        "mayor.",
    "pagos.precios_referencia_regional.valor_sugerido": "Precio de referencia sugerido.",
    "pagos.precios_referencia_regional.vigente_desde": "Inicio de la vigencia.",

    "pagos.tarifas_tutor.tutor_id": "Tutor (una tarifa vigente por tutor).",
    "pagos.tarifas_tutor.precio_hora": "Precio por hora (V31; antes, por sesión).",
    "pagos.tarifas_tutor.updated_at": _ACTUALIZADO,
    "pagos.tarifas_tutor.paquete_habilitado": "El tutor ofrece el paquete mensual.",
    "pagos.tarifas_tutor.paquete_descuento_porcentaje": "Descuento del paquete (0 a 30 %).",

    "pagos.pasarela_estado.id": "Siempre 1 (fila única).",
    "pagos.pasarela_estado.habilitada": "Verdadero: cobro real por MercadoPago; falso: modo "
        "bypass.",
    "pagos.pasarela_estado.updated_at": _ACTUALIZADO,
    "pagos.pasarela_estado.updated_by": "Usuario administrador que hizo el último cambio.",

    "pagos.preferencias_pago.reserva_id": "Reserva para la que se generó la preferencia.",
    "pagos.preferencias_pago.preference_id": "Identificador de la preferencia en MercadoPago.",
    "pagos.preferencias_pago.created_at": _CREADO,
    "pagos.preferencias_pago.conciliado_at": "Momento en que la reserva ya tiene su transacción.",
    "pagos.preferencias_pago.intentos_conciliacion": "Intentos del barrido de conciliación.",
    "pagos.preferencias_pago.alertado_at": "Aviso a Soporte por un pago aprobado que no se pudo "
        "atribuir.",

    "pagos.cuentas_mp_tutor.tutor_id": "Tutor.",
    "pagos.cuentas_mp_tutor.mp_user_id": "Usuario de MercadoPago; único entre las cuentas "
        "conectadas.",
    "pagos.cuentas_mp_tutor.access_token_cifrado": "Token de acceso cifrado (AES-256-GCM, clave "
        "fuera de la base).",
    "pagos.cuentas_mp_tutor.refresh_token_cifrado": "Token de renovación cifrado.",
    "pagos.cuentas_mp_tutor.public_key": "Clave pública de la cuenta.",
    "pagos.cuentas_mp_tutor.expira_at": "Vencimiento del token de acceso.",
    "pagos.cuentas_mp_tutor.estado": "`CONECTADA`, `REVOCADA` o `ERROR`.",
    "pagos.cuentas_mp_tutor.conectada_at": "Fecha y hora de la conexión.",
    "pagos.cuentas_mp_tutor.updated_at": _ACTUALIZADO,

    "pagos.oauth_estados.state": "Parámetro `state` del flujo (protección CSRF).",
    "pagos.oauth_estados.tutor_id": "Tutor que conecta su cuenta.",
    "pagos.oauth_estados.code_verifier": "Verificador PKCE.",
    "pagos.oauth_estados.expira_at": "Vencimiento (minutos).",

    # --------------------------------------------------------------- resumen
    "resumen.resumenes_sesion.id": _ID,
    "resumen.resumenes_sesion.sesion_id": "Sesión resumida (un resumen por sesión, no "
        "regenerable).",
    "resumen.resumenes_sesion.estado": "`pendiente`, `generado`, `suspendido_seguridad`, "
        "`reintento_agotado` o `fallido`.",
    "resumen.resumenes_sesion.prompt_anonimizado": "Prompt final, ya anonimizado.",
    "resumen.resumenes_sesion.transcript_anonimizado": "Transcripción anonimizada; se guarda "
        "siempre.",
    "resumen.resumenes_sesion.resumen_final": "Salida del modelo de lenguaje; nula hasta generar.",
    "resumen.resumenes_sesion.intentos": "Intentos de generación.",
    "resumen.resumenes_sesion.proximo_reintento_at": "Próximo reintento (espera de 5 min, 15 min "
        "y 1 h).",
    "resumen.resumenes_sesion.recordatorio_pendiente": "Falta el recordatorio único de las 24 h.",
    "resumen.resumenes_sesion.suspendido_seguridad": "Hay una denuncia o alerta activa sobre la "
        "sesión.",
    "resumen.resumenes_sesion.created_at": _CREADO,

    # ------------------------------------------------------------ reputacion
    "reputacion.calificaciones.id": _ID,
    "reputacion.calificaciones.sesion_id": "Sesión calificada.",
    "reputacion.calificaciones.autor_id": "Autor de la calificación.",
    "reputacion.calificaciones.direccion": "`estudiante_a_tutor` o `tutor_a_estudiante`; se "
        "deriva del rol del autor.",
    "reputacion.calificaciones.estrellas": "Puntaje de 1 a 5.",
    "reputacion.calificaciones.comentario": "Comentario; solo en `estudiante_a_tutor`.",
    "reputacion.calificaciones.editable_hasta": "Creación + 48 h.",
    "reputacion.calificaciones.created_at": _CREADO,

    "reputacion.senales_implicitas_tutor.tutor_id": "Tutor.",
    "reputacion.senales_implicitas_tutor.puntualidad_promedio": "Puntualidad promedio (0 a 1).",
    "reputacion.senales_implicitas_tutor.tasa_recontratacion": "Tasa de recontratación.",
    "reputacion.senales_implicitas_tutor.tasa_cancelacion_noshow": "Tasa de cancelaciones y "
        "ausencias.",
    "reputacion.senales_implicitas_tutor.tiempo_respuesta_promedio_min": "Tiempo de respuesta "
        "promedio, en minutos.",
    "reputacion.senales_implicitas_tutor.sesiones_dictadas_total": "Sesiones dictadas en total.",
    "reputacion.senales_implicitas_tutor.updated_at": _ACTUALIZADO,

    # ----------------------------------------------------------------- admin
    "admin.admins.id": _ID,
    "admin.admins.usuario_id": "Cuenta de usuario del administrador (1 a 1).",
    "admin.admins.rol": "`MODERACION_SEGURIDAD` o `SOPORTE_FINANCIERO` (un único rol).",
    "admin.admins.activo": "El administrador está habilitado.",
    "admin.admins.created_at": _CREADO,

    "admin.mapeo_origen_rol.origen_modulo": "Origen del pedido de soporte (por ejemplo, "
        "`M5.pago_fallido`).",
    "admin.mapeo_origen_rol.rol_asignado": "Rol que lo atiende.",

    "admin.tickets_soporte.id": _ID,
    "admin.tickets_soporte.usuario_id": "Usuario que pide soporte.",
    "admin.tickets_soporte.origen_modulo": "Origen del pedido; determina el rol.",
    "admin.tickets_soporte.asunto": "Asunto.",
    "admin.tickets_soporte.detalle": "Detalle del pedido.",
    "admin.tickets_soporte.estado": "`ABIERTO`, `EN_PROCESO`, `RESUELTO` o `CERRADO`.",
    "admin.tickets_soporte.rol_asignado": "Rol al que se enrutó.",
    "admin.tickets_soporte.creado_en": _CREADO,
    "admin.tickets_soporte.resuelto_en": "Fecha y hora de la resolución.",

    "admin.log_auditoria_admin.id": _ID,
    "admin.log_auditoria_admin.admin_id": "Administrador que actuó.",
    "admin.log_auditoria_admin.accion": "Acción realizada.",
    "admin.log_auditoria_admin.entidad_tipo": "Tipo de entidad afectada.",
    "admin.log_auditoria_admin.entidad_id": "Identificador de la entidad afectada.",
    "admin.log_auditoria_admin.detalle": "Detalle de la acción (JSON).",
    "admin.log_auditoria_admin.created_at": _CREADO,

    "admin.notificaciones.id": _ID,
    "admin.notificaciones.destinatario_id": "Usuario destinatario.",
    "admin.notificaciones.tipo": "Tipo de aviso.",
    "admin.notificaciones.datos": "Datos del aviso (JSON).",
    "admin.notificaciones.creada_at": _CREADO,
    "admin.notificaciones.leida_at": "Lectura en la bandeja; nula si no se leyó.",
    "admin.notificaciones.enviada_email_at": "Envío por correo.",
    "admin.notificaciones.intentos_email": "Intentos de envío por correo.",
    "admin.notificaciones.proximo_intento_email_at": "Próximo intento (espera de 5, 15 y 60 min).",
    "admin.notificaciones.email_descartado_at": "Descarte del correo: intentos agotados o "
        "destinatario sin correo.",

    "admin.nps_respuestas.usuario_id": "Usuario que respondió (una respuesta por usuario).",
    "admin.nps_respuestas.puntaje": "Puntaje de 0 a 10.",
    "admin.nps_respuestas.created_at": _CREADO,

    # ------------------------------------------------------------- seguridad
    "seguridad.denuncias.id": _ID,
    "seguridad.denuncias.denunciante_id": "Usuario que denuncia.",
    "seguridad.denuncias.denunciado_id": "Usuario denunciado.",
    "seguridad.denuncias.sesion_id": "Sesión en la que ocurrió, si corresponde.",
    "seguridad.denuncias.motivo": "`COMPORTAMIENTO_INAPROPIADO`, `INCUMPLIMIENTO`, `FRAUDE`, "
        "`CONTENIDO_ILEGAL` o `ACOSO`.",
    "seguridad.denuncias.evidencia_url": "Evidencia opcional.",
    "seguridad.denuncias.estado": "`REGISTRADA`, `EN_REVISION`, `RESUELTA_INFUNDADA`, "
        "`RESUELTA_FUNDADA` o `ESCALADA`.",
    "seguridad.denuncias.descargo_texto": "Último descargo del denunciado (hasta 300 caracteres).",
    "seguridad.denuncias.descargo_recibido_at": "Recepción del descargo.",
    "seguridad.denuncias.descargo_vence_at": "Vencimiento del plazo de descargo (inicio de la "
        "revisión + 48 h).",
    "seguridad.denuncias.sla_resolucion_vence_at": "Vencimiento del plazo de resolución "
        "(vencimiento del descargo + 5 días hábiles).",
    "seguridad.denuncias.prioridad_alta": "Marcada por el trabajo de control del plazo; no se "
        "resuelve sola.",
    "seguridad.denuncias.admin_resolutor_id": "Usuario administrador que la resolvió.",
    "seguridad.denuncias.resuelta_at": "Fecha y hora de la resolución.",
    "seguridad.denuncias.created_at": _CREADO,
    "seguridad.denuncias.descargo_historial": "Todos los descargos con su fecha, para el "
        "administrador.",

    "seguridad.sanciones.id": _ID,
    "seguridad.sanciones.usuario_sancionado_id": "Usuario sancionado.",
    "seguridad.sanciones.origen": "`DENUNCIA` o `ALERTA_SEGURIDAD`; exactamente una de las dos "
        "referencias.",
    "seguridad.sanciones.denuncia_id": "Denuncia que la origina.",
    "seguridad.sanciones.alerta_id": "Alerta de seguridad que la origina.",
    "seguridad.sanciones.tipo": "`ADVERTENCIA`, `SUSPENSION_TEMPORAL`, `SUSPENSION_DEFINITIVA` o "
        "`BANEO_AUTORIDADES`.",
    "seguridad.sanciones.dias_suspension": "7, 15 o 30; solo en la suspensión temporal.",
    "seguridad.sanciones.vigente_desde": "Inicio de la vigencia.",
    "seguridad.sanciones.vigente_hasta": "Fin de la vigencia; nulo en la definitiva y el baneo.",
    "seguridad.sanciones.admin_id": "Usuario administrador que la aplicó.",
    "seguridad.sanciones.created_at": _CREADO,
}

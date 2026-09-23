# Tinku: una plataforma digital de marketplace educativo para conectar estudiantes y tutores académicos a escala nacional

> Autor: Santiago Mercado Carbone
> Año académico: 2026
> Palabras clave: marketplace educativo, tutorías particulares, inteligencia artificial, matching semántico, educación personalizada

## Agradecimientos

*Texto de los agradecimientos.*

## Declaración sobre el uso de IA

En este trabajo se utilizaron herramientas de inteligencia artificial generativa tanto en el desarrollo del sistema como en la elaboración del documento. La tabla~[§tab:herramientas-ia] resume cada herramienta y las tareas que asistió; el método de desarrollo se describe en el capítulo~[§cap:metodologia] (sección~[§sec:desarrollo-ia]).

**Tabla:** Herramientas de IA generativa utilizadas

| **Herramienta** | **Tareas asistidas** |
| --- | --- |
| OpenCode (modelo Big Pickle) | Implementación del código del MVP a partir de la Constitución, las especificaciones, los planes técnicos y la lista de tareas redactados previamente, en las primeras etapas del desarrollo |
| Gemini (Gemini 3.1 Pro) | Consultas esporádicas, como segunda opinión sobre decisiones puntuales |
| ChatGPT (modelo predeterminado) | Consultas esporádicas, como tercera mirada sobre decisiones puntuales |
| Claude Code (Claude Opus 5, Claude Opus 5.5 y Claude Sonnet 5) | Revisión de la consistencia del documento, relevamiento de tarifas y fuentes, recálculo y edición del modelo financiero, y redacción asistida de capítulos y apéndices |

El uso se rigió por los siguientes criterios:

- **Autoría.** La definición del problema, la arquitectura, el alcance, los criterios de evaluación y las decisiones del proyecto son del autor. Las herramientas propusieron alternativas y redacciones; la elección entre ellas fue siempre del autor, y las decisiones de arquitectura se documentaron como registros de decisión validados por él.
- **Verificación.** Toda tarifa, cotización y dato de mercado se confirmó en la fuente original, que se cita en cada caso. Los indicadores financieros se calcularon en la planilla del anexo~[§anx:modelo-financiero] y se replicaron de forma independiente antes de incluirlos en el texto. El código se verificó con las pruebas automatizadas del repositorio y la integración continua.
- **Trazabilidad.** Las instrucciones con las que se desarrolló el sistema están versionadas en el propio repositorio (anexo~[§anx:repositorios]). Los prompts más relevantes de la elaboración del documento se registran en el apéndice~[§apx:prompts].
- **Comprensión.** El autor leyó, revisó y adaptó todo el contenido asistido, y asume la responsabilidad total sobre el contenido de este documento.

## Resumen (español)

Este proyecto nace como una red a lo largo del país, con una posibilidad de expandirse, para conectar el aprendizaje y el conocimiento, elevando la tradición del apoyo escolar en los hogares argentinos y brindándoles nuevas herramientas. La iniciativa busca facilitarle a cualquier estudiante, desde el nivel primario hasta el universitario, encontrar el apoyo académico ideal, permitiendo que el saber circule sin barreras geográficas o físicas.

Actualmente, el mercado de clases particulares opera de manera muy fragmentada. Si bien la utilización de redes de vínculos entre personas genera confianza, tiene un alcance muy limitado y se restringe a entornos geográficos inmediatos. El proyecto centraliza la oferta en un ecosistema digital donde la búsqueda, la reserva y los pagos conviven en un solo sitio. Esto profesionaliza la labor docente y ofrece a las familias un entorno transparente para potenciar los resultados escolares.

Un pilar central es el diseño de un modelo de confianza para el resguardo de los alumnos. Se plantea como objetivo deseado la implementación de procesos de certificación que idealmente incluyan validación de identidad, títulos y antecedentes de los tutores. Esta meta busca garantizar que el vínculo educativo sea seguro y cumpla con estándares de excelencia verificables.

Finalmente, el proyecto apunta a expandir el alcance de muchos profesionales y a facilitar el acceso al apoyo escolar personalizado mediante una plataforma digital con reputación dinámica y aulas virtuales integradas. Al poner en valor la labor de los tutores y formalizar el sector, este proyecto se posiciona como una infraestructura esencial para conectar a los estudiantes con educadores calificados, superando las barreras geográficas y generando un sustento económico para estos últimos. El impacto de esta solución se observará en la eficiencia del motor de matching, la estabilidad de las conexiones remotas y el nivel de satisfacción de los usuarios.

## Abstract (English)

Tinku is a digital educational marketplace platform designed to connect
Argentine primary, secondary, and university students with qualified academic tutors, virtually and without geographical restrictions. The system centralizes the search, booking, delivery, and payment of private lessons within a single digital ecosystem. It incorporates artificial intelligence for personalized student-tutor matching and the automatic generation of session summaries. The platform seeks to democratize access to academic support, formalize independent teaching work, and contribute to reducing school dropout rates nationwide.

# Capítulo 1: Introducción

## Introducción

Argentina es un país de geografías extremas. Entre sus más de 2,7
millones de kilómetros cuadrados conviven la densidad metropolitana del
Gran Buenos Aires con la soledad de la Puna jujeña, los valles catamarqueños, la estepa patagónica y los pequeños pueblos del interior profundo donde una escuela puede ser el único edificio público. En esos lugares, la educación formal llega –aunque con dificultades– pero el apoyo académico extracurricular prácticamente no llega. Un alumno de quinto año de secundaria en San Antonio de los Cobres que necesita reforzar matemáticas antes de un examen de ingreso universitario no tiene, hoy, una opción realista de encontrar un tutor particular en su localidad. Su única alternativa sería viajar horas hasta la ciudad más cercana, un costo económico y logístico que la mayoría de las familias no puede sostener.

Pero el problema no se limita a la geografía. La educación tradicional, por su naturaleza institucional, opera bajo un modelo de enseñanza uniforme: el docente avanza al ritmo del grupo, con un programa fijo, en tiempos determinados. Este modelo, aunque necesario para garantizar la universalidad de la instrucción, tiene una desventaja estructural bien documentada: no todos los estudiantes aprenden los mismos contenidos al mismo tiempo ni de la misma manera. Un alumno que no comprende el concepto de función matemática en el momento en que se enseña en clase no tiene, dentro del sistema formal, un mecanismo inmediato de recuperación personalizada. Si ese alumno no cuenta con apoyo extraescolar, la brecha entre él y el resto del grupo se amplía progresivamente, con consecuencias que en muchos casos terminan en repitencia o abandono escolar.

Las clases particulares han sido históricamente la respuesta informal de la sociedad argentina a este problema. Sin embargo, este mercado opera en condiciones de notable fragmentación: la oferta de tutores se articula principalmente a través de redes de recomendación interpersonal, sin estándares de calidad verificables, sin transparencia en las transacciones y sin mecanismos formales de protección para ninguna de las partes. Si bien en los grandes centros urbanos –Buenos
Aires, Córdoba, Rosario, Mendoza– la oferta de tutores es relativamente abundante y accesible, y la plataforma puede ser utilizada también en esos contextos, el impacto diferencial de Tinku se proyecta especialmente en aquellos lugares donde esa oferta hoy es inexistente o insuficiente: pueblos de montaña, localidades del interior, zonas rurales. Es ahí donde un ecosistema digital puede cambiar la ecuación.

En este contexto nace Tinku, cuyo nombre proviene de la lengua quechua –idioma originario presente en las provincias del Noroeste
Argentino– y significa *encuentro* o *punto de unión*. El término captura con precisión la misión del proyecto: construir el punto de encuentro digital entre quienes necesitan aprender y quienes tienen el conocimiento para enseñar, sin importar en qué rincón del país se encuentren. La conectividad a internet, incluso en zonas remotas, ha mejorado sustancialmente gracias a iniciativas de satelital de baja órbita como Starlink, que está siendo adoptada masivamente en localidades del interior argentino, ampliando de manera concreta la base de usuarios potenciales de la plataforma.

Tinku propone una plataforma digital de marketplace educativo que centraliza en un único ecosistema la búsqueda de tutores, la reserva de sesiones, el dictado de clases virtuales y la gestión de pagos, incorporando IA como eje diferenciador: un motor de matching semántico que compatibiliza perfiles de alumnos y tutores, y herramientas de apoyo post-sesión que extienden el valor de cada clase más allá del tiempo de pantalla.

## Planteo del problema

El mercado de clases particulares en Argentina presenta tres problemas estructurales que este proyecto busca resolver:

- **Informalidad y fragmentación de la oferta:** no existe en la actualidad una plataforma nacional que centralice y estandarice la oferta de tutores académicos. El proceso de búsqueda depende casi exclusivamente de recomendaciones informales, lo que dificulta la comparación objetiva entre tutores y expone a las familias a una experiencia de contratación sin garantías de calidad verificables, sin transparencia en los precios y sin mecanismos formales de protección para ninguna de las partes.
- **Brecha geográfica en el acceso al apoyo escolar:** el acceso a tutores especializados está fuertemente concentrado en los grandes centros urbanos. Los estudiantes de localidades del interior del país –pueblos pequeños, comunidades de montaña, zonas rurales– no cuentan con alternativas accesibles de apoyo académico extracurricular. En muchos casos, encontrar un tutor implicaría recorrer decenas o cientos de kilómetros, una opción económica y logísticamente inviable para la mayoría de las familias. Si bien las zonas urbanas también pueden beneficiarse de la plataforma, es en estas regiones donde el impacto potencial es mayor y la ausencia de alternativas es más crítica.
- **Desajuste entre el ritmo de enseñanza colectiva y el aprendizaje individual:** el sistema educativo formal, por su naturaleza grupal, no puede adaptarse al ritmo particular de cada alumno. Estudiantes que no comprenden un tema en el momento en que se enseña quedan progresivamente rezagados, sin un mecanismo institucional de recuperación personalizada. La tutoría particular es la herramienta más efectiva para cerrar esta brecha, pero su acceso no es universal.

Estos tres factores generan un mercado subdesarrollado que no aprovecha el potencial existente: miles de docentes y graduados universitarios con capacidad y disposición para ofrecer tutorías, que no encuentran una plataforma que profesionalice y amplíe su alcance más allá de su entorno geográfico inmediato.

## Hipótesis de investigación

**Hipótesis central.** La implementación de una plataforma digital de marketplace educativo con capacidades de matching inteligente basado en búsqueda semántica (NLP) permitirá que estudiantes ubicados en zonas geográficas con escasez de tutores locales
–incluyendo pueblos pequeños, comunidades de montaña y regiones rurales– accedan a servicios de apoyo académico personalizado de calidad equivalente a la disponible en centros urbanos, al tiempo que generará oportunidades de ingreso para tutores en áreas con exceso de oferta relativa, contribuyendo a reducir la brecha de acceso al apoyo escolar en todo el territorio argentino.

Esta hipótesis implica dos afirmaciones técnicas verificables al término del proyecto:

- El motor de matching semántico produce recomendaciones de tutores percibidas como relevantes por los usuarios, medido a través de pruebas de usabilidad y métricas de aceptación de sugerencias.
- La plataforma es técnicamente capaz de conectar usuarios de distintas provincias del país en sesiones de tutoría virtual en tiempo real con calidad de comunicación aceptable, incluso en contextos de conectividad variable.

## Objetivos

### Objetivo general

Diseñar, desarrollar e implementar una plataforma digital de marketplace educativo que conecte, a escala nacional, a estudiantes de nivel primario, secundario y universitario con tutores académicos calificados, mediante un sistema de matching inteligente basado en IA, un aula virtual integrada y un modelo de confianza verificable, con el fin de ampliar el acceso al apoyo escolar personalizado y profesionalizar el mercado de tutorías particulares en
Argentina, con especial impacto en comunidades y regiones donde la oferta presencial de tutores es escasa o inexistente.

### Objetivos específicos

- **OE1 — Análisis del mercado y estado del arte:** relevar el estado actual del mercado de tutorías en Argentina y plataformas educativas similares a nivel global, identificando brechas de funcionalidad y oportunidades de diferenciación tecnológica.
- **OE2 — Diseño de arquitectura del sistema:** definir la arquitectura técnica completa de Tinku, incluyendo modelo de datos, contratos de API, diseño UX y flujos operativos principales.
- **OE3 — Implementación del motor de matching
          IA:** desarrollar e integrar el microservicio de recomendación basado en embeddings semánticos semánticos
          (sentence-transformers + pgvector) para la sugerencia de tutores compatibles.
- **OE4 — Desarrollo del aula virtual (LiveKit):**
          implementar el módulo de videollamada mediante
          LiveKit/WebRTC integrado nativamente en la plataforma, con gestión de estado de sala en tiempo real a través de Redis.
- **OE5 — Implementación del sistema de pagos:** integrar la API de MercadoPago Marketplace con modelo de escrow y comisión de plataforma.
- **OE6 — Desarrollo del módulo de IA educativa:**
          implementar el servicio de transcripción y resumen automático de sesiones, y el asistente conversacional de repaso conceptual.
- **OE7 — Implementación del sistema de reputación:**
          desarrollar el sistema de calificaciones bidireccional implementando un umbral mínimo de calificaciones para su exposición pública como medida anti-manipulación.
- **OE8 — Validación funcional:** realizar pruebas de aceptación de usuario (UAT) con un grupo piloto de tutores y alumnos reales, midiendo usabilidad, confianza percibida y satisfacción con el matching propuesto.

## Barreras e impedimentos

El análisis del problema revela un conjunto de barreras que explican por qué la solución propuesta no ha sido desarrollada previamente en el mercado argentino con el nivel de integración que Tinku propone:

- **Barreras de verificación y onboarding:** aunque el objetivo ideal incluye la validación automatizada de antecedentes penales e identidad, los organismos competentes
          (RENAPER, Registro Nacional de Reincidencia) no ofrecen
          API públicas. Esta restricción impide automatizar dicho proceso en el MVP. En consecuencia, la plataforma centrará sus esfuerzos obligatorios de seguridad y confianza en la rigurosa verificación de los antecedentes académicos. Para dictar clases a menores, además, el tutor debe cargar un
          CAP vigente, tramitado por él mismo, que se revisa de forma manual. La exigencia se limita a los tutores de menores para no sumar fricción al registro de quienes enseñan a adultos, el recurso más escaso de la plataforma en su etapa inicial (capítulo~[§cap:riesgos]). El proceso de registro básico exigirá únicamente la demostración empírica de los conocimientos del tutor mediante la presentación de historial académico, títulos de grado o certificaciones pertinentes. Esta estrategia no solo sortea el impedimento técnico estatal, sino que alinea el sistema de admisión directamente con el objetivo central de la plataforma: asegurar la excelencia académica del apoyo escolar.
- **Barrera de adopción cultural:** el mercado de tutorías en Argentina opera bajo una lógica de confianza interpersonal muy arraigada. La migración hacia una plataforma digital requiere demostrar que la calidad y la seguridad del servicio son equivalentes o superiores al modelo informal vigente.
- **Barrera de conectividad:** aunque la cobertura de internet ha mejorado sustancialmente –y tecnologías como
          Starlink están siendo adoptadas masivamente en localidades del interior argentino, llevando conectividad satelital de banda ancha a zonas que antes carecían de ella– sigue existiendo un segmento de la población, especialmente en contextos de bajos recursos, que no puede acceder a estos servicios ni cuenta con dispositivos adecuados. Esta realidad puede limitar el alcance efectivo de la plataforma en los contextos donde el impacto social sería mayor, y debe ser considerada en el diseño de la experiencia de usuario.
- **Barrera de la masa crítica (arranque en frío):** como todo marketplace bilateral, Tinku resulta más valioso cuantos más tutores y alumnos lo utilizan. La estrategia de lanzamiento deberá contemplar mecanismos de adquisición simultánea de usuarios en ambos lados de la plataforma.
- **Barrera técnica — IA en tiempo real:** la transcripción y resumen automático de sesiones implica procesamiento de audio post-sesión, lo que requiere gestión eficiente de recursos computacionales para mantener costos operativos controlados en la fase de MVP.

## Relevancia del proyecto

La relevancia de Tinku se articula en tres dimensiones complementarias:

**Relevancia social.** Argentina presenta tasas de repitencia y abandono escolar que afectan especialmente a estudiantes en situaciones de vulnerabilidad educativa –entre ellos, quienes no logran seguir el ritmo de enseñanza colectivo y carecen de acceso a apoyo extracurricular. El acceso a tutoría personalizada y oportuna es uno de los factores protectores más eficaces contra la deserción escolar.
Tinku busca extender ese acceso a estudiantes que hoy no pueden aprovecharlo, ya sea por razones geográficas, por desconocimiento de la oferta disponible, o por la ausencia de plataformas que concentren y estandaricen esa oferta.

**Relevancia económica.** El mercado latinoamericano de tutorías online generó USD 637,3 millones en ingresos en 2023 y se proyecta un crecimiento anual compuesto del 16,6 % hasta 2030, según
[grandview2024]. A nivel global, el mercado de tutorías privadas fue valorado en USD 124,5 mil millones en 2024 y se proyecta alcanzar
USD 238,5 mil millones hacia 2033, con una CAGR del 7,5 %
[researchmarkets2024]. En Argentina, el segmento opera en su mayoría de manera informal, sin registro de transacciones ni facturación formal. Tinku propone formalizar una porción de ese mercado, habilitando el cobro digital, generando historial de actividad y contribuyendo a la bancarización de los tutores.

**Relevancia tecnológica.** El proyecto aplica tecnologías de
IA de vanguardia –embeddings semánticos semánticos para matching, modelos de lenguaje de gran escala (LLM) para asistencia educativa– a un problema local concreto. Esta aplicación constituye un aporte original al estado del arte en plataformas educativas adaptativas en el contexto latinoamericano, diferenciándose de soluciones globales por su foco en las particularidades del sistema educativo y la geografía argentina.

## Enfoque metodológico

El proyecto se abordará desde una metodología de desarrollo ágil (Scrum adaptado) combinada con un proceso de investigación aplicada. Las etapas principales son:

- **Investigación y relevamiento:** análisis del estado del arte, entrevistas con tutores y alumnos potenciales, relevamiento de plataformas competidoras (Preply, Wyzant,
          Superprof, Tusclases).
- **Diseño de arquitectura y UX:** definición del modelo de datos, diseño de wireframes y prototipos de alta fidelidad, validación con usuarios.
- **Desarrollo iterativo del MVP:** implementación por módulos funcionales con ciclos de revisión quincenales.
- **Integración y pruebas:** pruebas unitarias, de integración y de aceptación de usuario (UAT).
- **Piloto y validación:** lanzamiento controlado con grupo reducido de tutores y alumnos reales para validar la hipótesis central.
- **Documentación y presentación:** elaboración del informe final y presentación del producto funcional.

## Alcance del proyecto

El presente proyecto abarca el diseño completo y la implementación funcional de la versión MVP de Tinku. Este desarrollo comprende un frontend web estructurado como PWA, el cual proveerá todas las interfaces de usuario necesarias para alumnos, tutores y administradores. El núcleo del sistema estará compuesto por un backend
API REST que expondrá todos los endpoints operativos, respaldado por una base de datos relacional en PostgreSQL para el modelo de datos principal y Redis para la gestión del estado en tiempo real. El backend se implementa en Java mediante el framework Spring Boot. Todo este ecosistema será desplegado sobre infraestructura cloud utilizando
Supabase y Vercel, incluyendo la entrega de la documentación correspondiente a su arquitectura.

A nivel funcional, la plataforma integrará un microservicio de matching impulsado por IA y un módulo de aula virtual soportado por la tecnología de LiveKit (WebRTC). El flujo económico estará cubierto mediante la integración con MercadoPago para la gestión de pagos bajo la modalidad de escrow. Para potenciar la experiencia educativa, se implementará un módulo de resumen automático de sesiones, que el alumno activa como adicional opcional en cada reserva, utilizando un LLM que procesa audio nativamente (Gemini
3.5 Flash-Lite, capítulo~[§cap:economica]). Adicionalmente, el
MVP contará con un sistema de calificaciones y reputación bidireccional, junto con un panel de administración básico para la gestión interna de la plataforma. La plataforma incluye, además, un portal de denuncias con verificación de veracidad, que preserva la evidencia disponible –el fragmento capturado por el kill-switch y la aportada por quien denuncia– y deriva la resolución final a revisión manual.

Por último, es importante delimitar que este proyecto no incluye ciertas características en su fase inicial. Quedan excluidos de este alcance: el desarrollo de aplicaciones móviles nativas; la integración automatizada mediante API con sistemas estatales (reemplazada por la carga y revisión manual del CAP para los tutores de menores); el desarrollo de un módulo de accesibilidad completo; la implementación de un modelo de suscripción premium; la posibilidad de extender la duración de una sesión de videollamada en curso mediante un cobro adicional; y la incorporación de tutores menores de edad. Todas estas iniciativas y funcionalidades no incluidas quedarán debidamente documentadas como propuestas para el trabajo a futuro.

## Limitaciones

- **Límite de validación:** la validación de la hipótesis se realizará con un grupo piloto acotado. Los resultados son indicativos de la validez funcional del sistema, no estadísticamente representativos del mercado total.
- **Límite de verificación de tutores:** en el MVP, la verificación combina un chequeo automático de mayoría de edad mediante reconocimiento óptico (OCR) sobre la fecha de nacimiento del DNI cargado, y una revisión manual final de la autenticidad del documento y la correspondencia de los certificados académicos declarados. La verificación automatizada de antecedentes vía API queda fuera de alcance; para dictar clases a menores se exige, en cambio, la carga y revisión manual de un CAP vigente, con actualización anual (capítulo~[§cap:riesgos]).
- **Límite de conectividad:** el servicio requiere conexión a internet estable para el aula virtual. Si bien Starlink y otras soluciones satelitales amplían el universo de usuarios potenciales, persiste una porción de la población objetivo sin acceso adecuado a dispositivos o conectividad.
- **Límite del asistente IA:** el asistente conceptual opera sobre el resumen de la sesión y el conocimiento del modelo subyacente. No tiene acceso a libros de texto o currículos oficiales específicos del sistema educativo argentino.
- **Límite geográfico del piloto:** la validación funcional queda circunscripta al territorio argentino. La plataforma está diseñada para escalar regionalmente, pero dicha expansión excede el alcance de este trabajo.
- **Límite de alineación curricular:** dado que el sistema educativo argentino no tiene un diseño curricular único a nivel nacional, un tutor de una jurisdicción puede no estar alineado con los contenidos específicos que se enseñan en la escuela del alumno en otra provincia. Esta limitación no invalida la propuesta de valor de la plataforma, pero marca un límite real de la personalización ofrecida.
- **Límite de disponibilidad en fase de desarrollo:**
          mientras se construye el MVP, el backend se aloja en infraestructura propia del desarrollador y no en un proveedor cloud con garantías de disponibilidad, lo que implica un punto único de falla hasta la migración planificada a un VPS
          antes del piloto con usuarios reales, prevista para el
          Sprint~11.

## Justificación

La elección de Tinku como proyecto final de Ingeniería en
Informática se fundamenta en la convergencia de tres elementos clave para un proyecto de calidad: aplicación en el mundo real, uso de tecnología innovadora y potencial de impacto social demostrable.

El problema que Tinku aborda es real y urgente. La brecha en el acceso al apoyo escolar personalizado –acentuada por la geografía argentina y por la rigidez del modelo de enseñanza colectiva– afecta a miles de estudiantes hoy. No se trata de un problema académico hipotético, sino de una necesidad concreta con consecuencias medibles en las tasas de repitencia y abandono escolar.

La solución incorpora tecnologías emergentes de manera que genera valor diferencial concreto: no se intenta construir un modelo de IA
general, sino aplicar embeddings semánticos semánticos y modelos de lenguaje a un problema de matching y apoyo educativo específico. La IA
es un medio, no un fin en sí mismo.

Finalmente, el nombre del proyecto encarna su justificación más profunda. Tinku, en quechua, designa el encuentro ritual entre comunidades de distintos lugares –un momento en que las diferencias geográficas se suspenden y el intercambio es posible. Eso es exactamente lo que la plataforma propone: hacer que la distancia entre el estudiante de una comunidad de montaña y el tutor especializado de una ciudad sea un dato irrelevante. Que el nombre de un idioma originario del Noroeste
Argentino esté en el centro de un proyecto de ingeniería de sistemas es, en sí mismo, una declaración de intenciones sobre qué tipo de tecnología se quiere construir.

## Recursos preliminares

**Tabla:** Recursos preliminares del proyecto

| **Categoría** | **Detalle** |
| --- | --- |
| Recursos humanos | 1 desarrollador full-stack (autor del proyecto). Tutores y alumnos para el grupo piloto de validación. |
| Infraestructura cloud | Vercel (plan Hobby) para el frontend, Supabase (plan gratuito) para la base de datos Postgres, Upstash (plan gratuito) para Redis, y backend alojado inicialmente en infraestructura propia mediante Coolify y Cloudflare Tunnel, con migración planificada antes del piloto a un VPS de DigitalOcean de 4~GB (USD 24 mensuales). Estimación de costo: USD 0 en fase de desarrollo,  25 USD/mes en la fase de piloto. En operación comercial, Vercel y Supabase pasan a sus planes pagos (capítulo~[§cap:economica]). |
| APIs externas | Para el motor de matching semántico: sentence-transformers para generar los embeddings semánticos y pgvector, extensión de PostgreSQL, para la búsqueda por similitud, con procesamiento propio y sin costo de API por request. Para la transcripción y el resumen de sesión, y para el asistente conceptual: Gemini 3.5 Flash-Lite para la transcripción y resumen directo de audio, elegido por costo frente a GPT-4o y a Gemini 3.6 Flash; Gemini 2.0 Flash, candidato inicial, fue dado de baja en junio de 2026 (capítulos [§cap:marco-tecnologico] y [§cap:economica]). MercadoPago: sin costo fijo, comisión por transacción, con SDK oficial en Java. LiveKit Cloud: plan gratuito Build de 5.000 minutos de participante por mes. |
| Herramientas de desarrollo | OpenCode + Neovim (editor principal), GitHub (control de versiones), Figma (diseño UX), Postman (testing API), Jest (testing unitario). Herramientas de IA generativa: OpenCode, Gemini, ChatGPT y Claude Code (capítulo~[§cap:metodologia], sección~[§sec:desarrollo-ia]). |
| Tiempo estimado | 6 meses de desarrollo. Dedicación aproximada: 15–20 horas semanales. |
| Conocimientos previos | Desarrollo web full-stack (React para el frontend, Java con Spring Boot para el backend), bases de datos relacionales, fundamentos de ML, integración de API REST. |

# Capítulo 2: Metodología y procedimientos

## Introducción

El presente capítulo describe el marco metodológico adoptado para el desarrollo de Tinku. En línea con los requisitos del proyecto final, la metodología se articula en dos dimensiones complementarias: la metodología de investigación, que define cómo se aborda el problema, se recolecta la información y se validan los resultados; y la metodología de gestión del proyecto, que establece cómo se organiza, planifica y ejecuta el trabajo de desarrollo a lo largo del tiempo disponible. Ambas dimensiones son necesarias y se retroalimentan: el proceso investigativo informa las decisiones de diseño técnico, mientras que el marco de gestión garantiza que esas decisiones se implementen de manera ordenada, dentro del alcance y los plazos establecidos.

## Tipo de investigación

El presente proyecto se enmarca dentro de la **investigación aplicada**. A diferencia de la investigación básica –orientada a la producción de conocimiento teórico sin aplicación inmediata– la investigación aplicada parte de un problema real y concreto, y genera conocimiento con utilidad directa para resolverlo. En el caso de
Tinku, el problema es la fragmentación e inaccesibilidad del mercado de tutorías académicas en Argentina, y el conocimiento generado se materializa en un artefacto funcional: una plataforma digital que conecta tutores y alumnos a escala nacional. El aporte original del proyecto reside en la aplicación de técnicas de matching semántico basadas en IA a un dominio educativo local, y en la integración de funcionalidades de tutoría virtual en un único ecosistema diseñado para las condiciones geográficas y de conectividad del territorio argentino.
El enfoque es de carácter mixto: predominantemente cualitativo en la fase de relevamiento del problema y cuantitativo en la fase de validación.

## Metodología de la investigación

La investigación se estructura siguiendo las etapas del proceso científico aplicado al desarrollo de sistemas de información.

### Área temática

El área temática del proyecto se sitúa en la intersección entre el desarrollo de plataformas digitales de tipo marketplace, la IA
aplicada al matching de usuarios, y la tecnología educativa
(EdTech).

### Planteamiento del problema

El problema de investigación se formula como la ausencia de una plataforma nacional que centralice, estandarice y amplíe geográficamente el acceso al mercado de tutorías particulares en
Argentina.

### Delimitación de la investigación

La investigación se delimita a los objetivos específicos OE1 a OE8
definidos en el capítulo~[§cap:introduccion], con foco en el diseño e implementación del MVP de Tinku para el mercado argentino.
Quedan fuera del alcance investigativo los mercados regionales, la integración con organismos estatales y los módulos de accesibilidad y suscripción premium, los cuales se documentan como trabajo futuro.

### Marco teórico

Se realizará una búsqueda sistemática de bibliografía académica y técnica sobre los temas centrales del proyecto, abarcando plataformas de marketplace educativo, algoritmos de recomendación basados en embeddings semánticos semánticos, sistemas de reputación en plataformas digitales, tecnología WebRTC aplicada a educación, y el contexto educativo argentino. Esta revisión se documenta en el capítulo~[§cap:marco-teorico]. Las fuentes a consultar incluyen artículos científicos, tesis de grado y posgrado, documentación técnica oficial, informes de mercado de organizaciones como Grand View Research y Research and Markets, y reportes del Ministerio de Educación de la
Nación Argentina.

### Diseño concreto de investigación

A partir de la información relevada, se definirá el diseño técnico del sistema, abarcando la arquitectura, el modelo de datos, los flujos de usuario y los contratos de API. Esta etapa se documenta en el capítulo~[§cap:marco-tecnologico].

### Indicadores

Los indicadores principales para verificar la hipótesis central se resumen en la tabla~[§tab:indicadores].

**Tabla:** Indicadores del proyecto

| **ID** | **Variable** | **Indicador** | **Umbral** |
| --- | --- | --- | --- |
| I-01 | Aceptación del matching | Tasa de aceptación de las sugerencias del motor por parte del alumno | $> 60 %$ de recomendaciones aceptadas en el piloto |
| I-02 | Calidad percibida de la sesión | Puntuación promedio otorgada por los alumnos en el cuestionario post-sesión (escala 1 a 5) | $4{,}0$ |
| I-03 | Cobertura geográfica del piloto | Sesiones completadas entre usuarios de provincias distintas | Al menos 1 sesión exitosa entre dos provincias, incluyendo una del interior |
| I-04 | Satisfacción y recomendación | NPS del piloto | Porcentaje positivo (promotores $>$ detractores) |

### Técnicas de recolección de datos

Se implementarán técnicas cualitativas y cuantitativas para la recolección de datos primarios. La técnica cualitativa consistirá en entrevistas para validar el problema planteado, identificar puntos de dolor en el proceso de búsqueda y contratación, y relevar expectativas.
La técnica cuantitativa se basará en encuestas de validación de demanda para cuantificar la frecuencia de uso de tutorías, los canales actuales de búsqueda y la disposición a utilizar y pagar por una plataforma centralizada.

### Instrumentos de recolección de datos

Se utilizarán entrevistas semiestructuradas aplicadas a una muestra de al menos dos tutores particulares activos y cuatro alumnos o familias que hayan contratado tutorías, complementadas con un formulario breve en
Tally orientado a alumnos, familias con hijos en edad escolar y tutores, buscando un mínimo de 30 respuestas válidas. El guion de las entrevistas se transcribe en el apéndice~[§apx:entrevista] y la encuesta completa en el apéndice~[§apx:encuesta].

### Datos

Los datos a obtener consistirán en registros de audio provenientes de las entrevistas semiestructuradas y datos tabulares generados a partir de las respuestas numéricas y de selección múltiple del formulario digital.

### Procesamiento de los datos

Las entrevistas serán grabadas con el consentimiento del entrevistado para luego ser transcritas en su totalidad y analizadas mediante codificación temática, mientras que los datos cuantitativos obtenidos de los formularios serán agrupados y tabulados para permitir un conteo y evaluación estadística de las métricas.

### Análisis de los datos

Los datos recolectados durante el piloto funcional y la validación de demanda se analizarán en relación con los indicadores definidos, presentando los resultados estructurados en el capítulo~[§cap:resultados].

### Síntesis y conclusiones

La síntesis de los datos contrastados con los indicadores de validación evaluará el cumplimiento de la hipótesis central, presentando las conclusiones finales y las implicancias del proyecto en el capítulo~[§cap:conclusiones].

## Metodología de gestión del proyecto: Scrum adaptado

Para la planificación y ejecución del desarrollo de Tinku se adopta
**Scrum adaptado a un contexto unipersonal**, siendo el marco ágil más apropiado dado que se cuenta con un único desarrollador, un conjunto de módulos técnicos bien delimitados y una fecha de entrega final fija.
La metodología en cascada fue descartada porque asume que todos los requisitos pueden definirse con precisión al inicio y que las etapas son completamente secuenciales, lo cual choca con la necesidad de iteración en proyectos con IA e integraciones complejas como LiveKit o
API externas. Kanban fue descartado como marco principal porque, aunque útil para tareas diarias, no provee la planificación por objetivos ni los hitos verificables exigidos por el cronograma académico.

Scrum organiza el trabajo en **sprints de dos semanas** con objetivos concretos, revisión del incremento al final de cada ciclo y un backlog priorizado. En este contexto unipersonal, el desarrollador asume los roles de Product Owner, Scrum Master y Development Team, contando con el director del proyecto como stakeholder externo para la revisión académica. Los artefactos incluyen el Product Backlog, el
Sprint Backlog y el Incremento, mientras que las ceremonias adaptadas comprenden la Sprint Planning de una hora al inicio de cada ciclo, un
Daily Stand-up diario personal documentado en la bitácora de desarrollo, la Sprint Review y la Sprint Retrospective.

## Gestión del proyecto: dimensiones clave

En línea con los criterios de evaluación del proyecto y el perfil directivo en Project Management Professional, se detallan las dimensiones principales de gestión:

- **Alcance:** definido por los nueve módulos del MVP
          descritos en el capítulo~[§cap:introduccion]. Requiere aprobación explícita cualquier funcionalidad adicional para el control del alcance, apoyándose en el uso del Product Backlog, el Sprint Backlog y los incrementos funcionales.
- **Tiempos:** el proyecto se estructura en sprints de dos semanas a lo largo de seis meses entre junio y noviembre de
          2026, con una dedicación estimada de 15 a 20 horas semanales e hitos académicos inamovibles, integrando las ceremonias del marco ágil adoptado.
- **Costos:** los costos operativos del MVP se estiman entre cero y cien dólares mensuales durante el desarrollo, cubiertos mediante planes gratuitos y de bajo costo en la nube, detallándose plenamente en el capítulo~[§cap:economica].
- **Riesgos:** el análisis detallado se presenta en el capítulo~[§cap:riesgos], contemplando factores como demoras en la integración de API externas, costos de modelos de lenguaje superiores a los estimados y la dificultad para reclutar usuarios para el piloto.
- **Calidad:** cada módulo desarrollado debe superar pruebas unitarias con una cobertura mínima del 70 %, además de sortear una batería de pruebas de integración previas al piloto, midiendo la calidad percibida mediante los indicadores específicos de la investigación.
- **Recursos:** un desarrollador full-stack con conocimientos en React, Java con Spring Boot, Python y bases de datos relacionales, junto al uso de herramientas tecnológicas de soporte y la estructura de roles unipersonales descrita.
- **Satisfacción de los interesados:** se medirá a través de un sistema de calificaciones post-clase bidireccional para mantener altos estándares de calidad, complementándose con el análisis del NPS del grupo piloto para comprobar el grado de utilidad percibida y la aplicabilidad de los resultados en escenarios reales.

## Cronograma de entregables

El cronograma fue construido de atrás hacia adelante tomando como fecha límite el 28 de noviembre de 2026, fecha estimada de la presentación final, y distribuyendo los entregables académicos y los sprints de desarrollo de manera que cada capítulo se apoye en trabajo ya realizado
(tabla~[§tab:hitos]).

**Tabla:** Cronograma de entregables y sprints asociados

| **Hasta** | **Entregable académico** | **Sprints de desarrollo asociados** |
| --- | --- | --- |
| 9 jun 2026 | Cap.~2 Metodología | Sprint 0: setup del entorno, estructura del repositorio, wireframes iniciales + spike/prototipo técnico (kill-switch) |
| 28 jul 2026 | Cap.~3 Marco teórico | Sprints 1–2: autenticación y perfiles de usuario (backend + frontend) |
| 18 ago 2026 | Cap.~4 Marco tecnológico | Sprints 3–4: motor de matching IA + sistema de búsqueda y filtros |
| 8 sep 2026 | Cap.~5 Justificación económica | Sprints 5–6: reservas + integración MercadoPago |
| 22 sep 2026 | Cap.~6 Análisis de riesgos | Sprint 7: aula virtual (LiveKit + Redis) |
| 13 oct 2026 | Cap.~7 Resultados | Sprints 8–9: módulo IA educativa + sistema de reputación |
| 27 oct 2026 | Cap.~8 Conclusiones | Sprint 10: integración end-to-end, pruebas de sistema y correcciones |
| 28 nov 2026 | Presentación final + producto funcional | Sprint 11: piloto con usuarios reales, análisis de resultados, documentación final |

Cabe aclarar que Redis en el Sprint 7 cubre el estado propio de la aplicación –chat en tiempo real, límite de tasa de peticiones– y no el estado interno de LiveKit, que al usarse en su modalidad Cloud queda gestionado del lado del proveedor sin intervención del backend. La figura~[§fig:gantt] muestra la línea de tiempo completa.

<!-- Figura: Cronograma de sprints del proyecto (ciclo lectivo 2026) -->

## Herramientas de gestión y seguimiento

Para garantizar la trazabilidad del trabajo y la calidad del proceso, se implementarán diversas herramientas tecnológicas de soporte. Se utilizará **GitHub Projects** para la gestión del backlog y los sprints mediante tableros Kanban integrados al repositorio, donde cada issue representa una tarea del sprint backlog. El control de versiones se efectuará en GitHub mediante ramas de características y solicitudes de revisión antes de la integración a la rama principal. Asimismo, se mantendrá una bitácora de desarrollo en formato de texto simple actualizada al cierre de cada jornada para registrar avances y decisiones técnicas como parte del seguimiento diario.

Para el diseño de interfaz se empleará Figma en la elaboración de prototipos de alta fidelidad, mientras que Postman servirá para la documentación y prueba de los endpoints de la API REST, y Jest se configurará como marco de pruebas unitarias del frontend, mientras que
JUnit 5 junto con Mockito cumplen ese rol en el backend Spring Boot, ambos integrados en el pipeline de integración continua mediante GitHub
Actions. Para el despliegue, el backend se empaqueta como imagen Docker y se publica mediante Coolify, una plataforma de despliegue autoalojada que gestiona contenedores, certificados y variables de entorno de forma equivalente a un PaaS gestionado, alojada primero en infraestructura propia del desarrollador y migrada a un VPS antes del piloto.

## Desarrollo asistido por inteligencia artificial

La construcción del MVP siguió un método dirigido por especificaciones, en el que la documentación precede al código y guía a un agente de programación basado en IA. El método se organiza en cuatro niveles de documentos, todos versionados en el repositorio
(anexo~[§anx:repositorios]):

- **Constitución.** Principios que gobiernan toda decisión técnica: arquitectura de monolito modular, minimización de datos, seguridad del menor como restricción principal y preferencia por la solución más simple compatible con un único desarrollador y un presupuesto acotado.
- **Especificaciones por módulo.** Nueve documentos, uno por módulo de dominio, con historias de usuario, requerimientos funcionales y reglas de negocio.
- **Planes técnicos.** Diez documentos que traducen cada especificación en un modelo de datos, contratos de API y decisiones de implementación.
- **Lista de tareas.** Una lista de verificación atómica, que funciona como memoria persistente entre sesiones de trabajo: cada tarea se marca como completada solo después de verificarse.

Sobre esa base, en las primeras etapas del desarrollo la implementación se realizó con agentes de OpenCode. Un archivo de instrucciones persistentes (‘AGENTS.md‘), que el agente lee al iniciar cada sesión, fija las reglas de arquitectura, las condiciones de seguridad del menor y los casos en que una decisión exige un registro formal
(*Architecture Decision Record*, ADR). Ante un conflicto o una decisión no prevista, el agente debe detenerse y consultar, en lugar de decidir por su cuenta. Las decisiones resultantes se documentaron en catorce registros de decisión, validados por el autor. Además, se consultaron Gemini y ChatGPT de forma esporádica, como segunda y tercera opinión sobre decisiones puntuales.

El control de calidad del código generado se apoyó en tres mecanismos: las pruebas automatizadas (455 casos de prueba en el backend, incluidas pruebas de extremo a extremo del flujo principal y de la rama de seguridad), la integración continua en GitHub Actions y la revisión de cada cambio antes de integrarlo a la rama principal.

En las etapas posteriores, la documentación, el modelo financiero y la redacción de este trabajo se realizaron con asistencia de Claude Code. La declaración de uso de IA detalla las herramientas y tareas, y el apéndice~[§apx:prompts] registra los prompts más relevantes.

Este método tiene una consecuencia directa sobre el esfuerzo de desarrollo. El historial del repositorio registra unas 103 horas de trabajo para un código que un modelo de estimación tradicional sitúa en el orden de las 10.300 horas (capítulo~[§cap:economica], sección~[§sec:costo-mvp]).

# Capítulo 3: Síntesis de la literatura consultada

## Estado del arte

### Investigaciones nacionales

[torino2023], en su tesis de maestría de la Universidad Torcuato
Di Tella, desarrolló un modelo predictivo de deserción escolar para
Argentina utilizando datos socioeconómicos y habitacionales de la
Encuesta Permanente de Hogares, alcanzando un desempeño del 87,4 %
bajo la métrica AUC-ROC. Un hallazgo relevante para este proyecto es que la autora señala la ausencia, a nivel nacional, de un sistema de seguimiento educativo que permita identificar tempranamente a los estudiantes en riesgo para brindarles un acompañamiento personalizado
–la misma carencia estructural de personalización que Tinku busca atender desde el lado de la oferta de tutorías.

Un estudio sobre ruralidad y educación en Argentina [olea] cuantifica la brecha urbano-rural en la finalización del nivel secundario: mientras que en Tierra del Fuego la diferencia es inferior a
10 puntos porcentuales, en provincias del norte del país –Chaco,
Corrientes, Misiones, Santiago del Estero, Jujuy y Tucumán– la brecha supera los 30 puntos porcentuales entre estudiantes urbanos y rurales de
15 a 17 años. El mismo trabajo documenta que algunas jurisdicciones ya recurrieron históricamente a esquemas de “escuelas mediadas por tecnología con docentes en las ciudades y estudiantes en sus localidades acompañados por tutores” como estrategia para ampliar el acceso –un antecedente conceptual directo del modelo remoto que propone Tinku.

Ambos antecedentes empíricos evidencian, por un lado, la necesidad crítica de implementar sistemas de seguimiento personalizado y, por el otro, validan estructuralmente la eficacia de los modelos mediados por tecnología para sortear las barreras de dispersión geográfica en el territorio nacional.

### Investigaciones internacionales

Respecto del impacto de la tutoría personalizada, una revisión sistemática con meta-análisis de tres niveles [sciencedirect2022] sintetizó evidencia experimental sobre tutoría privada y encontró tamaños de efecto de entre 0,42 y 0,67 sobre el rendimiento académico, con la región y la materia como las variables moderadoras más influyentes entre los trece factores analizados. En la misma dirección, un trabajo reciente sobre tutoría bajo demanda [ondemand2026] sostiene que la tutoría es una de las intervenciones educativas más efectivas para mejorar los resultados de aprendizaje, superando en muchos casos a otras intervenciones como la reducción del tamaño de clase. Ambos antecedentes respaldan empíricamente la Variable~2 del marco teórico de este proyecto (sección~[§sec:variable2]).

En el plano tecnológico, un trabajo de la Universidad de Ottawa
[isotropy2026] propuso un sistema de recomendación semántica de cursos universitarios basado en aprendizaje contrastivo sobre representaciones BERT, aplicado a un catálogo de más de 500 cursos de ingeniería. El antecedente es relevante porque identifica y corrige un problema técnico conocido de los embeddings semánticos tradicionales –la anisotropía, que hace que las representaciones de distintos cursos resulten artificialmente similares entre sí– y constituye el precedente más cercano encontrado al motor de matching que Tinku plantea implementar sobre perfiles de alumnos y tutores. En la misma línea, un estudio publicado en el *Journal of Applied Informatics and
Computing* [paperrec2025] implementó un sistema de recomendación de artículos científicos con sentence-transformers y similitud de coseno, validado con una prueba de usuario de 45 personas en la que el 95,5 %
consideró relevantes las recomendaciones recibidas –un antecedente metodológico útil para diseñar la validación del propio motor de
Tinku. Un tercer trabajo [beefore2024] advierte que, hasta el momento, el uso de sentence-transformers en sistemas de recomendación se limita mayormente a generar información auxiliar para resolver el problema de arranque en frío, y no a operar como mecanismo central de recomendación –lo cual señala un espacio de aporte relativamente inexplorado que coincide con el uso que Tinku le daría a esta tecnología.

Sobre los sistemas de reputación y confianza en plataformas bilaterales, un capítulo del libro *Reengineering the Sharing Economy*
[reputation] desarrolla la teoría detrás de los mecanismos de reputación en mercados online y plantea como pregunta central de diseño si la reputación debe ser bidireccional –como en Airbnb– o unidireccional –como en eBay o Amazon–, señalando que ambos marketplaces resuelven de forma distinta el problema de la información asimétrica entre las partes. Esta discusión respalda directamente la decisión de diseño de Tinku de implementar un sistema de calificación bidireccional entre alumnos y tutores.

Finalmente, en cuanto a la viabilidad técnica de la tutoría virtual, un trabajo presentado en una conferencia de la ACM [webrtc2025] sobre un sistema de enseñanza remota basado en WebRTC para cursos de inglés reportó, tras la optimización de la transmisión de audio y video y la implementación de mecanismos de redundancia multicanal, una tasa de pérdida de video de apenas 0,15 % y una latencia de pizarra de
8,2~milisegundos en un entorno de red educativa –cifras que evidencian que es técnicamente viable sostener sesiones de videollamada estables incluso en condiciones de conectividad variable, tal como requiere la hipótesis central del proyecto.

### Productos y plataformas similares

La tabla~[§tab:comparativa] sintetiza el relevamiento comercial de las cinco plataformas más representativas del sector.

| **Plataforma** | **Modelo de matching** | **Aula virtual integrada** | **Pago dentro de la plataforma** | **Verificación de tutores** | **Alcance / foco geográfico** |
| --- | --- | --- | --- | --- | --- |
| Preply [preply] | Filtros manuales (materia, precio, disponibilidad); sin matching semántico | Sí, parcial (Preply Classroom, hoy limitada mayormente a tutores de inglés) | Sí, por suscripción – comisión de 100 % en la primera clase y de 18 % a 33 % en las siguientes | Reseñas de alumnos + video de presentación del tutor | Global; sin foco en zonas de baja densidad de oferta |
| Wyzant [wyzant] | Búsqueda por filtros | No nativa | Sí | Reseñas | Estados Unidos; más de 80.000 tutores y 4 millones de alumnos |
| Superprof [superprof] | Ninguno – el alumno contacta manualmente a cada profesor | No | No – el pago se coordina fuera de la plataforma | Reseñas de alumnos | Global, incluida Argentina; sin comisión para el profesor |
| Tusclases [tusclases] | Filtros (materia, precio, ubicación); sin matching automático | No | No | Reseñas + título declarado por el profesor | España y Latinoamérica; portal líder en Argentina |
| profe.com [profecom] | Asignación manual por parte de un equipo curado, no es un marketplace abierto | Sí, con pizarra digital | Sí | Selección propia del equipo docente de la plataforma | España; sin presencia en Argentina |

Un dato relevante encontrado durante este relevamiento es que
[profecom] ya ofrece a las familias un panel de seguimiento con “informes personalizados generados por IA con feedback detallado”
sobre el progreso del alumno –el antecedente comercial más cercano encontrado al asistente conceptual post-sesión que Tinku plantea en su alcance (sección~[§sec:alcance]), aunque aplicado sobre un modelo de plantilla docente curada y no sobre un marketplace abierto de tutores independientes.

**Síntesis.** Ninguna de las plataformas relevadas combina simultáneamente las cuatro piezas que propone Tinku: (1) un motor de matching basado en similitud semántica en lugar de filtros manuales, (2) un aula virtual nativa disponible para todas las materias y no solo para determinados perfiles de tutor, (3) un modelo de pago protegido dentro de la plataforma, y (4) un foco explícito en ampliar la oferta hacia zonas geográficas donde hoy es escasa o inexistente. Los competidores de mayor escala en Argentina (Tusclases, Superprof) replican en esencia el modelo de directorio de contactos que el capítulo~[§cap:introduccion] describe como parte del problema
–búsqueda por filtros, contacto manual, sin protección de pago–
mientras que los competidores con aula virtual y pagos integrados
(Preply) no tienen foco geográfico en el país ni resuelven el matching de forma semántica. Ese espacio vacío es, en definitiva, el que este proyecto busca ocupar.

### Oportunidades de diferenciación adicionales

A partir del relevamiento de la sección anterior, se identificaron cuatro funcionalidades que ninguna de las plataformas competidoras ofrece y que se proponen incorporar al alcance del proyecto: el sistema de detección de contenido inapropiado en tiempo real, la reputación con señales implícitas, el precio dinámico por poder adquisitivo regional y el modo de baja conectividad.

    [Sistema de detección de contenido inapropiado en tiempo real
    (“kill-switch” de seguridad).] Ninguna de las plataformas relevadas implementa moderación automática del contenido de la videollamada en sí misma. Existe, sin embargo, un antecedente académico directo:
    [liang2013] desarrollaron SafeVchat, un sistema de detección automática de contenido obsceno para servicios de videollamada aleatoria, que combina múltiples detectores visuales mediante teoría de Dempster-Shafer para decidir en tiempo real si un usuario debe ser bloqueado. Reportaron que la combinación del sistema automático con moderación humana redujo el contenido ofensivo del 33,08 % al
    3,49 %. Dado que una porción significativa de los usuarios de
    Tinku serán menores de edad, se propone un mecanismo que analice localmente (*edge computing*) los fotogramas mediante un modelo de clasificación y que ante una detección positiva corte automáticamente la transmisión y bloquee la cuenta preventivamente.
    El mecanismo técnico completo, incluida la verificación de edad del tutor mediante OCR y DNI, se desarrolla en la sección~[§sec:seguridad].

    **Salvedades a considerar:** ningún clasificador automático tiene 0 % de falsos positivos/negativos; es una capa adicional, no una garantía absoluta. El procesamiento en el dispositivo (por ejemplo, TensorFlow.js) evita enviar video a un servidor, facilitando el cumplimiento de la Ley de Protección de Datos Personales
    (Ley~25.326). El proceso de reactivación manual debe contemplar la notificación a un adulto responsable. Al ser un desarrollo complejo
    (visión por computadora en tiempo real), debe evaluarse su viabilidad dentro de los plazos del MVP.

- **Reputación con fricción reducida (señales implícitas).** — La literatura [reputation] señala que las calificaciones explícitas (estrellas) son propensas a sesgos. Se propone combinar una acción mínima (reacción rápida) con señales de comportamiento capturadas automáticamente: tasa de sesiones completadas, puntualidad, y la tasa de recontratación del mismo tutor por parte del mismo alumno (preferencia revelada).

- **Precio dinámico por poder adquisitivo regional.** — Se propone que la plataforma sugiera un rango de precio de referencia ajustado al poder adquisitivo de la provincia o localidad del alumno, calculado a partir de los datos transaccionales de la plataforma, manteniendo la decisión final en el tutor.

- **Modo de baja conectividad.** — Se propone una degradación progresiva de calidad (video $$ solo audio
    $$ mensajería de texto) ante caídas de ancho de banda, sumado a la retención temporal de un buffer de video rotativo de 30
    segundos, el cual se persiste y envía como evidencia únicamente si se dispara el sistema de seguridad (kill-switch).

### Marco legal

El diseño de la relación contractual entre la plataforma, el adulto responsable y el menor se apoya en el sistema de capacidad progresiva del Código Civil y Comercial de la Nación, artículos 25 y 26, que establece que los adolescentes de entre 13 y 18 años tienen capacidad de ejercicio creciente, pero que los contratos que los comprometan patrimonialmente requieren la representación o el consentimiento de los progenitores según los artículos 682 y 690, salvo los de escasa cuantía de la vida cotidiana previstos en el artículo 684 bis, categoría en la que un paquete de clases particulares no encuadra. De ahí surge la decisión de que la cuenta contratante y pagadora sea siempre la del adulto responsable.

El mismo criterio se refuerza con un antecedente impositivo: el modelo de retención que aplican plataformas comparables en Argentina, como
Uber, Rappi, PedidosYa y Airbnb, donde AFIP obliga al agente de pago a retener hasta un 28 % de lo abonado a quien no esté inscripto en el régimen de Monotributo, funciona como antecedente directo de la estrategia de formalización tributaria de los tutores de Tinku, desarrollada en el capítulo~[§cap:economica]. A esto se suma la jurisprudencia laboral argentina sobre la relación de dependencia encubierta de repartidores de plataformas de delivery, que constituye un antecedente de riesgo legal relevante para el vínculo entre Tinku y sus tutores, documentado como riesgo en el capítulo~[§cap:riesgos].

## Bases teóricas

### Variable 1: matching semántico e inteligencia artificial aplicada a sistemas de recomendación

El motor de matching de Tinku se apoya conceptualmente en dos cuerpos teóricos: los sistemas de recomendación (*recommender systems*), que buscan predecir la afinidad entre dos entidades a partir de sus atributos; y el procesamiento de lenguaje natural (NLP) aplicado a la representación semántica de texto mediante embeddings semánticos. Un embeddings semánticos es una representación vectorial de un texto en un espacio de alta dimensionalidad. Modelos como los sentence-transformers generan vectores a partir de oraciones completas, superando las búsquedas por palabras clave. Sobre este espacio, la búsqueda de los vectores más cercanos (*k-nearest neighbors*) puede resolverse con índices en memoria, como FAISS (Facebook AI Similarity
Search), o dentro de la propia base de datos, como la extensión pgvector de PostgreSQL. Tinku adopta pgvector, por los motivos que se detallan en el capítulo~[§cap:marco-tecnologico].

Como se detalló en la sección~[§sec:estado-del-arte], el trabajo de la Universidad de Ottawa [isotropy2026] validó esta técnica en la recomendación de cursos, corrigiendo el problema de anisotropía. Este antecedente es directamente aplicable a Tinku, donde los perfiles comparten un vocabulario acotado (materias, niveles). La literatura
[beefore2024] identifica que el uso de sentence-transformers como mecanismo central sigue siendo poco explorado, confirmando que la implementación de Tinku representa un aporte que excede la aplicación estándar.

### Variable 2: acceso a educación personalizada y brecha de aprendizaje

La base teórica proviene de la investigación sobre enseñanza individualizada de Carroll [carroll1963] y Bloom
[bloom1968,, bloom1984]. Carroll planteó que el aprendizaje depende de la relación entre el tiempo necesario para dominar un contenido y el tiempo efectivamente destinado. Bloom desarrolló la teoría del
*mastery learning*, sosteniendo que la mayoría puede alcanzar niveles altos de dominio con instrucción personalizada.

El aporte central es el “problema de los 2 sigma” [bloom1984]: alumnos con tutoría individual rinden, en promedio, dos desviaciones estándar por encima de alumnos en instrucción grupal convencional. La propuesta de Tinku responde tecnológicamente a este problema: busca hacer que la tutoría individual sea accesible a escala, superando la barrera de disponibilidad geográfica. Esto es consistente con el meta-análisis de tutoría privada [sciencedirect2022] y el trabajo sobre tutoría bajo demanda [ondemand2026], que la ubican entre las intervenciones más efectivas.

### Relación entre las variables

El vínculo se explica a través de la teoría económica de los mercados bilaterales (*two-sided markets*) [rochet2006]. Un mercado bilateral conecta a dos grupos (alumnos y tutores) donde la participación de uno aumenta el valor para el otro. El mayor riesgo es el problema del arranque en frío, señalado en el capítulo~[§cap:introduccion].

En un mercado geográficamente disperso (Variable~2), el problema del arranque en frío se agrava. La función del matching semántico
(Variable~1) es el mecanismo que permite que esa masa crítica, aunque dispersa, se encuentre eficientemente a escala nacional. Al no depender de coincidencias exactas ni proximidad, el motor permite a Tinku operar como un único mercado denso. Esta es la hipótesis técnica que sostiene el proyecto.

## Marco conceptual

Tinku se ubica dentro del sector EdTech y, específicamente, en los marketplace educativos (dimensionado en el capítulo~[§cap:introduccion]).

En el plano de la infraestructura, el proyecto se apoya en WebRTC, un estándar abierto para comunicación en tiempo real en navegadores.
Sobre este, Tinku utiliza LiveKit, un framework open-source que simplifica la implementación de salas escalables. Para sostener el estado en tiempo real de esas salas, se utiliza Redis (base de datos en memoria clave-valor), necesaria por sus exigencias de baja latencia.

En el circuito de pagos, se apoya en un modelo de escrow implementado a través de MercadoPago Marketplace, reteniendo los fondos hasta la realización de la clase, reduciendo el riesgo de fraude.

Sobre la confianza, Tinku adopta un sistema de reputación bidireccional, respaldado por la literatura [reputation]. Para medir la satisfacción general, se contempla el uso del NPS.
Finalmente, el proyecto se desarrolla bajo un esquema de Scrum adaptado
(capítulo~[§cap:metodologia]).

## Entrevistas a especialistas

Se proponen dos perfiles de especialista complementarios cuyos guiones completos se transcriben en el apéndice~[§apx:entrevista]:
**Perfil 1**, docente o gestor/a institucional, para indagar sobre el rol del apoyo escolar en la prevención de la repitencia, las diferencias urbanas-rurales en el acceso a tutorías y los recaudos pedagógicos y de seguridad de una tutoría virtual; y **Perfil 2**, psicopedagogía / vínculo y seguridad con menores, para abordar el impacto vincular del acompañamiento personalizado, las señales de alerta en entornos remotos y los errores a evitar en el diseño del sistema de reputación.

**[PENDIENTE:** una vez realizada la entrevista, se agregará acá la síntesis de los resultados con fecha, nombre, cargo y aporte de cada persona entrevistada. La evidencia detallada se conserva en el apéndice~[§apx:entrevista]**]**

# Capítulo 4: Marco tecnológico

## Introducción

Este capítulo documenta el *cómo* de Tinku: las decisiones técnicas concretas mediante las cuales se traduce el problema planteado en el capítulo~[§cap:introduccion] y el marco conceptual del capítulo~[§cap:marco-teorico] en un sistema funcional y verificable.
Cada elección tecnológica se justifica en función de tres criterios consistentes con las restricciones ya declaradas en el capítulo~[§cap:metodologia] (sección~[§sec:dimensiones]): un único desarrollador, un presupuesto operativo de entre 0 y 100 USD mensuales durante el desarrollo, y un plazo fijo de seis meses. Cuando existió una alternativa técnicamente superior pero incompatible con esas restricciones, se documenta también por qué fue descartada.

## Arquitectura del sistema

### Estilo arquitectónico

Tinku adopta una arquitectura **cliente-servidor en capas**, con un backend propio que concentra la lógica de negocio y un conjunto de servicios externos especializados y desacoplados para las funciones que no forman parte del núcleo diferencial del producto: video (LiveKit
Cloud), pagos (MercadoPago) e inteligencia artificial (proveedores de modelos de lenguaje y embeddings semánticos). Se descartó una arquitectura de microservicios propios porque, para un equipo de un desarrollador y un
MVP de alcance acotado, la sobrecarga operativa de orquestar múltiples servicios propios (versionado independiente, comunicación entre servicios, observabilidad distribuida) no se justifica frente al beneficio –los “servicios” que sí están desacoplados (video, pagos,
IA) ya lo están porque se delegan a proveedores externos maduros, no porque Tinku los reimplemente como microservicios propios.

### Componentes y responsabilidades

La tabla~[§tab:componentes] resume los ocho componentes del sistema y sus responsabilidades.

**Tabla:** Componentes del sistema y responsabilidades

| **Componente** | **Responsabilidad** | **Tecnología** |
| --- | --- | --- |
| Cliente (PWA) | Interfaz de usuario para alumno, tutor y adulto responsable; consume la API REST del backend | React / Next.js |
| Backend API REST | Lógica de negocio, autenticación y autorización por rol, orquestación de los servicios externos | Spring Boot (Java) |
| Base de datos relacional | Persistencia del modelo de datos principal (usuarios, reservas, pagos, calificaciones, denuncias) | PostgreSQL (Supabase) |
| Caché / estado en tiempo real | Sesiones, chat en tiempo real (pub/sub), rate limiting | Redis (Upstash) |
| Aula virtual | Transmisión de audio/video entre tutor y alumno | LiveKit Cloud (WebRTC) |
| Pasarela de pagos | Procesamiento de cobro vía Checkout Pro | MercadoPago (SDK oficial Java) |
| Servicios de IA | matching semántico, transcripción y resumen de sesión, asistente conceptual, kill-switch de seguridad | sentence-transformers + pgvector, LLM (Gemini 3.5 Flash-Lite), clasificador on-device |
| Panel de administración | Moderación, resolución de denuncias, aprobación de tutores | Módulo interno del backend + vista en el frontend |

### Flujo de datos

El cliente nunca se comunica directamente con los servicios externos con sus propias credenciales: todo pasa por el backend, que actúa como intermediario autenticado. El cliente autentica contra el backend mediante JWT y consume la API REST para las operaciones habituales –búsqueda de tutores, reservas, chat, calificaciones. Para el aula virtual, el backend genera un token de acceso de LiveKit con permisos acotados a la sala correspondiente y se lo entrega al cliente, que recién en ese momento se conecta directamente al servicio de LiveKit
Cloud para el flujo de audio y video; este diseño evita que todo el tráfico de video circule por el propio backend, que no está dimensionado para soportarlo. Los pagos siguen una lógica equivalente: el backend crea la preferencia de pago contra la API de MercadoPago y recibe notificaciones vía webhook cuando el estado del pago cambia, actualizando en consecuencia el estado de la reserva en la base de datos. El matching y la IA educativa, por su parte, se invocan de forma asincrónica –mediante colas o llamadas diferidas– y el resultado se persiste sin bloquear al usuario mientras espera la respuesta de un modelo externo.

### Diagrama de arquitectura

El diagrama muestra los ocho componentes de la tabla~[§tab:componentes] y sus conexiones: el cliente solo se comunica con Vercel (que sirve los archivos estáticos) y, a través de HTTPS, con el backend; el backend es el único componente que tiene credenciales para hablar con Supabase,
Upstash, MercadoPago y los servicios de IA; LiveKit Cloud es la única excepción, donde el cliente se conecta directamente una vez que el backend le entrega un token de corta duración.

<!-- Figura: Diagrama de arquitectura del sistema -->

## Prototipo / MVP construido

El alcance implementado y operativo frente al que todavía está simulado o mockeado se documenta en cada entrega: qué funcionalidades están activas
(por ejemplo, registro, login o búsqueda de tutores) frente a las pantallas de flujo de pago sin integración real. A eso se suman capturas de pantalla de las vistas principales, un enlace al repositorio de código en GitHub (anexo~[§anx:repositorios]) con la estructura de carpetas documentada, una descripción de cómo se probó lo construido hasta el momento –pruebas manuales, UAT con usuarios del piloto, pruebas automatizadas– junto con los resultados obtenidos, y las limitaciones puntuales del estado actual con los próximos pasos según el
Sprint Backlog vigente.

*Completar con el estado del MVP al momento de la entrega.*

## Stack de software

### Frontend

**Tabla:** Frontend: decisión tecnológica

| **Ítem** | **Detalle** |
| --- | --- |
| Tecnología | React (o Next.js, a confirmar según necesidad de server-side rendering) |
| Por qué se eligió | Conocimiento previo del desarrollador (capítulo~[§cap:introduccion], sección~[§sec:recursos]), ecosistema maduro, gran disponibilidad de componentes para formularios, calendarios y videollamada embebida |
| Alternativas evaluadas | Vue.js – descartado por menor familiaridad del desarrollador, lo que hubiera consumido tiempo de aprendizaje no disponible en el cronograma de seis meses |
| Formato de despliegue | PWA, consistente con la exclusión de app móvil nativa del alcance (capítulo~[§cap:introduccion], sección~[§sec:alcance]) |

### Backend

**Tabla:** Backend: decisión tecnológica

| **Ítem** | **Detalle** |
| --- | --- |
| Tecnología | Java 21 + Spring Boot |
| Por qué se eligió | Framework “batteries-included” (seguridad, ORM, validación, manejo de excepciones ya resueltos) que reduce el riesgo de un desarrollador único investigando y ensamblando librerías sueltas bajo un cronograma fijo; alta disponibilidad de documentación y comunidad en español, relevante para un desarrollador sin experiencia previa profunda en ninguno de los lenguajes candidatos |
| Alternativas evaluadas | Go – descartado pese a tener ventajas reales de footprint de memoria y simplicidad del lenguaje, porque su ecosistema requiere ensamblar manualmente router, ORM y librerías de autenticación, lo cual consume tiempo de decisión de arquitectura que un proyecto de 6 meses en solitario no puede permitirse. Node.js – descartado como backend principal por preferirse la robustez de tipado y el ecosistema de seguridad de Spring frente a un desarrollador que tampoco tenía experiencia consolidada previa en ninguno de los dos |
| Autenticación | Spring Security + JWT emitido y validado por el propio backend (no se delega la autenticación a Supabase Auth, dado que el modelo de roles de Tinku –adulto responsable, menor con permisos por acción, tutor, administrador– requiere lógica de autorización granular propia que conviene mantener dentro del mismo framework que ya gestiona el resto de las reglas de negocio) |

### Datos

**Tabla:** Capa de datos: decisión tecnológica

| **Ítem** | **Detalle** |
| --- | --- |
| Motor relacional | PostgreSQL, gestionado por Supabase. Postgres es un motor relacional maduro con buen soporte de extensiones; Supabase ofrece un plan gratuito suficiente para el MVP y evita la administración manual de backups y actualizaciones del motor de base de datos |
| Índice semántico | Extensión pgvector: los embeddings semánticos de 384 dimensiones de cada perfil de tutor se guardan en una columna ‘vector(384)‘ y el servicio de matching resuelve la búsqueda por similitud con una consulta a la base. Se descartó un índice FAISS en memoria del proceso Python porque obliga a reconstruir o restaurar el índice cada vez que el proceso se reinicia, mientras que con pgvector el índice persiste junto con el resto de los datos. A la escala del piloto, la latencia adicional de consultar la base es despreciable, porque la búsqueda se aplica sobre un subconjunto de candidatos ya filtrado por autorización |
| Detalle de conexión | El backend Spring Boot se conecta a través del pooler de Supabase (Supavisor) en modo sesión (puerto 5432), que se comporta como una conexión directa y es compatible con prepared statements de Hibernate sin configuración adicional. Se documenta como decisión explícita porque el modo transacción (puerto 6543) del mismo pooler no es compatible por defecto con el cacheo de prepared statements que usa Hibernate, y migrar a ese modo en el futuro requeriría desactivar esa característica en el driver JDBC |
| Caché / tiempo real | Redis, gestionado por Upstash (plan gratuito serverless por volumen de uso) – usado para estado de chat en tiempo real y rate limiting, no para el estado interno de las salas de videollamada, que en el MVP delega en LiveKit Cloud |
| Respaldo y migraciones | Backups automáticos de Supabase en su plan gestionado; migraciones de esquema versionadas con Flyway o Liquibase integradas al ciclo de despliegue de Spring Boot |

## Infraestructura y hosting

La tabla~[§tab:infra] resume dónde se aloja cada componente.

**Tabla:** Infraestructura y hosting de cada componente

| **Componente** | **Dónde se aloja** | **Notas** |
| --- | --- | --- |
| Frontend (PWA) | Vercel | Plan gratuito (Hobby) durante el desarrollo y plan Pro en operación comercial, porque el Hobby se limita al uso no comercial; CDN global sin configuración adicional |
| Backend (Spring Boot) | Fase de desarrollo: computadora propia del desarrollador, gestionada con Coolify (PaaS autoalojado) y expuesta a internet mediante Cloudflare Tunnel, sin necesidad de IP pública ni apertura de puertos. Fase de piloto (Sprint 11, capítulo~[§cap:metodologia]): migración a un VPS Basic de DigitalOcean de 2 vCPU y 4~GB (USD 24/mes), reutilizando la misma configuración de Coolify | La migración de computadora propia a VPS no requiere reescribir la configuración de despliegue, dado que Coolify orquesta el mismo conjunto de contenedores Docker en ambos casos. Los 4~GB alcanzan para Coolify, Spring Boot y el servicio de matching porque las imágenes se construyen en GitHub Actions y no en el servidor. Se descartó Hetzner porque sus planes económicos no admiten nuevas órdenes y aumentó dos veces sus precios en 2026 |
| Base de datos y Redis | Supabase y Upstash respectivamente | Servicios gestionados en la nube, independientes de dónde corra el backend |
| Audio del resumen opcional | Garage, almacenamiento compatible con S3 autoalojado en el mismo VPS | LiveKit Cloud sube el audio por HTTPS y el backend lo borra al obtener la transcripción, con un máximo de 24 horas. Se descartó MinIO porque su edición comunitaria fue archivada en febrero de 2026 y dejó de recibir parches de seguridad |
| Aula virtual | LiveKit Cloud | Plan gratuito (Build): 5.000 minutos de participante por mes sin necesidad de tarjeta de crédito, equivalente a más de 40 horas de clases de 1 a 1 mensuales – cobertura suficiente para el piloto. Se descartó el auto-hospedaje de LiveKit porque requiere una IP pública alcanzable por UDP para el protocolo WebRTC, algo que ni la computadora de desarrollo ni un VPS económico garantizan sin trabajo adicional de configuración de NAT/TURN |

En cuanto a la escalabilidad: para el rango de tráfico esperado durante el MVP y el piloto (capítulo~[§cap:metodologia]), un único
VPS vertical (backend + base de datos si se optara por auto-alojarla) es suficiente. La estrategia de escalado horizontal
–balanceador de carga con múltiples instancias, o eventualmente
Kubernetes– queda fuera del alcance de esta entrega y se documenta como trabajo futuro, condicionada a que el volumen de uso real lo justifique.

Los costos por componente y por etapa (desarrollo, piloto, eventual escalado) se presentan en el capítulo~[§cap:economica]. El techo de
0–100 USD mensuales declarado en el capítulo~[§cap:metodologia] rige para el desarrollo y el piloto; la operación comercial requiere planes pagos y se evalúa por separado en ese capítulo.

## Modelo de datos

El modelo se organiza alrededor de nueve entidades, cuyo detalle completo de atributos se documenta en el diccionario de datos que se incluye como apéndice técnico. **Usuario** es la entidad base y define un rol (ADULTO, MENOR, TUTOR, ADMIN); un usuario con rol ADULTO puede, además de gestionar sus propios datos, tener uno o más perfiles de MENOR
asociados como responsable. **PerfilMenor** está vinculado a un Usuario con rol ADULTO y hereda una sesión propia, pero con permisos restringidos a nivel de endpoint: no puede iniciar pagos, aceptar acuerdos ni reservar con un tutor no autorizado previamente. **PerfilTutor** concentra las credenciales académicas, la documentación de verificación (DNI, certificados), las materias, la disponibilidad y el precio de referencia, mientras que **Certificado** representa cada documento cargado por el tutor –DNI, título, analítico y, para los tutores de menores, el
CAP– con un estado de revisión (pendiente, aprobado manual, rechazado y, solo para el CAP, en revisión legal). La credencial académica aprobada habilita al tutor en el matching; para dictar clases a menores se requiere, además, un CAP aprobado y vigente.

**Reserva** es el bloque horario entre un PerfilMenor/Usuario ADULTO y un PerfilTutor, con estados que recorren ‘pendiente_pago‘,
‘confirmada‘, ‘en_curso‘, ‘finalizada‘,
‘cancelada‘ o ‘no_show‘. **Sesión** es la instancia de videollamada asociada a una Reserva, con referencia a la grabación de audio y al resumen generado por IA cuando se contrató el adicional de resumen; **Pago** referencia la transacción de MercadoPago asociada a esa Reserva, con su estado de escrow. Por último, **Calificación** es bidireccional y se asocia a una Sesión finalizada, y **Denuncia** se asocia a una Sesión o a un
PerfilTutor/Usuario, con estado de revisión propio y una referencia a la evidencia preservada.

**Relaciones clave:** un Usuario ADULTO $$ varios
PerfilMenor; un PerfilTutor $$ varias Reserva; una Reserva
$$ una Sesión (1 a 1) $$ un Pago (1 a 1)
$$ cero o más Calificación y Denuncia.

**Integridad:** se define una restricción de exclusión a nivel de base de datos (no solo validación de aplicación) para impedir dos Reserva superpuestas del mismo PerfilTutor o del mismo alumno, dado que una validación exclusivamente en el backend es vulnerable a condiciones de carrera cuando dos solicitudes llegan casi simultáneamente.

El perfil de menor de edad no puede crear Reservas directamente ni acceder a flujos de pago; en su lugar, genera una *Solicitud de
Sesión* (entidad separada y no bloqueante) que el Adulto Responsable debe aprobar y abonar para convertirla en una Reserva transaccional. La duración de la Reserva se congela según la franja publicada por el tutor
(entre 30 y 180 minutos), calculándose el monto final al prorratear el valor por hora fijado por el educador.

Por normas estrictas de seguridad, el perfil de menor tiene inhabilitada la acción de generar Denuncias directamente desde su interfaz; cualquier reporte recae exclusivamente bajo la gestión de su Adulto Responsable. El rol ADMIN se divide lógicamente en dos dominios con colas operativas y permisos separados: *Moderación y Seguridad* (alertas del kill-switch, credenciales, sanciones) y *Soporte Financiero*
(intervención manual en fallas de pago). El diccionario de datos completo se presenta en el apéndice~[§apx:tecnicos].

## Diseño y experiencia de usuario (UX/UI)

El onboarding de Términos y Condiciones reemplaza el documento de scroll continuo por un carrusel de cinco a seis tarjetas, cada una con un título, un párrafo breve sobre un punto de los términos y una ilustración; al final, un checkbox de aceptación explícita, desactivado por defecto, habilita la creación de la cuenta, que queda deshabilitada mientras el checkbox no se marca. La interfaz se diferencia según el rol: la de un PerfilMenor no muestra ni expone controles de las acciones reservadas al adulto –pago, gestión de acuerdos, contacto con tutores no autorizados–, y esa restricción opera tanto en el diseño de interfaz como en los permisos de la API, no solo a nivel visual. El sistema contempla una degradación de la videollamada a chat de texto exclusivamente durante una sesión activa en caso de conectividad deficiente.

En accesibilidad, el MVP no incluye un módulo completo
(capítulo~[§cap:introduccion], sección~[§sec:alcance]), pero aplica buenas prácticas básicas: contraste adecuado, tamaños de fuente legibles y navegación con foco visible. La validación del diseño con usuarios se apoya en las entrevistas y encuestas ya definidas en el capítulo~[§cap:metodologia], y en UAT con el grupo piloto
(OE8).

<!-- Figura: Mockups de pantallas principales -->

## Seguridad, calidad y despliegue

### Seguridad

La autenticación se resuelve con JWT emitido por el propio backend a través de Spring Security, con contraseñas almacenadas mediante hash bcrypt; no se utiliza Supabase Auth, por el motivo ya explicado en la sección~[§sec:stack-backend]. El control de accesos se basa en autorización por rol (ADULTO, MENOR, TUTOR, ADMIN) aplicada a nivel de cada endpoint del backend: el modelo de permisos por acción del rol MENOR
(sección~[§sec:modelo-datos]) se implementa como reglas de autorización explícitas, no como una restricción de interfaz que pudiera sortearse llamando directamente a la API. Toda la comunicación viaja cifrada mediante TLS entre el cliente y el backend y entre el backend y los servicios externos, con el cifrado en reposo de la base de datos delegado a Supabase.

La verificación de tutores combina la carga de DNI y certificados académicos con la extracción automática de la fecha de nacimiento mediante OCR (implementado con Tesseract vía Tess4J, ejecutado in-process en el propio backend para garantizar que las imágenes de los documentos nunca se envíen a servicios de terceros), que rechaza automáticamente el registro de cualquier tutor menor de 18 años, y una revisión manual final a cargo del rol ADMIN sobre la autenticidad del documento y la correspondencia de los certificados con las materias declaradas. Para dictar clases a menores, el tutor debe presentar además un CAP vigente, que el rol ADMIN revisa de forma manual y que vence a los doce meses de su emisión. Una primera versión exigía el
CAP a todos los tutores y se retiró (ADR-M1-02); se reincorpora acotada a los tutores de menores, por los motivos que analiza el capítulo~[§cap:riesgos].

El kill-switch de seguridad, presentado como SafeVchat en la sección~[§sec:estado-del-arte] –donde se desarrolla el mecanismo técnico completo, incluida esta misma verificación de edad del tutor vía
OCR y DNI–, se apoya en un clasificador de contenido que corre localmente en el dispositivo (*edge computing*, por ejemplo con
TensorFlow.js) durante la videollamada; ante una detección positiva ejecuta dos acciones diferenciadas: si hay un menor presente, corta la transmisión y suspende preventivamente la cuenta de forma inmediata; si ambos participantes son adultos, el video del detectado se bloquea con un filtro de desenfoque y el sistema solicita confirmación a la contraparte antes de proceder al corte. Como evidencia, el cliente mantiene un buffer de los últimos 30 segundos de la videollamada y lo sube al backend solo si el kill-switch se dispara; las sesiones no se graban de forma completa, salvo el audio de las que contrataron el adicional de resumen.
El portal de denuncias sigue una lógica equivalente: al registrarse una denuncia, el sistema preserva la evidencia disponible –el fragmento del kill-switch, si existe, y la que aporta quien denuncia– fuera del ciclo normal de borrado, suspende preventivamente al usuario denunciado y deriva la resolución final a revisión humana del rol ADMIN.

La protección de datos personales sigue la Ley 25.326, con especial cuidado en el procesamiento de video de menores y en la definición de una política de retención y baja de datos a solicitud del titular o su responsable.

### Calidad y pruebas

Las pruebas unitarias del backend se implementan con JUnit 5 y Mockito, con una cobertura mínima del 70 % (capítulo~[§cap:metodologia]), mientras que las del frontend usan Jest, aplicable a la capa de
React/Next.js –esto corrige la mención original de Jest como herramienta de testing “general” del capítulo~[§cap:metodologia], dado que Jest es específico del ecosistema JavaScript y no aplica al backend Spring
Boot, que usa JUnit y Mockito. Las pruebas de integración corren contra una base de datos de prueba con Testcontainers y Postgres antes de cada release al entorno de piloto, y las UAT se realizan con el grupo piloto, según lo definido en el capítulo~[§cap:metodologia] y el OE8.
La documentación de la API se mantiene en Postman. Las métricas evaluadas sobre el conjunto de prueba se reportan en el capítulo~[§cap:resultados].

### Despliegue

El control de versiones se lleva en GitHub, con ramas de feature y revisión antes de integrar a la rama principal. El pipeline de CI/CD
corre en GitHub Actions: ejecuta las pruebas automatizadas en cada pull request y, al integrarse a la rama principal, construye una imagen Docker del backend que se despliega automáticamente a la instancia de Coolify
–computadora propia durante el desarrollo, VPS durante el piloto– mediante un webhook de despliegue. El monitoreo del MVP se limita a los paneles nativos de Coolify (estado del contenedor, uso de recursos) y a los paneles propios de LiveKit Cloud, Supabase y Upstash; un sistema de monitoreo unificado, como Grafana, queda fuera del alcance del MVP.

# Capítulo 5: Justificación económica

## Alcance y método de la evaluación

Este capítulo presenta los beneficios tangibles e intangibles que se obtendrían con la puesta en marcha de Tinku, evaluados sobre un horizonte de cinco años mediante un análisis costo-beneficio. La secuencia metodológica es la siguiente: primero se cuantifican los costos (inversión inicial y gastos recurrentes post-lanzamiento), luego los beneficios (el ingreso por comisión y los ahorros e intangibles asociados), con ambos se construye el flujo de fondos proyectado y, finalmente, sobre ese mismo flujo se calculan los cuatro indicadores de evaluación: período de repago, repago descontado, VAN y TIR.

Los cuatro indicadores responden preguntas distintas y se leen en conjunto, tal como resume la tabla~[§tab:que-mide]. Ninguno reemplaza a los otros: el repago mide liquidez y exposición al riesgo, el VAN
mide creación de valor y la TIR mide rendimiento.

**Tabla:** Qué mide cada técnica de evaluación

| **Técnica** | **Pregunta que responde** | **Unidad** | **Tasa de descuento** |
| --- | --- | --- | --- |
| Período de repago | ¿Cuándo recupero la inversión? | años | No la utiliza |
| Repago descontado | ¿Cuándo la recupero en dinero de hoy? | años | La aplica |
| VAN | ¿Cuánto valor crea el proyecto? | USD | Es un dato de entrada |
| TIR | ¿Qué rendimiento anual rinde? | % anual | Es el resultado |

Todos los cálculos se apoyan en un modelo financiero parametrizado construido en planilla de cálculo, en el cual los indicadores están formulados con las funciones nativas ‘NPV‘ e ‘IRR‘. Esto permite que al modificar cualquier supuesto de entrada —el ticket promedio, la comisión, las horas de desarrollo o el volumen de sesiones— los tres escenarios, el VAN y la TIR se recalculen de forma inmediata. El modelo se describe en el anexo~[§anx:modelo-financiero].

## Justificación institucional, legal, ambiental y social

El desarrollo de Tinku se fundamenta en un impacto transversal comprobable:

- **Justificación social:** el proyecto busca democratizar el acceso al apoyo escolar, eliminando las barreras geográficas que afectan especialmente a estudiantes en comunidades rurales o del interior del país. A su vez, propone formalizar el mercado de tutorías particulares, el cual opera mayormente en la informalidad.
- **Justificación legal e impositiva:** el modelo de contratación se apoya en el Código Civil y Comercial de la
          Nación (artículos 25, 26, 682 y 690), exigiendo que la cuenta pagadora pertenezca siempre a un adulto responsable para resguardar patrimonialmente a los menores. En materia impositiva, la retención de fondos vía MercadoPago Marketplace funciona como un mecanismo de formalización tributaria (similar a los esquemas de retención de AFIP para plataformas digitales), mitigando además los riesgos de relación de dependencia laboral encubierta. Asimismo, la plataforma aplica el principio de minimización de datos para cumplir estrictamente con la Ley de
          Protección de Datos Personales (Ley 25.326).
- **Justificación institucional:** Tinku se desarrolla como el proyecto final de la carrera de Ingeniería en
          Informática, demostrando la aplicación de tecnologías de vanguardia (IA y WebRTC) para resolver una problemática concreta del sistema educativo argentino.
- **Justificación ambiental:** al centralizar el apoyo académico en un ecosistema digital y virtual, se elimina la necesidad de desplazamiento físico de alumnos y tutores, reduciendo la huella de carbono asociada al transporte. A nivel de infraestructura tecnológica, se prioriza la eficiencia mediante servicios gestionados de bajo consumo, evitando el aprovisionamiento permanente de servidores dedicados.

## Modelo de monetización y alternativas descartadas

El ingreso principal de Tinku es una **comisión de plataforma del 27 % sobre el precio de cada sesión**, descontada exclusivamente del pago que recibe el tutor. Se complementa con el margen del resumen automático, que se ofrece como adicional opcional
(sección~[§sec:resumen-opcional]). El estudiante abona el precio final fijado por el docente, sin cargos de servicio adicionales visibles, con un **precio mínimo de USD 4 por hora** (sección~[§sec:precio-sesion]). Se excluyen explícitamente vías de ingreso como la publicidad, la venta de datos o las suscripciones premium durante la etapa de MVP.

Durante el diseño del modelo de negocio se evaluaron y descartaron dos metodologías alternativas de intermediación:

- **Suscripción mensual al estudiante (modelo Superprof):** se descartó porque la imposición de una barrera de entrada fija contradice el objetivo principal de reducir la fricción económica para familias de bajo poder adquisitivo.
          Adicionalmente, no genera un ingreso proporcional al valor efectivo entregado en cada sesión.
- **Comisión de alta retención en el extremo superior del mercado (33 %):** se descartó replicar las bandas tarifarias máximas de Preply. Una comisión percibida como excesiva incentiva la desintermediación —acuerdos de pago por fuera de la plataforma tras el primer contacto— lo cual erosiona los ingresos y vulnera el modelo de confianza diseñado.

### Calibración de la comisión

Una primera formulación del modelo adoptó una comisión del 15 %, valor que posiciona a la plataforma por debajo de toda la banda de Preply
(18 % a 33 %). Al incorporar los costos financieros de la pasarela de pago, esa comisión no alcanzaba a cubrir los costos fijos de operación en ninguno de los escenarios. La comisión se recalibró al 27 %, valor que continúa dentro de la banda de mercado y por debajo de su extremo superior, descartado por el riesgo de desintermediación ya señalado.

Con el resto de los supuestos del modelo, el escenario base alcanza un
VAN nulo con una comisión del 23,4 %. El 27 % adoptado deja, por lo tanto, un margen de 3,6 puntos porcentuales dentro de la banda de mercado (sección~[§sec:sensibilidad]).

### Unidad de cobro y duración de las sesiones

La plataforma admite sesiones de duración variable, con un mínimo facturable de 30 minutos y una duración estándar de 60 minutos. Asumiendo que un 30 % de las sesiones utiliza el mínimo de 30 minutos, la duración promedio ponderada resulta:

    d = 60 (1 - 0{,}30) + 30 0{,}30 = 51  minutos.

### Precio de la sesión

El precio lo fija cada tutor, pero la plataforma impone un **piso de USD 4 por hora**. El piso evita que la competencia entre tutores reduzca el precio hasta que la comisión deje de cubrir los costos de operación. Según la encuesta de validación, el 57,8 % de los encuestados pagaría ese valor o uno superior (apéndice~[§apx:encuesta]).

Para el modelo se adopta como precio promedio la **mediana de la disposición a pagar relevada en la encuesta: USD 4,56 por hora**. Los montos, relevados en pesos, se convierten con la cotización vendedora del
Banco de la Nación Argentina al cierre de la encuesta, $1.535 por dólar
[bna2026]. Aplicado a la duración promedio de la ecuación~[§eq:duracion], el ticket promedio por sesión resulta:

    T = 4{,}56 51{60} USD~3{,88}.

*Contrastar con la tarifa promedio por hora que publica
Superprof para apoyo escolar en Argentina (verificar en el sitio y citar).*

Una formulación anterior del modelo suponía un ticket de USD~7 por sesión, equivalente a USD~8,24 por hora. Ese valor no tenía respaldo empírico y resultó casi el doble de la mediana relevada: solo el
31,8 % de los encuestados declaró pagar USD~5,86 por hora o más, y el rango superior de la encuesta es abierto, por lo que no permite saber cuántos pagarían USD~8,24. Se reemplaza, por lo tanto, por el valor respaldado por la evidencia.

### Resumen automático como adicional opcional

El resumen automático de la sesión (OE6) requiere grabar el audio de la clase y procesarlo con un LLM. Ambos costos escalan con la duración real del audio y no con la cantidad de sesiones:

- **Grabación del audio.** La captura de solo audio en
          LiveKit Cloud (*egress*) cuesta USD~0{,005} por minuto
          [livekit2026], es decir, $51 0{,}005 =
          USD~0{,255}$ por sesión promedio.
- **Transcripción y resumen.** Se adopta Gemini 3.5
          Flash-Lite, que acepta audio como entrada directa a
          USD~0{,30} por millón de tokens [gemini2026]. El audio se tokeniza a 32 tokens por segundo [geminitokens2026]: una sesión de 51 minutos equivale a 97.920 tokens de entrada
          (USD~0{,0294}), a los que se suman unos 1.500 tokens de salida
          (USD~0{,0038}). El costo resulta de USD~0{,033} por sesión.

El costo total del resumen asciende entonces a USD~0{,288} por sesión, equivalente al 35 % del margen de la comisión. Absorberlo dentro de la comisión deterioraría los indicadores. Por ese motivo, el resumen se ofrece como un **adicional opcional** que el alumno o su adulto responsable activa en cada reserva. Cubriendo además la comisión de la pasarela de pago, su precio mínimo es $0{,}288 / (1 - 0{,}0604) =
USD~0{,31}$; se fija en USD~0{,50}.

Se supone que el 40 % de las sesiones contrata el adicional, supuesto que se declara como tal: la encuesta midió cuánto se valora la función, pero no cuánto se pagaría por ella. Además, en el MVP el adicional no se ofrece en sesiones con menores, por el riesgo de privacidad que analiza el capítulo~[§cap:riesgos], por lo que la adopción debe verificarse en el piloto. El aporte al margen de una sesión promedio resulta:

    0{,}40 [ 0{,}50 (1 - 0{,}0604) - 0{,}288 ]
    USD~0{,0727}.

La elección del modelo responde al costo. Gemini 2.0 Flash, uno de los dos candidatos considerados originalmente, fue dado de baja el 1 de junio de 2026 [geminidep2026]. Su reemplazo recomendado, Gemini 3.6
Flash, costaría USD~0{,079} por sesión, con un precio que se duplica a partir de enero de 2027 [gemini2026]. La encuesta respalda el carácter opcional sin resignar valor: el resumen automático fue la segunda función más valorada, mencionada por el 56,8 % de los encuestados (apéndice~[§apx:encuesta]).

## Estructura de costos

### Inversión inicial

La evaluación responde a la decisión que Tinku enfrenta hoy: si conviene lanzar comercialmente el MVP, que ya se encuentra construido (anexo~[§anx:repositorios]). Por ese motivo, la inversión del Año 0 comprende únicamente las erogaciones *incrementales*
necesarias para completarlo y ponerlo en producción. El esfuerzo ya invertido en construirlo es un **costo hundido**: no puede recuperarse ni depende de la decisión que se evalúa, por lo que no integra el flujo de fondos, conforme al criterio estándar de evaluación de proyectos. Se informa, no obstante, en la sección~[§sec:costo-mvp]. La tabla~[§tab:inversion] presenta el desglose.

**Tabla:** Inversión incremental del lanzamiento (en USD)

| **Categoría** | **Concepto** | **Cant.** | **Valor unit.** | **Total** |
| --- | --- | --- | --- | --- |
| Personal | Senior — desarrollo pendiente (36 tareas) | 27,3 hs | 50 | 1.366 |
| Personal | Senior — soporte y correcciones del piloto | 32 hs | 50 | 1.600 |
| Personal | Junior — UAT del piloto | 20 hs | 15 | 300 |
| Infraestructura | Cloud del piloto (capas gratuitas) | 1 mes | 0 | 0 |
| Administrativo | Registro de dominio | 1 año | 3 | 3 |
| Legal | Asesoría en TyC, privacidad y antecedentes | único | 800 | 800 |
| Riesgo | Contingencia (10 % del trabajo) | único | 327 | 327 |
| **Total inversión incremental** | **4.395** |  |  |  |

Cada partida surge de un cálculo explícito:

- **Desarrollo pendiente.** Al 22 de septiembre de 2026, el repositorio registra 136 tareas completadas y 32 pendientes, entre ellas la integración del kill-switch en el cliente
          (T-M3-06), la selección dinámica de horarios y la remediación de los hallazgos abiertos de la auditoría técnica
          (capítulo~[§cap:resultados]). A ellas se suman cinco tareas para reincorporar la verificación del CAP a los tutores de menores (capítulo~[§cap:riesgos]) y se descuenta una que queda cancelada, lo que da 36 tareas. El esfuerzo por tarea se toma de la tasa observada en el propio repositorio: 103,2 horas para 136 tareas, es decir, 0,76 horas por tarea
          (sección~[§sec:costo-mvp]). Resultan
          $36 0{,}76 27{,}3$ horas.
- **Piloto.** El piloto con usuarios reales ocupa el
          Sprint~11, de cuatro semanas (capítulo~[§cap:metodologia]).
          Se imputan 8 horas semanales de un perfil senior para soporte y correcciones, y 5 horas semanales de un perfil junior para las pruebas de aceptación.
- **Dominio.** Monto efectivamente pagado por el registro de
          ‘tinku.site‘.
- **Contingencia.** 10 % del trabajo del lanzamiento, para absorber retrabajo y subestimación de las tareas pendientes.

Las tarifas horarias (USD 50 para el perfil senior y USD 15 para el junior) se adoptan como estimación propia basada en valores de mercado para desarrollo remoto en la región, y se declaran como tal. La tasa de
0,76 horas por tarea es un promedio: las tareas pendientes incluyen algunas de las más complejas del sistema. La sección~[§sec:sensibilidad] cuantifica cuánto desvío admite esta estimación antes de comprometer la viabilidad.

### Costo del MVP ya construido

Aunque no integra la evaluación, el esfuerzo invertido en el MVP
se estima por dos vías independientes, con fines informativos.

- **Esfuerzo registrado.** El algoritmo *git-hours*
          [githours] agrupa los commits en sesiones de trabajo: cuenta como trabajado el tiempo entre dos commits separados por menos de 120 minutos y suma 120 minutos por cada sesión nueva.
          Aplicado a los 213 commits del repositorio, registrados entre el
          2 y el 22 de septiembre de 2026, arroja **103,2 horas** en
          31 sesiones.
- **Esfuerzo tradicional.** El modelo COCOMO básico
          [boehm1981], en modo orgánico, estima el esfuerzo como
          $E = 2{,}4 KLOC^{1{,}05}$ personas-mes. Para las
          24.110 líneas de código de producción del repositorio resulta en unas 68 personas-mes, del orden de 10.300 horas.

La diferencia de dos órdenes de magnitud entre ambas estimaciones refleja el uso de herramientas de IA generativa en el desarrollo, según el método descrito en el capítulo~[§cap:metodologia]
(sección~[§sec:desarrollo-ia]) y en la declaración de uso de IA
de este trabajo. Una formulación anterior del modelo valorizaba la construcción completa del producto con un equipo de cuatro perfiles, por 812 horas y USD~25.730; esa cifra no correspondía a la decisión evaluada y se reemplaza por la inversión incremental.

### Costos recurrentes post-lanzamiento

Los costos operativos se proyectan mensualmente y se anualizan para el flujo de fondos. La tabla~[§tab:costos-fijos] muestra su evolución a lo largo del horizonte de evaluación.

**Tabla:** Costos fijos mensuales post-lanzamiento (en USD)

| **Categoría** | **Concepto** | **Año 1** | **Año 2** | **Año 3** | **Año 4** | **Año 5** |
| --- | --- | --- | --- | --- | --- | --- |
| Infraestructura | Base de datos y frontend (Supabase Pro, Vercel Pro) | 45 | 45 | 50 | 55 | 60 |
| Infraestructura | Servidor de aplicación (VPS de 4~GB) | 24 | 24 | 24 | 24 | 24 |
| Infraestructura | Transmisión de video (LiveKit) | 60 | 60 | 65 | 70 | 75 |
| Infraestructura | Asistente conceptual LLM (base) | 55 | 55 | 60 | 65 | 70 |
| Administrativo | Honorarios contables | 150 | 150 | 150 | 150 | 150 |
| Administrativo | Renovación de dominio (.com.ar) | 0,46 | 0,46 | 0,46 | 0,46 | 0,46 |
| Comercial | Adquisición de usuarios | 40 | 50 | 60 | 70 | 80 |
| **Total mensual** | **374,46** | **384,46** | **409,46** | **434,46** | **459,46** |  |
| **Total anual** | **4.494** | **4.614** | **4.914** | **5.214** | **5.514** |  |

Las partidas de infraestructura surgen de las tarifas públicas vigentes de cada proveedor, relevadas en septiembre de 2026:

- **Base de datos y frontend.** Supabase Pro cuesta
          USD~25 mensuales [supabase2026] y Vercel Pro USD~20
          por usuario [vercel2026]. El plan gratuito de Vercel no es una alternativa en operación, porque se limita al uso personal y no comercial; el de Supabase tampoco, porque pausa los proyectos inactivos.
- **Servidor de aplicación.** El backend Spring Boot y el servicio de matching corren en un VPS Basic de
          DigitalOcean de 2 vCPU y 4~GB, a USD~24 mensuales
          [digitalocean2026]. Se descartaron los planes económicos de Hetzner, que no admiten nuevas órdenes y registraron dos aumentos de precio durante 2026 [hetzner2026], y un
          VPS equivalente alojado en Buenos Aires, que cuesta
          USD~40,7 mensuales [lightnode2026].
- **Transmisión de video.** Con el volumen del escenario base del Año 1 (600 sesiones mensuales de 51 minutos y dos participantes), el consumo es de 61.200 minutos de participante, cubiertos por el plan Ship de LiveKit Cloud
          (USD~50 mensuales, 150.000 minutos incluidos). El excedente de transferencia de datos, a USD~0{,12} por GB
          [livekit2026], lleva el costo a un rango de USD~64 a
          USD~86 mensuales según la calidad de video, contra los
          USD~60 proyectados. La diferencia se declara como una sensibilidad del modelo.
- **Caché y tiempo real.** Redis se mantiene en el plan gratuito de Upstash (500.000 comandos mensuales), suficiente para el chat y el *rate limiting* del volumen proyectado; el excedente se factura a USD~0{,20} cada 100.000 comandos
          [upstash2026]. Se trata de un supuesto declarado.
- **Dominio.** Para la operación comercial se adopta un dominio ‘.com.ar‘, cuya renovación anual cuesta $8.500
          [nic2026], es decir, USD~5,54 al tipo de cambio de referencia o USD~0,46 mensuales.

Dos decisiones de este cuadro merecen justificación explícita:

- **Ausencia de equipo de soporte rentado.** El modelo no incorpora personal técnico contratado dentro de los costos fijos durante los cinco años proyectados. Un análisis de sensibilidad sobre esta variable mostró que, con el volumen de sesiones proyectado, sostener un equipo de soporte
          —aun escalonando su incorporación— vuelve el proyecto inviable en los tres escenarios. El mantenimiento correctivo y evolutivo queda a cargo del equipo fundador. La incorporación de soporte pago se difiere hasta que el volumen efectivo de sesiones lo justifique, lo cual constituye una restricción operativa declarada del modelo y no un supuesto de costo cero.
- **Presupuesto de adquisición de usuarios.** Se incorpora una partida de marketing, modesta pero creciente, dado que la proyección de demanda no se sostiene por sí sola: un modelo que proyecta captación de usuarios sin asignar presupuesto de adquisición incurre en una inconsistencia interna.

### Costos variables por transacción

Además de los costos fijos, cada sesión concretada genera costos variables que se deducen del ingreso bruto. La tabla~[§tab:unit-economics] presenta la economía unitaria completa de una sesión promedio.

**Tabla:** Economía unitaria por sesión (en USD)

| **Concepto** | **Cálculo** | **Valor** |
| --- | --- | --- |
| Ticket promedio de la sesión | Mediana de la encuesta, ec.~[§eq:ticket] | 3,8800 |
| Comisión bruta de plataforma | Ticket $$ 27 % | 1,0476 |
| Costo de pasarela de pago | Ticket $$ 6,04 % | $-0{,}2344$ |
| Margen del resumen opcional | Ec.~[§eq:adicional] | 0,0727 |
| **Margen neto por sesión** |  | **0,8859** |

El costo de la pasarela de pago corresponde a la comisión de procesamiento de MercadoPago con dinero disponible de forma inmediata, incrementada por el IVA que grava dicha comisión. Es un costo real de cobranza y resulta conceptualmente distinto de la comisión de plataforma, que constituye el ingreso del proyecto. Su omisión en una formulación preliminar del modelo sobrestimaba el margen neto en aproximadamente un 26 %. El resumen automático aporta solo su margen, porque su costo lo cubre el precio del adicional
(sección~[§sec:resumen-opcional]).

Se reconoce además la existencia de fricción financiera adicional
—retenciones de ingresos brutos, percepciones impositivas y contracargos— cuya magnitud depende de la jurisdicción y del comportamiento efectivo de los usuarios. No se cuantifica en el modelo base y se trata como una sensibilidad adicional sobre el margen, lo cual se declara como una restricción del análisis.

## Beneficios del proyecto

El análisis costo-beneficio contempla tanto los beneficios directamente monetizables como aquellos que, sin traducirse en flujo de caja, inciden sobre la viabilidad del proyecto. La tabla~[§tab:beneficios] los sistematiza.

**Tabla:** Beneficios tangibles e intangibles del proyecto

| **Tipo** | **Beneficio** | **Cuantificación** |
| --- | --- | --- |
| Tangible | Ingreso por comisión y adicional de resumen sobre sesiones concretadas | USD~0,8859 de margen neto por sesión, incluido el adicional de resumen; es el único beneficio que integra el flujo |
| Tangible | Ahorro en desplazamiento para alumnos y tutores | No se imputa al flujo del proyecto; es un excedente que capta el usuario |
| Intangible | Formalización tributaria del mercado de tutorías | Reduce exposición regulatoria y habilita escalabilidad institucional |
| Intangible | Trazabilidad y seguridad en la interacción con menores | Barrera de entrada frente a competidores informales |
| Intangible | Acceso a apoyo escolar en zonas sin oferta presencial | Impacto social; amplía el mercado direccionable |

Únicamente el primer beneficio se incorpora al flujo de fondos. Los ahorros que captura el usuario final y los beneficios intangibles se declaran pero no se monetizan, con el fin de no sobrestimar la rentabilidad del proyecto.

## Estimación de la demanda

La variable que tracciona los ingresos no es la cantidad de usuarios registrados sino el **volumen anual de sesiones concretadas**. Un usuario registrado que no reserva clases no genera ingreso alguno. La proyección se construye, por lo tanto, sobre alumnos activos —aquellos que efectivamente reservan— y una frecuencia de uso:

    Sesiones anuales = Alumnos activos Clases por alumno por mes 12.

Se adopta una frecuencia de tres clases por alumno por mes, equivalente a menos de una clase semanal, criterio deliberadamente conservador para un servicio de apoyo escolar.

La proyección de alumnos activos, presentada en la tabla~[§tab:demanda], se define como un dato de entrada por año y por escenario, y no como una curva de crecimiento compuesto. Esta decisión metodológica es deliberada: las proyecciones estrictamente lineales o exponenciales constituyen un error frecuente en la evaluación de proyectos, ya que ignoran la estacionalidad del ciclo lectivo, la rotación de cohortes y el efecto acotado en el tiempo de las campañas de captación. Los valores adoptados oscilan entre años, reflejando ese comportamiento.

**Tabla:** Proyección de alumnos activos y sesiones anuales por escenario

| **Escenario** | **Métrica** | **Año 1** | **Año 2** | **Año 3** | **Año 4** | **Año 5** |
| --- | --- | --- | --- | --- | --- | --- |
| Pesimista | Alumnos activos | 130 | 110 | 160 | 140 | 190 |
|  | Sesiones anuales | 4.680 | 3.960 | 5.760 | 5.040 | 6.840 |
|  | Sesiones anuales | 7.200 | 9.360 | 7.560 | 10.440 | 9.000 |
|  | Sesiones anuales | 10.080 | 15.120 | 12.240 | 17.280 | 14.400 |

El escenario pesimista refleja una plataforma que no logra consolidar retención: retrocede en el Año 2 y sus repuntes posteriores dependen de campañas puntuales. El escenario base describe una operación que oscila en una banda de entre 200 y 290 alumnos activos sin una tendencia sostenida de crecimiento. El optimista contempla mayor volatilidad, con picos apalancados por alianzas institucionales seguidos de caídas estacionales.

## Tasa de descuento

La tasa de descuento expresa el rendimiento mínimo que exigiría un inversor por inmovilizar capital en Tinku en lugar de destinarlo a una alternativa de riesgo comparable. Como el proyecto no toma deuda, la tasa coincide con el costo del capital propio. Se construye por acumulación, con el método de [damodaranctry2026] para mercados emergentes: al rendimiento de un activo libre de riesgo se le suma la prima de riesgo del mercado accionario, ajustada por el riesgo del sector, y la prima de riesgo país:

    r = r_f + ERP + CRP.

**Tabla:** Construcción de la tasa de descuento

| **Componente** | **Valor** | **Fuente** |  |
| --- | --- | --- | --- |
| Tasa libre de riesgo ($r_f$): bono del Tesoro de EE. UU. a 10 años, al 9 de septiembre de 2026 | 4,83 % | [fred2026] |  |
| Beta desapalancado ($$) del sector Software (Internet) | 1,55 | [damodaranbeta2026] |  |
| Prima de riesgo de un mercado maduro ($ERP$), implícita en el S | P~500 | 4,23 % | [damodaranerp2026] |
| Prima de riesgo país de Argentina ($CRP$), calificación Caa1 | 9,71 % | [damodaranctry2026] |  |
| **Tasa de descuento** $r = 4{,}83 % + 1{,}55 4{,}23 % + 9{,}71 %$ | **21,10 %** |  |  |

Cada componente responde a una decisión explícita:

- **Moneda.** Todo el modelo está expresado en dólares, por lo que la tasa libre de riesgo es la de un bono en dólares y no incorpora la inflación en pesos. La fecha coincide con la del tipo de cambio de referencia del trabajo.
- **Sector.** Tinku es un marketplace digital, por lo que se adopta el beta de Software (Internet) y no el de
          Educación (0,66), cuyas empresas son mayormente instituciones educativas. Es además la opción más conservadora.
- **Apalancamiento.** Se usa el beta desapalancado porque el proyecto se financia íntegramente con capital propio.
- **Riesgo país.** La prima de [damodaranctry2026] surge del diferencial de incumplimiento asociado a la calificación soberana, ajustado por la mayor volatilidad del mercado accionario frente al de bonos.

La tasa resultante, del **21,10 % anual en dólares**, reemplaza al
15 % adoptado en una formulación anterior del modelo, que carecía de fuentes. La sensibilidad de los resultados frente a esta elección se examina en la sección~[§sec:sensibilidad].

## Flujo de fondos proyectado

El flujo de fondos cruza los ingresos derivados del volumen de sesiones contra los costos fijos anuales, imputando la inversión inicial íntegramente en el Año 0. Los ingresos netos de cada año se obtienen multiplicando las sesiones anuales por el margen neto unitario de
USD~0,8859. La tabla~[§tab:flujo-caja] presenta el flujo del escenario base.

**Tabla:** Flujo de fondos proyectado — escenario base (en USD)

| **Concepto** | **Año 0** | **Año 1** | **Año 2** | **Año 3** | **Año 4** | **Año 5** |
| --- | --- | --- | --- | --- | --- | --- |
| Sesiones anuales | 0 | 7.200 | 9.360 | 7.560 | 10.440 | 9.000 |
| Ingreso neto | 0 | 6.379 | 8.292 | 6.698 | 9.249 | 7.973 |
| Costos fijos anuales | 0 | $-4.494$ | $-4.614$ | $-4.914$ | $-5.214$ | $-5.514$ |
| Inversión incremental | $-4.395$ | 0 | 0 | 0 | 0 | 0 |
| **Flujo neto** | **$-4.395$** | **1.885** | **3.679** | **1.784** | **4.035** | **2.460** |
| **Flujo acumulado** | **$-4.395$** | **$-2.510$** | **1.168** | **2.952** | **6.988** | **9.447** |
| **Flujo descontado** | **$-4.395$** | **1.557** | **2.509** | **1.005** | **1.877** | **945** |
| **Acum. descontado** | **$-4.395$** | **$-2.839$** | **$-330$** | **674** | **2.551** | **3.496** |

La operación genera flujos positivos todos los años. El flujo acumulado nominal cambia de signo durante el Año 2 y el descontado durante el
Año 3; al cierre del Año 5 alcanzan USD~9.447 nominales y
USD~3.496 en dinero de hoy.

## Evaluación financiera

### Formulación de los indicadores

El VAN es la suma de todos los flujos del proyecto traídos al presente, incluida la inversión inicial:

    VAN = -I_0 + _{t=1}^{n} FC_t{(1 + r)^{t}},

donde $I_0$ es la inversión inicial, $FC_t$ el flujo de fondos neto del período $t$, $r$ la tasa de descuento y $n$ la cantidad de períodos. El criterio de decisión es directo: si $VAN 0$ el proyecto se acepta, porque rinde por encima de la tasa exigida; si
$VAN < 0$ se rechaza, porque destruye valor frente a la alternativa.

La TIR es el caso particular en que la tasa de corte hace que el
VAN sea exactamente cero:

    0 = -I_0 + _{t=1}^{n} FC_t{(1 + TIR)^{t}}.

No admite despeje algebraico directo, por lo que se resuelve por iteración numérica. Si la tasa de corte es menor o igual a la TIR, el proyecto se acepta; si la supera, se rechaza o se renegocian sus condiciones.

El período de repago es el lapso necesario para que el flujo acumulado alcance el valor cero. Se calcula de forma fraccionaria, interpolando dentro del año en que se produce el cambio de signo:

    Repago = m - 1 + | FA_{m-1 |}{FC_{m}},

donde $FA_{m-1}$ es el flujo acumulado del último período negativo y
$FC_m$ el flujo del período que revierte el signo. El repago descontado aplica la misma expresión sobre los flujos ya descontados.

### Resultados

La tabla~[§tab:indicadores-financieros] resume los cuatro indicadores calculados sobre el flujo de fondos de cada escenario.

**Tabla:** Indicadores financieros por escenario

| **Escenario** | **VAN (USD)** | **TIR** | **Repago simple** | **Repago descontado** |
| --- | --- | --- | --- | --- |
| Pesimista | $-5.468$ | $-52{,}86$ % | No recupera en 5 años | No recupera en 5 años |
| Base | 3.496 | 52{,}06 % | 1,68 años | 2,33 años |
| Optimista | 16.072 | 134{,}20 % | 0,99 años | 1,12 años |

La lectura de cada indicador es la siguiente:

- **VAN:** es positivo en los escenarios base
          (USD~3.496) y optimista (USD~16.072), por lo que en ambos el proyecto crea valor por encima de la tasa exigida del
          21,10 % y, conforme al criterio de decisión, se acepta. En el escenario pesimista es negativo (USD~-5.468).
- **TIR:** en el escenario base es del 52,06 %, más del doble de la tasa de corte. La magnitud se explica por el tamaño reducido de la inversión incremental frente a los flujos operativos, y debe leerse junto con el VAN: en términos absolutos, el valor creado es moderado.
- **Período de repago:** la inversión nominal se recupera a los 1,68 años en el escenario base y antes del cierre del primer año en el optimista.
- **Repago descontado:** medido en dinero de hoy, el escenario base recupera la inversión a los 2,33 años. El pesimista no la recupera dentro del horizonte.

## Análisis de sensibilidad

El análisis de sensibilidad identifica, para cada variable y manteniendo constante el resto de los supuestos, el valor que anula el VAN del escenario base. La distancia entre el valor adoptado y el de equilibrio mide el margen de seguridad del proyecto frente a un error en esa variable. La tabla~[§tab:sensibilidad] resume el resultado.

**Tabla:** Valor de cada variable que anula el van

     del escenario base

| **Variable** | **Valor adoptado** | **Valor de equilibrio** | **Lectura** |
| --- | --- | --- | --- |
| Inversión incremental | USD~4.395 | USD~7.891 | Admite unas 64 horas senior más de desarrollo pendiente, más de tres veces lo estimado |
| Volumen de sesiones | 100 % | 84,2 % | Admite una caída del 16 % de la demanda proyectada |
| Precio por hora | USD~4,56 | USD~3,78 | Por debajo del piso de USD~4 por hora que fija la plataforma |
| Comisión de plataforma | 27 % | 23,4 % | Dentro de la banda de mercado (18 % a 33 %) |
| Tasa de descuento | 21,10 % | 52,06 % | Coincide con la TIR |

Dos lecturas se desprenden de la tabla. La primera: el **piso de precio de USD~4 por hora** funciona como un resguardo del modelo, ya que el equilibrio del escenario base se ubica por debajo de ese valor. La segunda: la estimación del desarrollo pendiente, cuyo cálculo se apoya en un promedio histórico, puede subestimarse más de tres veces sin que el proyecto deje de convenir.

- **Punto de equilibrio operativo.** Dividiendo los costos fijos anuales por el margen neto unitario, en el Año 1 se requieren $4.494 / 0{,}8859 5.072$ sesiones anuales para cubrir los costos fijos, y en el Año 5 aproximadamente 6.224.
          El escenario base supera ese umbral todos los años; el pesimista no lo alcanza en tres de los cinco.
- **Tasa de descuento.** Con la tasa del 15 % de la formulación anterior, el VAN del escenario base sería de
          USD~4.729. La construcción de la tasa con fuentes reduce el valor creado, pero no altera la decisión.
- **Estructura de costos fijos.** La incorporación de un equipo de soporte rentado —evaluada en una formulación previa del modelo con perfiles junior, mid y senior incorporados de forma escalonada— torna negativo el VAN en los tres escenarios. La operación con equipo fundador no es una preferencia sino una condición de viabilidad en esta etapa.

## Política de reembolsos y su costo real

Todo reembolso al estudiante se ejecuta de manera total a través de la
API de MercadoPago, nunca de forma parcial. Esta política tiene un costo real de cero para Tinku, ya que la pasarela reintegra su propia comisión de procesamiento junto con los fondos, evitando saldos negativos. Además, previene riesgos legales de retención indebida frente a la Ley de Defensa del Consumidor y reduce significativamente la exposición de la plataforma a contracargos.

La única excepción es el adicional de resumen
(sección~[§sec:resumen-opcional]): si el resumen no puede generarse, se reembolsa solo el monto del adicional, de $770, porque la sesión se dictó y su precio no corresponde devolverlo. El consentimiento para grabar el audio, condición del adicional, forma parte de los términos y condiciones: el alumno lo acepta de forma explícita al contratarlo y el tutor, al registrarse.

## Conclusión de la evaluación económica

El lanzamiento comercial de Tinku **se justifica económicamente**. En el escenario base, los cuatro indicadores apuntan en la misma dirección: el VAN es positivo (USD~3.496), la
TIR (52,06 %) supera ampliamente la tasa de corte del 21,10 % y la inversión se recupera, aun medida en dinero de hoy, en poco más de dos años. El escenario optimista confirma la conclusión con holgura.

El resultado descansa sobre tres bases verificables. El precio surge de la mediana de disposición a pagar relevada en la encuesta, y no de un supuesto. La inversión se limita a lo necesario para completar y lanzar un MVP que ya existe. Y la tasa de descuento se construye con fuentes públicas e incorpora el riesgo país de Argentina.

El escenario pesimista, en cambio, no resulta viable (VAN de
USD~-5.468): con una demanda que no logra consolidarse, la operación no cubre sus costos fijos en tres de los cinco años. De ello se desprenden las condiciones de viabilidad del proyecto:

- **Sostener un volumen mínimo de aproximadamente 5.100
          sesiones anuales**, umbral por debajo del cual la operación no cubre sus costos fijos.
- **Mantener el piso de precio de USD~4 por hora**, que se ubica por encima del precio de equilibrio del escenario base.
- **Operar sin equipo de soporte rentado** durante el horizonte evaluado, difiriendo esa incorporación hasta que el volumen efectivo la justifique.

Que el escenario pesimista no resulte viable no invalida el proyecto, sino que delimita el terreno en que debe moverse. Ante una tracción inferior a la proyectada, las alternativas pasan por revisar el modelo de negocio: validar un segmento de mayor precio, como la preparación para exámenes de ingreso universitario; incorporar clases grupales que eleven el ingreso por hora de tutor, o explorar acuerdos institucionales que aporten volumen agregado. El análisis de riesgos del capítulo siguiente retoma estas contingencias.

# Capítulo 6: Análisis de riesgos

## Enfoque y criterios

Un riesgo es un evento incierto que, de ocurrir, afecta al menos a uno de los objetivos del proyecto; a diferencia de un problema, todavía no ocurrió y admite decisiones anticipadas [pmi2021]. Cada riesgo de este capítulo se formula como “debido a [causa], podría ocurrir
[evento], lo que provocaría [efecto]”, se clasifica por su naturaleza
(alcance, técnico, recursos, terceros, datos o cumplimiento), por su origen (interno, bajo control del proyecto, o externo) y por la etapa en que puede materializarse (antes de arrancar, durante el desarrollo, en el pasaje a producción o en la operación).

La exposición al riesgo se calcula como el producto de la probabilidad y el impacto, ambos en una escala de 1 a 5
(tabla~[§tab:exposicion]). Para este proyecto, las escalas se interpretan de la siguiente manera:

- **Probabilidad.** 1: sin indicios de que ocurra; 3: hay evidencia de que la causa existe; 5: la causa ya está presente y nada la contiene.
- **Impacto.** 1: demora de días sin efecto sobre los objetivos; 3: afecta un objetivo específico o reduce el
          VAN sin volverlo negativo; 5: impide el lanzamiento, vuelve negativo el VAN del escenario base o expone a menores a un daño.

Las respuestas posibles son cuatro: **evitar** (eliminar la causa, cambiando el alcance o la actividad), **mitigar** (reducir la probabilidad o el impacto), **transferir** (trasladar el riesgo a un tercero mejor preparado) y **aceptar** (convivir con él, documentado y con un plan de contingencia).

## Identificación y evaluación

La tabla~[§tab:matriz-riesgos] presenta los quince riesgos identificados, ordenados por exposición descendente. Las fuentes de identificación fueron la encuesta de validación
(apéndice~[§apx:encuesta]), el modelo financiero
(capítulo~[§cap:economica]), el estado del repositorio
(anexo~[§anx:repositorios]) y las condiciones de los proveedores relevadas en el capítulo~[§cap:marco-tecnologico].

**Tabla:** Ubicación de los riesgos en la matriz de exposición (probabilidad $$ impacto)

    {4pt}

|  | **1 Insignif.** | **2 Menor** | **3 Moderado** | **4 Importante** | **5 Severo** |
| --- | --- | --- | --- | --- | --- |
| **5 Muy probable** | | | | | |
| **4 Probable** | | | R-06, R-08 | R-02, R-03 | R-01 |
| **3 Posible** | | R-13, R-14 | R-11 | R-07 | R-04, R-05 |
| **2 Poco probable** | | | R-15 | R-12 | R-09, R-10 |
| **1 Muy improbable** | | | | | |

| **ID** | **Descripción (causa, evento, efecto)** | **Naturaleza (origen)** | **Etapa** | **P** | **I** | **E** | **Respuesta** | **Resp.** | **Contingencia** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-01 | Debido a que el resumen automático envía el audio de la sesión directamente al LLM de un proveedor extranjero, y la anonimización prevista opera sobre texto, podría ocurrir que la voz y los datos personales de menores se transfieran sin anonimizar, lo que provocaría un incumplimiento de la Ley 25.326 y la pérdida de confianza de las familias. | Cumplimiento (interno) | Durante | 4 | 5 | 20 | Evitar: en el MVP el adicional de resumen no se ofrece en sesiones con menores; para adultos, consentimiento explícito previo | Autor | Si se detecta un envío indebido: desactivar el módulo de resumen, solicitar la eliminación al proveedor y notificar a los titulares |
| R-02 | Debido a que solo el 35,2 % de los encuestados prefiere pagar dentro de una plataforma antes que por transferencia, podría ocurrir que alumnos y tutores acuerden las clases por fuera después del primer contacto, lo que provocaría la pérdida de la comisión, principal fuente de ingreso. | Terceros: usuarios (externo) | Operación | 4 | 4 | 16 | Mitigar: escrow, verificación, reputación y resumen solo existen dentro de la plataforma; datos de contacto ocultos hasta la primera reserva | Autor | Si la recompra dentro de la plataforma cae por debajo del 50 %: comisión decreciente por fidelidad del tutor |
| R-03 | Debido a que el capítulo~[§cap:conclusiones] vence el 20 de octubre y el piloto se extiende del 27 de octubre al 27 de noviembre, con 36 tareas pendientes a cargo de un único desarrollador, podría ocurrir que la hipótesis deba responderse sin datos del piloto, lo que provocaría conclusiones sin evidencia suficiente. | Alcance (interno) | Durante | 4 | 4 | 16 | Mitigar: alcance del MVP congelado; pruebas con usuarios reducidas antes del 20 de octubre | Autor | Presentar la respuesta a la hipótesis como preliminar y completarla con el piloto para la entrega final |
| R-04 | Debido a que el escenario pesimista no cubre los costos fijos en tres de los cinco años, podría ocurrir que la demanda no supere las 5.100 sesiones anuales, lo que provocaría que la inversión no se recupere (VAN de USD~-5.468). | Recursos: mercado (externo) | Operación | 3 | 5 | 15 | Mitigar: piso de USD~4 por hora, presupuesto de adquisición y acuerdos institucionales | Autor | Si a los 12 meses el volumen anualizado es menor a 5.100 sesiones: pasar a clases grupales o al segmento de ingreso universitario; si persiste, cierre ordenado |
| R-05 | Debido a que el clasificador del kill-switch no está integrado en el cliente (T-M3-06), podría ocurrir que el piloto incluya sesiones con menores sin la protección prevista, lo que provocaría la exposición de menores a contenido inapropiado. | Técnico (interno) | Pasaje a producción | 3 | 5 | 15 | Evitar: T-M3-06 es criterio de entrada para cualquier sesión con un menor | Autor | Piloto limitado a alumnos mayores de edad |
| R-06 | Debido a que los proveedores de LLM discontinúan modelos y modifican precios (Gemini 2.0 Flash fue dado de baja en junio de 2026 y Gemini 3.6 Flash duplica su precio en enero de 2027), podría ocurrir que el modelo elegido deje de estar disponible o se encarezca, lo que provocaría la interrupción del resumen o la pérdida de su margen. | Terceros (externo) | Operación | 4 | 3 | 12 | Mitigar: el backend accede al proveedor a través de un puerto intercambiable (‘ResumenProveedor‘) | Autor | Cambiar de proveedor y ajustar el precio del adicional; si no es viable, suspenderlo sin afectar el núcleo |
| R-07 | Debido a que solo 9 tutores respondieron la encuesta y el marketplace es bilateral, podría ocurrir que no haya suficientes tutores verificados al iniciar el piloto, lo que provocaría búsquedas sin candidatos e impediría medir la aceptación del matching (I-01). | Recursos: oferta (externo) | Antes de arrancar | 3 | 4 | 12 | Mitigar: reclutar tutores antes del piloto en la comunidad universitaria | Autor | Acotar el piloto a una o dos materias con oferta suficiente |
| R-08 | Debido a que el 90,9 % de las respuestas de la encuesta proviene del AMBA, podría ocurrir que la demanda y el precio del interior difieran de los relevados, lo que provocaría que la hipótesis de reducción de la brecha geográfica quede sin evidencia. | Datos (interno) | Antes de arrancar | 4 | 3 | 12 | Mitigar: reencuesta dirigida al interior y entrevista a docentes de zonas rurales | Autor | Declarar la limitación y acotar el alcance de la conclusión al AMBA |
| R-09 | Debido a que el desarrollo y la operación dependen de una sola persona, podría ocurrir una enfermedad, una sobrecarga o un abandono, lo que provocaría la detención del desarrollo o de la operación. | Recursos (interno) | Operación | 2 | 5 | 10 | Aceptar: el modelo económico no admite un equipo rentado (capítulo~[§cap:economica]); documentación y pruebas reducen la dependencia | Autor | Prórroga ante la cátedra; en operación, pausa sin pérdida de datos y traspaso a partir del repositorio documentado |
| R-10 | Debido a que la verificación de antecedentes depende de la revisión manual del CAP, un documento que presenta el propio tutor, podría ocurrir que un certificado adulterado o evaluado con un criterio incorrecto habilite a un tutor con antecedentes para dar clases a menores, lo que provocaría un daño grave al menor y responsabilidad legal para la plataforma. | Cumplimiento (interno) | Operación | 2 | 5 | 10 | Mitigar: CAP vigente obligatorio para dictar clases a menores, con verificación de la firma digital del Registro Nacional de Reincidencia y criterio de rechazo definido con asesoría legal | Autor y asesoría legal | Suspensión inmediata, preservación de la evidencia y denuncia ante la autoridad |
| R-11 | Debido a que el cobro con MercadoPago solo se probó con usuarios de prueba, dado que el entorno sandbox presenta fallas conocidas en las notificaciones, podría ocurrir que en producción los webhooks lleguen tarde, duplicados o no lleguen, lo que provocaría reservas confirmadas sin cobro o cobros sin reserva. | Técnico: terceros (externo) | Pasaje a producción | 3 | 3 | 9 | Mitigar: procesamiento idempotente de las notificaciones y conciliación periódica contra la API | Autor | Modo bypass (ADR-M5-01) y conciliación manual por el rol de soporte financiero |
| R-12 | Debido a la jurisprudencia laboral sobre repartidores de plataformas de delivery, podría ocurrir que un tutor reclame una relación de dependencia con la plataforma, lo que provocaría costos laborales no previstos. | Cumplimiento (externo) | Operación | 2 | 4 | 8 | Transferir: términos y condiciones redactados por asesoría legal; el tutor fija precio y horarios | Asesoría legal | Defensa legal con los registros de autonomía del tutor |
| R-13 | Debido a que la infraestructura se contrata en dólares a proveedores que pueden ajustar sus tarifas (Hetzner lo hizo dos veces en 2026), podría ocurrir un aumento de los costos fijos, lo que provocaría una reducción del VAN. | Terceros (externo) | Operación | 3 | 2 | 6 | Mitigar: despliegue en contenedores portables entre proveedores | Autor | Migrar de proveedor con la misma configuración de Coolify |
| R-14 | Debido a que el esfuerzo de las 36 tareas pendientes se estima con un promedio histórico de 0,76 horas por tarea, podría ocurrir que las tareas más complejas demanden más tiempo, lo que provocaría un aumento de la inversión y un retraso del piloto. | Recursos (interno) | Durante | 3 | 2 | 6 | Aceptar dentro del margen: el VAN base tolera hasta 64 horas adicionales | Autor | Cubrir el desvío con la contingencia del 10 % y postergar las tareas no críticas (T-M4-12 a T-M4-15) |
| R-15 | Debido a que el backend se migra de la computadora del desarrollador a un VPS antes del piloto, podría ocurrir una falla en el despliegue o en las migraciones de esquema, lo que provocaría una interrupción del servicio al inicio del piloto. | Técnico (interno) | Pasaje a producción | 2 | 3 | 6 | Mitigar: migraciones versionadas con Flyway y despliegue ensayado antes del piloto | Autor | Volver a la imagen Docker anterior y restaurar el último respaldo |

## Tratamiento de los riesgos principales

Los diez primeros riesgos concentran la exposición del proyecto. Su tratamiento se detalla a continuación; el resto se monitorea.

- **R-01, privacidad del audio de menores (20).** La causa está presente en el diseño: el Plan M6 del repositorio prevé anonimizar el texto antes de enviarlo al LLM, pero el proveedor elegido recibe el audio directamente
          (capítulo~[§cap:economica]). Por el impacto, se opta por evitar el riesgo en lugar de mitigarlo: el adicional de resumen queda fuera de las sesiones con menores hasta que exista un paso de transcripción previo a la anonimización. La decisión reduce la adopción esperada del adicional, supuesto que se revisa en la sección~[§sec:supuestos].
- **R-02, desintermediación (16).** Es el riesgo con mejor respaldo empírico: el 34,1 % de los encuestados se mostró en desacuerdo con pagar dentro de una plataforma
          (apéndice~[§apx:encuesta]). La respuesta apunta a que el valor diferencial solo exista dentro de Tinku: las funciones más valoradas en la encuesta —profesores verificados (58 %), resumen automático (56,8 %) y pago seguro (48,9 %)— dependen de que la transacción ocurra en la plataforma.
- **R-03, alcance y cronograma (16).** Corresponde al
          “alcance que nunca cierra” señalado por la cátedra. El alcance del MVP se congela en las 36 tareas pendientes, y cualquier funcionalidad nueva pasa al trabajo futuro.
- **R-04, inviabilidad económica (15).** Surge del escenario pesimista del capítulo~[§cap:economica]. La contingencia define un disparador medible y una decisión: si a los doce meses el volumen anualizado no alcanza el punto de equilibrio operativo, se revisa el modelo de negocio y, si no hay alternativa viable, se cierra la operación de forma ordenada.
          Cancelar a tiempo un proyecto inviable es una decisión de gestión, no un fracaso.
- **R-05, kill-switch sin integrar (15).** El backend del kill-switch está completo, pero el clasificador que corre en el navegador no. La respuesta es evitar: sin esa integración no se habilitan sesiones con menores.
- **R-06, proveedor de LLM (12).** La probabilidad es alta porque ya ocurrió durante el desarrollo: el candidato original fue dado de baja. El impacto es moderado porque el resumen es un adicional y el backend lo aísla detrás de un puerto intercambiable.
- **R-07, oferta de tutores (12).** Es la manifestación del problema de arranque en frío (arranque en frío) descrito en el capítulo~[§cap:marco-teorico].
- **R-08, sesgo geográfico de la encuesta (12).** Afecta directamente a la hipótesis central, que pone el foco en las zonas con escasa oferta de tutores.
- **R-09, dependencia de una persona (10).** Se acepta porque no existe una respuesta alternativa compatible con el proyecto: el análisis económico mostró que un equipo rentado torna negativo el VAN en los tres escenarios. Aceptarlo no equivale a ignorarlo: la documentación de diseño (especificaciones, planes y decisiones de arquitectura) y 455 casos de prueba automatizados permiten que otra persona retome el sistema.
- **R-10, antecedentes de los tutores de menores (10).**
          Una primera versión del sistema exigía el CAP a todos los tutores y se retiró (ADR-M1-02) por dos motivos: la fricción en el registro de tutores, el recurso más escaso de la plataforma
          (R-07), y la necesidad de decidir la descalificación de un tutor por sus antecedentes sin asesoría legal. La verificación se reincorpora acotada: el CAP vigente es obligatorio solo para dictar clases a menores. Así, los tutores que enseñan a adultos se registran sin fricción adicional, y el criterio de rechazo se define con la asesoría legal ya presupuestada
          (capítulo~[§cap:economica]). El riesgo residual es la validez del documento y su evaluación manual.

## Riesgos que cancelan proyectos

La tabla~[§tab:riesgos-fatales] vincula los siete riesgos que la cátedra señala como causas de cancelación con los riesgos identificados.

**Tabla:** Riesgos fatales y su tratamiento en Tinku{

    }

| **Riesgo fatal** | **Situación en Tinku** |
| --- | --- |
| Alcance que no cierra | R-03: alcance congelado en las 36 tareas pendientes |
| Pérdida del proveedor de datos | R-06 y R-11: los servicios de terceros se aíslan detrás de interfaces intercambiables y existe un modo de operación sin cobro real |
| Equipo que se desarma | R-09: aceptado, con documentación y pruebas que permiten el traspaso |
| Tecnología inadecuada | R-05: la tecnología existe y el spike fue exitoso (ADR-M3-01); falta su integración |
| Inviabilidad económica | R-04: viable en los escenarios base y optimista, con disparador de revisión |
| Barrera ética o legal | R-01 se evita; R-10 se mitiga con el CAP obligatorio para dictar clases a menores; R-12 se transfiere |
| Falta de un responsable | El autor es responsable de todos los riesgos internos; los de cumplimiento se comparten con la asesoría legal |

## Oportunidades

El análisis también identificó dos riesgos positivos, que se gestionan buscando que ocurran:

- **O-01.** Debido a que el 56,8 % de los encuestados valoró el resumen automático, podría ocurrir que la adopción del adicional supere el 40 % supuesto, lo que provocaría un margen por sesión mayor al proyectado. Respuesta: explotar, destacando el adicional en el flujo de reserva.
- **O-02.** Debido a que algunas jurisdicciones ya recurren a escuelas mediadas por tecnología con docentes en las ciudades
          [olea], podría ocurrir que una institución educativa o un municipio contrate paquetes de sesiones, lo que provocaría un volumen agregado superior al del escenario optimista. Respuesta: mejorar la probabilidad, presentando el piloto a instituciones del interior.

## Supuestos y restricciones

Los supuestos son condiciones que se dan por ciertas para que el proyecto sea válido; si alguno falla, se convierte en un riesgo. Las restricciones son condiciones impuestas que limitan el tiempo, el costo o el alcance.

**Tabla:** Supuestos del proyecto y riesgo asociado si fallan

| **ID** | **Supuesto** | **Si falla** |
| --- | --- | --- |
| S-01 | Los alumnos activos por año se ubican en la banda del escenario base (200 a 290) | R-04 |
| S-02 | Cada alumno activo toma tres clases por mes | R-04 |
| S-03 | La mediana de disposición a pagar (USD~4,56 por hora) es representativa fuera del AMBA | R-08 |
| S-04 | El 40 % de las sesiones contrata el adicional de resumen; con la exclusión de las sesiones con menores (R-01), el supuesto debe verificarse en el piloto | R-04 |
| S-05 | Las tarifas de los proveedores se mantienen constantes en dólares durante el horizonte | R-13 |
| S-06 | El plan gratuito de Upstash alcanza para el volumen de chat y *rate limiting* | R-13 |
| S-07 | Las tareas pendientes demandan, en promedio, el esfuerzo observado en el repositorio | R-14 |
| S-08 | La mayoría de los pagos se realiza dentro de la plataforma | R-02 |

**Tabla:** Restricciones del proyecto

| **Tipo** | **Restricción** |
| --- | --- |
| Tiempo | Presentación final el 28 de noviembre de 2026, con entregas parciales por capítulo |
| Recursos | Un único desarrollador, con una dedicación de 15 a 20 horas semanales |
| Costo | Entre 0 y 100 USD mensuales durante el desarrollo y el piloto |
| Técnica | Los organismos estatales (RENAPER, Registro Nacional de Reincidencia) no ofrecen API públicas |
| Legal | Ley 25.326 de protección de datos personales; tutores exclusivamente mayores de edad |
| Alcance | PWA sin aplicaciones móviles nativas |

## Seguimiento y continuidad

Los riesgos se revisan en cada Sprint Review (capítulo~[§cap:metodologia]): se actualizan la probabilidad y el impacto, se incorporan los riesgos nuevos y se registran los que se materializaron como problemas. Durante la operación, los disparadores de las contingencias —el volumen anualizado de sesiones para R-04 y la tasa de recompra dentro de la plataforma para R-02— se miden mensualmente.

En cuanto a la pregunta de quién mantiene el sistema una vez finalizado el proyecto académico: el modelo económico prevé que el equipo fundador asuma el mantenimiento correctivo y evolutivo durante los cinco años evaluados, sin personal rentado (capítulo~[§cap:economica]). Si el proyecto no continuara, el cierre se haría de forma ordenada: aviso a los usuarios, reembolso de las reservas pendientes a través de
MercadoPago, y exportación o eliminación de los datos personales conforme a la Ley 25.326.

# Capítulo 7: Presentación de resultados

Este capítulo presenta los resultados del proyecto al 22 de septiembre de 2026: los requerimientos del sistema, su diseño y construcción, las pruebas técnicas, la validación con usuarios y la evaluación económica.
Se informan tanto los resultados favorables como los desfavorables. Las pruebas de aceptación con usuarios reales corresponden al piloto del
Sprint~11 (capítulo~[§cap:metodologia]); sus resultados se incorporarán al finalizarlo, y las secciones afectadas lo indican.

## Requerimientos

### Requerimientos funcionales

Los requerimientos funcionales se especificaron por módulo, antes de implementarse, en las especificaciones del repositorio
(capítulo~[§cap:metodologia], sección~[§sec:desarrollo-ia]). Cada uno tiene un identificador, una descripción y criterios de aceptación expresados como escenarios verificables. La tabla~[§tab:rf] resume los 118 requerimientos por módulo y su estado de implementación.

**Tabla:** Requerimientos funcionales por módulo y estado de implementación

| **Módulo** | **Prefijo** | **RF** | **Estado** |
| --- | --- | --- | --- |
| M1 Identidad y perfiles | FR-ID | 19 | Implementado. Los requerimientos del CAP (FR-ID-021 a 025), retirados por ADR-M1-02, se reincorporan acotados a los tutores de menores |
| M2 Motor de matching | FR-MATCH | 9 | Implementado |
| M3 Aula virtual | FR-AULA | 10 | Implementado en el servidor; falta integrar el clasificador del kill-switch en el cliente (T-M3-06) |
| M4 Reservas y agenda | FR-RES | 20 | Implementado; falta integrar la selección dinámica de horarios en la interfaz |
| M5 Motor de pagos | FR-PAG | 16 | Implementado, con modo de operación sin cobro real (ADR-M5-01) |
| M6 Resumen automático | FR-SUM | 8 | Implementado sin proveedor: no genera resúmenes hasta integrar el LLM |
| M7 Reputación | FR-REP | 12 | Implementado |
| M8 Administración | FR-ADM | 8 | Implementado |
| M9 Denuncias y seguridad | FR-SEC | 16 | Implementado |
| **Total** | **118** |  |  |

La prioridad de cada requerimiento y su criterio de aceptación detallado se encuentran en la especificación del módulo correspondiente
(anexo~[§anx:repositorios]). La verificación funcional con usuarios se traza a los indicadores del capítulo~[§cap:metodologia]
(tabla~[§tab:indicadores]): el matching (M2) a la tasa de aceptación de sugerencias (I-01), el aula virtual (M3) a la calidad percibida (I-02) y a la cobertura geográfica (I-03), y la experiencia completa al NPS (I-04).

### Requerimientos no funcionales

La tabla~[§tab:rnf] presenta los requerimientos no funcionales, que la Constitución del proyecto define como no negociables.

**Tabla:** Requerimientos no funcionales

| **ID** | **Atributo** | **Umbral medible** | **Estado** |
| --- | --- | --- | --- |
| RNF-01 | Disponibilidad | 95 % mensual durante el piloto | A medir en el piloto |
| RNF-02 | Seguridad | TLS 1.2 o superior; contraseñas con bcrypt o argon2; registro de auditoría de toda acción de administración | Implementado; con hallazgos abiertos de la auditoría técnica (sección~[§sec:auditoria]) |
| RNF-03 | Privacidad | Cumplimiento de la Ley 25.326, con especial cuidado en los datos de menores | Parcial: ver riesgo R-01 del capítulo~[§cap:riesgos] |
| RNF-04 | Rendimiento | Latencia de videollamada menor a 200~ms; ajuste automático de calidad sin modo degradado visible | A medir en el piloto |
| RNF-05 | Mantenibilidad | Sostenible por uno o dos desarrolladores, sin conocimiento tácito no documentado | Cumplido: especificaciones, planes y registros de decisión versionados |

## Diseño

La arquitectura, el modelo de datos y las decisiones de diseño se documentan en el capítulo~[§cap:marco-tecnologico]. El resultado de esa etapa fue un monolito modular de nueve módulos de dominio, con un único proceso separado para el matching y con los servicios de video, pagos e IA delegados en proveedores externos
(figura~[§fig:arquitectura]).

*Insertar capturas reales de las pantallas principales: búsqueda de tutores, reserva, aula virtual y panel de administración.*

## Construcción e integración

El sistema se construyó con el método dirigido por especificaciones descrito en el capítulo~[§cap:metodologia]. La tabla~[§tab:construccion] resume el resultado medido sobre el repositorio.

**Tabla:** Métricas de construcción al 22 de septiembre de 2026

| **Métrica** | **Valor** |
| --- | --- |
| Líneas de código de producción (Java, TypeScript, SQL y Python) | 24.110 |
| Migraciones de base de datos versionadas | 24 |
| Registros de decisión de arquitectura | 14 |
| Tareas completadas / pendientes | 136 / 32 |
| Commits | 213 |
| Esfuerzo registrado (*git-hours*) | 103,2 horas |

El listado~[§lst:puerto-resumen] muestra un fragmento representativo de la construcción: el puerto que aísla al proveedor de LLM. Su implementación por defecto rechaza toda solicitud (*fail-closed*), de modo que ningún dato sale hacia un modelo externo mientras el proveedor no se integre formalmente. El comentario del propio código registra la tensión entre el envío directo de audio y la anonimización, que el capítulo~[§cap:riesgos] trata como el riesgo R-01.

/**
 * Anonimizacion (FR-SUM-005): transcriptAnonimizado ES lo que se
 * envia [...] el audio crudo no es anonimizable antes de salir,
 * asi que [...] el flujo manda solo el transcript ya limpio.
 */
public interface ResumenProveedor {
    ResumenResultado generarResumen(ResumenRequest request);
}

@Component public class ResumenProveedorFailClosed implements ResumenProveedor {
    @Override public ResumenResultado generarResumen(ResumenRequest request) {
        throw new ResumenProveedorNoConfiguradoException();
    }
}

## Pruebas técnicas

### Pruebas automatizadas

El backend cuenta con 455 casos de prueba unitarios y de integración.
Las pruebas de integración se ejecutan con Testcontainers contra una base PostgreSQL real, e incluyen dos pruebas de extremo a extremo sin simulaciones entre los módulos propios: el flujo principal completo
(alta del adulto responsable y del menor, autorización del tutor, solicitud, reserva, pago, sesión, resumen y calificación) y la rama de seguridad (sesión con un menor, disparo del kill-switch, suspensión, alerta y resolución del administrador). La integración continua ejecuta en cada cambio las pruebas del backend y, en el frontend, el análisis estático y pruebas de extremo a extremo con Playwright; estas últimas todavía simulan la API, lo que la auditoría registró como un hallazgo abierto. El servicio de matching tiene 10 pruebas propias, pero aún no forma parte de la integración continua.

*Cobertura de código medida sobre el backend, contra el umbral del 70 % fijado en el capítulo~[§cap:metodologia*.]

### Auditoría técnica

El 21 de septiembre de 2026 se realizó una auditoría técnica del repositorio completo, que incluyó la ejecución de la suite de pruebas
(383 casos en ese momento, todos exitosos).
*Quién realizó la auditoría y con qué método o herramienta.*
La auditoría registró 36 hallazgos, que se gestionan en un registro con su estado; un hallazgo solo se da por cerrado con un cambio en el código y una prueba de regresión. La tabla~[§tab:auditoria] resume su estado al 22 de septiembre.

**Tabla:** Hallazgos de la auditoría técnica por severidad y estado

| **Severidad** | **Hallazgos** | **Cerrados** | **Abiertos** |
| --- | --- | --- | --- |
| Crítica | 7 | 7 | 0 |
| Alta | 12 | 4 | 8 |
| Media | 13 | 2 | 11 |
| Baja | 4 | 1 | 3 |
| **Total** | **36** | **14** | **22** |

Es el resultado más relevante de la etapa de pruebas. La auditoría concluyó que el proceso de desarrollo era disciplinado, pero que la implementación de los controles de seguridad era más débil de lo que la documentación sugería. Los siete hallazgos críticos afectaban directamente a la seguridad del menor y a la confianza, y ya fueron corregidos:

- el kill-switch registraba el corte en la base de datos, pero no cerraba la sala de video, que seguía activa;
- los permisos de acceso a las salas de video otorgaban a los participantes privilegios de administración;
- el DNI del participante se usaba como identificador en la sala de video y se mostraba en pantalla, incluido el de los menores;
- la verificación de identidad por OCR funcionaba con una simulación activada por defecto;
- cualquier participante podía disparar el kill-switch sin aportar evidencia;
- la credencial académica se aprobaba sin que el administrador pudiera ver el documento;
- el enlace de restablecimiento de contraseña se registraba en claro en los logs.

Entre los hallazgos de severidad alta que siguen abiertos se destacan la ausencia de límites de intentos en los endpoints públicos, la falta de una infraestructura real de notificaciones, el servicio de matching expuesto sin autenticación y una restricción de reservas que compara horarios idénticos en lugar de superpuestos. Su remediación forma parte de las tareas pendientes que dimensiona la inversión del capítulo~[§cap:economica].

Dos lecturas surgen de este resultado. La primera: 455 pruebas exitosas no garantizan la ausencia de defectos graves, porque las pruebas verifican lo que se especificó y no lo que se omitió; la revisión independiente detectó fallas que ninguna prueba cubría. La segunda: el desarrollo asistido por IA acelera la construcción, pero no reemplaza la verificación; la auditoría fue el mecanismo que compensó esa diferencia.

### Pruebas de aceptación

Las pruebas de aceptación con usuarios (UAT) se realizan en el piloto del Sprint~11, entre el 27 de octubre y el 27 de noviembre de
2026, y miden los indicadores del capítulo~[§cap:metodologia]. Por los riesgos R-01, R-05 y R-10 del capítulo~[§cap:riesgos], el piloto no incluye sesiones con menores mientras el kill-switch no esté integrado en el cliente y el CAP no se haya reincorporado.

**Tabla:** Indicadores del piloto

| **ID** | **Indicador** | **Umbral** | **Resultado** |
| --- | --- | --- | --- |
| I-01 | Aceptación de las sugerencias del matching | $> 60 %$ | *pendiente* |
| I-02 | Calidad percibida de la sesión (escala 1 a 5) | $4{,}0$ | *pendiente* |
| I-03 | Sesiones entre provincias distintas, con una del interior | $1$ | *pendiente* |
| I-04 | NPS del piloto | positivo | *pendiente* |

## Validación con usuarios

### Encuesta de validación

La encuesta, aplicada a 88 personas entre el 28 de agosto y el 9 de septiembre de 2026, se detalla en el apéndice~[§apx:encuesta]. Sus resultados se contrastan con los supuestos del proyecto:

- **El problema existe.** De quienes tomaron clases particulares, el 70 % encontró al profesor por recomendación, y las dificultades más mencionadas fueron saber si era bueno
          (30 %) y la confianza (20 %). El resultado respalda el diagnóstico de informalidad del capítulo~[§cap:introduccion].
- **La modalidad virtual es aceptada.** El 77,3 % tomaría clases virtuales con un buen profesor, lo que respalda el modelo remoto.
- **La verificación genera confianza.** El 81,8 % confía más en una plataforma con profesores verificados, que además fue la función más valorada (58 %).
- **La IA se valora por su resultado, no como etiqueta.** El 68,2 % querría que la plataforma le recomiende el tutor más adecuado, pero solo el 5,7 % eligió “IA que recomiende profesores” entre las funciones importantes, el último lugar. En cambio, el resumen automático, una función basada en IA descrita por su utilidad, fue la segunda más valorada (56,8 %).
- **El pago dentro de la plataforma no está asegurado.**
          Solo el 35,2 % prefiere pagar dentro de una plataforma antes que por transferencia, y el 34,1 % está en desacuerdo. Es el resultado más desfavorable para el modelo de negocio.
- **El precio es menor al supuesto originalmente.** La mediana de la disposición a pagar es de USD~4,56 por hora, casi la mitad del precio que suponía la primera formulación del modelo económico.

La encuesta tiene limitaciones que acotan estas conclusiones: la muestra no es probabilística, el 90,9 % de las respuestas proviene del AMBA y solo 9 corresponden a tutores.

### Entrevistas a especialistas

*Síntesis de las entrevistas (apéndice~[§apx:entrevista*): fecha, entrevistado, aportes principales y contraste con los resultados de la encuesta.]

### Decisiones derivadas

La tabla~[§tab:feedback-decisiones] traduce los hallazgos en decisiones concretas.

**Tabla:** Traducción de los hallazgos en decisiones de diseño

| **Fuente** | **Hallazgo** | **Decisión** | **Estado** |
| --- | --- | --- | --- |
| Encuesta | Mediana de disposición a pagar de USD~4,56 por hora | Precio del modelo y piso de USD~4 por hora (capítulo~[§cap:economica]) | Aplicado |
| Encuesta | El resumen automático es la segunda función más valorada | Resumen como adicional opcional | Aplicado en el modelo |
| Encuesta | La IA como etiqueta casi no se valora | Presentar las recomendaciones por su resultado, sin destacar la IA | Planificado |
| Encuesta | Solo el 35,2 % prefiere pagar en la plataforma | Mitigación del riesgo R-02: valor exclusivo dentro de la plataforma | Planificado |
| Encuesta | 90,9 % de las respuestas del AMBA | Reencuesta dirigida al interior (riesgo R-08) | Planificado |
| Auditoría | 7 hallazgos críticos de seguridad | Corrección con prueba de regresión | Aplicado |
| Auditoría | 22 hallazgos abiertos | Incorporados a las tareas pendientes y a la inversión | En curso |
| Costos | El audio de la sesión no puede anonimizarse antes del LLM | Sin resumen en sesiones con menores (R-01) | Aplicado en el diseño |

## Contraste con el estado del arte

El capítulo~[§cap:marco-teorico] comparó las plataformas existentes
(tabla~[§tab:comparativa]). Los resultados permiten contrastar la propuesta con ellas en tres ejes:

- **matching.** Las plataformas relevadas ofrecen filtros manuales; Tinku implementa un motor de matching semántico con embeddings semánticos. Su valor para los usuarios queda sujeto al indicador I-01 del piloto.
- **Aula y pagos integrados.** Tinku integra en un mismo flujo la reserva, el aula virtual y el cobro con escrow, algo que las plataformas relevadas resuelven solo de forma parcial.
- **Seguridad del menor.** Es el diferencial más ambicioso y, a la vez, el que la auditoría encontró más débil. Tras corregir los hallazgos críticos, queda pendiente la integración del kill-switch en el cliente y la reincorporación del CAP
          obligatorio para los tutores de menores (riesgo R-10 del capítulo~[§cap:riesgos]).

## Evaluación económica

La evaluación del capítulo~[§cap:economica], con el precio relevado en la encuesta, la inversión incremental y una tasa de descuento del
21,10 %, arroja un VAN de USD~3.496 y una TIR del
52,06 % en el escenario base, con un repago descontado de 2,33 años.
El escenario pesimista no resulta viable (VAN de USD~-5.468). El resultado más relevante del proceso fue que la contrastación del modelo con datos primarios cambió la conclusión dos veces: el precio relevado tornó inviable la primera formulación, y la medición de la inversión real sobre el repositorio la volvió viable.

## Síntesis

**Tabla:** Síntesis de resultados

| **Resultados favorables** | **Resultados desfavorables** |
| --- | --- |
| Nueve módulos implementados, con 455 pruebas automatizadas | 36 hallazgos de auditoría, 22 todavía abiertos |
| Los 7 hallazgos críticos, corregidos con prueba de regresión | Kill-switch sin integrar en el cliente |
| La encuesta respalda el problema, la modalidad virtual y la verificación | Solo el 35,2 % prefiere pagar dentro de la plataforma |
| Escenarios base y optimista económicamente viables | Escenario pesimista no viable |
| Esfuerzo de construcción muy inferior al de un desarrollo tradicional | El resumen automático no funciona todavía y no puede ofrecerse a menores |
| Verificación de identidad, edad y credencial académica de los tutores | CAP para tutores de menores pendiente de reincorporar |

# Capítulo 8: Implicancias, conclusiones y recomendaciones

*Desarrollo del capítulo.*

## *Nombre de la sección*

**Ejemplo.** [Ejemplo: forma de la respuesta a la hipótesis]
La hipótesis planteada en el capítulo~[§cap:introduccion] se responde de manera *afirmativa, con matices*: el sistema alcanzó
*métrica* sobre el umbral definido en el capítulo~[§cap:metodologia], aunque *limitación concreta*.

*Texto.*

**Tabla:** Grado de cumplimiento de los objetivos específicos (ejemplo de estructura)

| **Objetivo** | **Evidencia** | **Grado** | **Observación** |
| --- | --- | --- | --- |
| OE-1 | Capítulo~[§cap:resultados] | Alcanzado | *...* |
| OE-2 | *...* | Parcial | *...* |

# Apéndices

# Encuesta de validación

## Introducción

La encuesta constituye el instrumento cuantitativo de validación de demanda previsto en el capítulo~[§cap:metodologia]. Su objetivo fue contrastar con usuarios potenciales cuatro supuestos del proyecto:

- que la búsqueda de un tutor particular depende hoy de canales informales y presenta fricciones concretas (confianza, calidad, coordinación);
- que alumnos y familias aceptarían la modalidad virtual y valorarían la verificación de los tutores;
- qué funciones de la plataforma se perciben como más importantes, incluidas las basadas en IA;
- la disposición a pagar por una clase de una hora y a hacerlo dentro de la plataforma, supuesto sobre el que descansa el modelo de ingresos del capítulo~[§cap:economica].

## Metodología

- **Instrumento:** cuestionario autoadministrado en línea
          (Tally), de 14 preguntas cerradas: opción única, escala de 1
          (menor acuerdo) a 5 (mayor acuerdo) y selección múltiple.
- **Lógica condicional:** las preguntas 5 a 8 se muestran solo a quienes responden “Sí” en la pregunta 4.
- **Población objetivo:** alumnos, madres y padres de alumnos, y tutores particulares residentes en Argentina.
- **Muestreo:** no probabilístico, por conveniencia.
          *Canal de distribución (grupos de WhatsApp, redes sociales, contactos personales, etc.).*
- **Período de aplicación:** del 28 de agosto al 9 de septiembre de 2026. El 87,5 % de las respuestas se registró en los dos primeros días.
- **Respuestas:** 88 respuestas válidas, sin duplicados por identificador de respondente, por encima del mínimo de 30
          fijado en el capítulo~[§cap:metodologia].
- **Moneda:** el cuestionario relevó los montos en pesos argentinos. Para su análisis se convierten a dólares estadounidenses, moneda de todo el trabajo, con la cotización vendedora del Banco de la Nación Argentina al cierre de la encuesta: $1.535 por dólar el 9 de septiembre de 2026
          [bna2026].
- **Depuración:** un registro indicó no haber tomado clases particulares pero completó dos preguntas del bloque condicional; esas dos respuestas se excluyen del análisis de ese bloque.

## Presentación de la encuesta

*Texto introductorio que vieron las personas participantes
(propósito, anonimato, duración estimada) y, dado que respondieron menores de 18 años, cómo se obtuvo o se solicitó el consentimiento de su adulto responsable.*

## Cuestionario

**Bloque 1 — Perfil.**

- Edad (opción única): Menor de 18 / 18–25 / 26–40 / Más de 40.
- Provincia (opción única).
- Rol (opción única): Alumno / Padre/Madre / Tutor.

**Bloque 2 — Experiencia previa.**

- ¿Tomaste clases particulares durante los últimos años? (Sí / No)
- ¿Cuántas veces? (Una / 2–5 / Más de cinco)
- ¿Cómo encontraste al profesor? (Recomendación / Google /
          Superprof / Redes / Otro)
- ¿Cuánto tardaste? (1–3 días / Una semana / Más de una semana)
- ¿Qué fue lo más difícil? (Encontrar profesor / Saber si era bueno / Comparar precios / Coordinar horarios / Confianza)

**Bloque 3 — Actitudes (escala de 1 a 5).**

- Me gustaría que una plataforma me recomendara automáticamente el tutor más adecuado.
- Tomaría clases virtuales si el profesor fuera bueno.
- Me genera confianza una plataforma con profesores verificados.
- Preferiría pagar dentro de una plataforma antes que por transferencia.

**Bloque 4 — Funciones y precio.**

- ¿Cuáles de estas funciones considera más importantes?
          (selección múltiple): Videollamada integrada / Pago seguro /
          Profesores verificados / Calificaciones / IA que recomiende profesores / Chat / Agenda / Recordatorios / Resumen automático de la clase.
- ¿Cuánto estaría dispuesto a pagar por una clase de una hora?
          (opción única): hasta USD~1,95 / USD~1,95 a USD~3,26 /
          USD~3,26 a USD~5,86 / USD~5,86 o más. Las opciones se presentaron en pesos argentinos: “Hasta $3000”, “$3000 a
          $5000”, “$5000 a $9000” y “$9000 o más”.

## Resultados descriptivos

Esta sección presenta las frecuencias de cada pregunta. Su interpretación y su contraste con los supuestos del proyecto se desarrollan en el capítulo~[§cap:resultados].

### Perfil de la muestra

**Tabla:** Perfil de las personas encuestadas ($n = 88$)

| **Variable** | **Categoría** | **Frecuencia** | **%** |
| --- | --- | --- | --- |
| Rol | Alumno | 50 | 56,8 |
|  | Padre/Madre | 29 | 33,0 |
|  | Tutor | 9 | 10,2 |
|  | 18–25 | 24 | 27,3 |
|  | 26–40 | 23 | 26,1 |
|  | Más de 40 | 30 | 34,1 |
|  | Ciudad Autónoma de Buenos Aires | 8 | 9,1 |
|  | Resto del país (7 provincias) | 8 | 9,1 |

Las respuestas del resto del país corresponden a Corrientes (2),
Córdoba, Chaco, Entre Ríos, San Juan, Santa Cruz y Santa Fe (1 cada una).

### Experiencia previa con clases particulares

El 22,7 % de la muestra (20 personas) tomó clases particulares en los últimos años. La tabla~[§tab:encuesta-experiencia] resume las respuestas de ese subgrupo.

**Tabla:** Experiencia de búsqueda de quienes tomaron clases particulares ($n = 20$)

| **Pregunta** | **Respuesta** | **Frecuencia** | **%** |
| --- | --- | --- | --- |
| Cantidad de veces | Una | 3 | 15,0 |
|  | 2–5 | 7 | 35,0 |
|  | Más de cinco | 10 | 50,0 |
|  | Google | 2 | 10,0 |
|  | Superprof | 1 | 5,0 |
|  | Otro | 3 | 15,0 |
|  | Una semana | 6 | 30,0 |
|  | Más de una semana | 5 | 25,0 |
|  | Confianza | 4 | 20,0 |
|  | Coordinar horarios | 4 | 20,0 |
|  | Comparar precios | 3 | 15,0 |
|  | Encontrar profesor | 3 | 15,0 |

### Actitudes hacia la plataforma

**Tabla:** Grado de acuerdo con las afirmaciones del bloque 3 ($n = 88$, escala 1 a 5)

| **Afirmación** | **Media** | **% 4–5** | **% 3** | **% 1–2** |
| --- | --- | --- | --- | --- |
| Me genera confianza una plataforma con profesores verificados | 4,24 | 81,8 | 6,8 | 11,4 |
| Tomaría clases virtuales si el profesor fuera bueno | 4,15 | 77,3 | 6,8 | 15,9 |
| Me gustaría que una plataforma me recomendara el tutor más adecuado | 4,07 | 68,2 | 22,7 | 9,1 |
| Preferiría pagar dentro de una plataforma antes que por transferencia | 3,07 | 35,2 | 30,7 | 34,1 |

### Funciones valoradas

**Tabla:** Funciones consideradas más importantes (selección múltiple, $n = 88$)

| **Función** | **Menciones** | **% de encuestados** |
| --- | --- | --- |
| Profesores verificados | 51 | 58,0 |
| Resumen automático de la clase | 50 | 56,8 |
| Pago seguro | 43 | 48,9 |
| Videollamada integrada | 42 | 47,7 |
| Agenda | 25 | 28,4 |
| Chat | 21 | 23,9 |
| Recordatorios | 21 | 23,9 |
| Calificaciones | 12 | 13,6 |
| IA que recomiende profesores | 5 | 5,7 |

### Disposición a pagar

**Tabla:** Disposición a pagar por una clase de una hora, en USD ($n = 88$)

| **Rango (USD)** | **Frecuencia** | **%** | **% acumulado** |
| --- | --- | --- | --- |
| Hasta 1,95 | 9 | 10,2 | 10,2 |
| 1,95 a 3,26 | 19 | 21,6 | 31,8 |
| 3,26 a 5,86 | 32 | 36,4 | 68,2 |
| 5,86 o más | 28 | 31,8 | 100,0 |

Interpolando dentro del rango que la contiene, la mediana de la disposición a pagar es de USD~4,56 por hora. La distribución es similar entre quienes tomaron clases particulares (35 % en el rango superior, $n = 20$) y quienes no lo hicieron (31 %, $n = 68$).

## Limitaciones del instrumento

- **Representatividad:** la muestra es no probabilística y sus resultados son indicativos, no extrapolables al mercado nacional.
- **Sesgo geográfico:** el 90,9 % de las respuestas proviene de la provincia de Buenos Aires y de la Ciudad
          Autónoma de Buenos Aires. Las zonas del interior y rurales, en las que el capítulo~[§cap:introduccion] ubica el mayor impacto del proyecto, están subrepresentadas.
- **Lado de la oferta:** solo 9 respuestas corresponden a tutores, por lo que la encuesta valida principalmente el lado de la demanda.
- **Experiencia previa:** el 77,3 % no tomó clases particulares en los últimos años, por lo que las preguntas actitudinales reflejan en su mayoría intenciones y no conductas observadas.
- **Precio:** la disposición a pagar se relevó en rangos de pesos argentinos y para una clase de una hora. Su expresión en dólares depende del tipo de cambio de una única fecha, y el rango superior es abierto, por lo que no permite estimar cuánto por encima de USD~5,86 pagaría ese 31,8 %.

# Entrevistas a especialistas

Como se detalla en el capítulo~[§cap:marco-teorico]
(sección~[§sec:entrevistas]), se definieron dos perfiles de especialista complementarios: un docente o gestor/a institucional y un/a profesional del campo psicopedagógico o del vínculo y la seguridad con menores. En cada caso se documenta el contexto, la ficha de la persona entrevistada y la transcripción por ejes temáticos.

**Estado: [PENDIENTE]** – las entrevistas no se realizaron en el
Sprint 3, como preveía originalmente el cronograma del capítulo~[§cap:metodologia], y se reprogramaron para
*fecha prevista*, antes de la entrega del capítulo~[§cap:resultados]. Hasta entonces los guiones aquí transcritos constituyen la evidencia del diseño metodológico; los
*completar* marcan los datos que se completarán con la realización efectiva de cada entrevista.

## Perfil 1: Docente o gestor/a institucional

### Contexto de la entrevista

*Fecha, modalidad (presencial/remota), medio y duración.*

### Datos de la persona entrevistada

*Formación, cargo actual, experiencia relevante.*

### Guion de entrevista

*Eje 1 – apoyo escolar y repitencia.*

- ¿Qué rol juega el apoyo escolar personalizado en la prevención de la repitencia en los niveles primario y secundario?
- ¿Qué diferencias observa entre el acceso a tutorías en zonas urbanas y rurales del país?

*Eje 2 – tutoría virtual pedagógica y de seguridad.*

- Desde lo pedagógico, ¿qué recaudos considera necesarios para que una tutoría virtual 1 a 1 sea efectiva con un menor?
- Desde la seguridad, ¿qué condiciones mínimas debería garantizar una plataforma que conecta adultos desconocidos con menores en un entorno remoto?
- ¿Cómo observaría la articulación de esta plataforma con las instituciones educativas (escuelas, docentes, equipos de orientación)?

### Transcripción de la entrevista

*Transcripción organizada por ejes temáticos.*

## Perfil 2: Psicopedagogía / vínculo y seguridad con menores

### Contexto de la entrevista

*Fecha, modalidad (presencial/remota), medio y duración.*

### Datos de la persona entrevistada

*Formación, cargo actual, experiencia relevante.*

### Guion de entrevista

*Eje 1 – vínculo y acompañamiento.*

- ¿Qué impacto vincular observa en un acompañamiento personalizado
          1 a 1 para niños, niñas y adolescentes?
- ¿Qué señales de alerta de un menor conviene monitorear en un entorno remoto de interacción con un adulto no conocido?
- ¿Qué rol recomienda para el adulto responsable dentro de la plataforma?

*Eje 2 – reputación y diseño seguro.*

- ¿Qué errores evitaría en el diseño de un sistema de reputación bidireccional que involucra a menores?
- ¿Qué balance propone entre la protección del menor y el respeto a su privacidad al revisar sesiones o interacciones?
- ¿Qué recomendaciones daría para el manejo de denuncias y situaciones de conflicto entre tutores y familias?

### Transcripción de la entrevista

*Transcripción organizada por ejes temáticos.*

# Detalles técnicos e implementación

## Configuración de los modelos

**Tabla:** Hiperparámetros del modelo final (ejemplo de estructura)

| **Parámetro** | **Valor** | **Criterio de selección** |
| --- | --- | --- |
| *n_estimators* | *500* | *búsqueda en grilla, validación cruzada 5 pliegues* |
| *max_depth* | *8* | *...* |

## Datos utilizados

*Identificador, fuente, versión, fecha de descarga, licencia y tamaño de cada conjunto de datos.*

## Arquitectura de la aplicación

### Stack tecnológico

python == 3.12
scikit-learn == 1.5.0
fastapi == 0.111.0
postgresql == 16

### Esquema de base de datos

CREATE TABLE usuario (
    id          SERIAL PRIMARY KEY, correo      TEXT NOT NULL UNIQUE, creado_en   TIMESTAMPTZ NOT NULL DEFAULT now()
);

### Variables de entorno

*Nombre, propósito y ejemplo de valor de cada variable. Nunca incluir secretos reales.*

# Prompts utilizados con herramientas de IA generativa

## Criterios de registro

- **Alcance.** Se registran las instrucciones cuyo resultado tuvo un impacto significativo en el sistema o en el documento.
          Los prompts se transcriben con leves correcciones de redacción, sin alterar su contenido.
- **Verificación.** Para cada resultado se indica cómo se verificó antes de incorporarlo.
- **Autoría.** Las salidas se describen como evidencia; el texto final del documento surge de la revisión y adaptación del autor.

## Desarrollo del sistema

El desarrollo con OpenCode no se guió por prompts aislados, sino por instrucciones persistentes versionadas en el repositorio
(anexo~[§anx:repositorios]): el archivo ‘AGENTS.md‘, la
Constitución, las especificaciones, los planes técnicos y la lista de tareas. Ese conjunto constituye el registro completo de lo que se le pidió al agente. Se transcriben dos de las reglas de ‘AGENTS.md‘
que más condicionaron el resultado.

> **Instrucción IA:** Ante dos soluciones que cumplen el mismo requisito, la más simple. No justifiques una decisión técnica con “buena práctica genérica”: justificala contra un desarrollador y un presupuesto de
USD 0 a 100 por mes, o no la tomes.
> **Respuesta IA:** Arquitectura de monolito modular con nueve módulos de dominio y un único proceso separado, el servicio de matching.
Verificación: cada desvío quedó documentado en un registro de decisión
(ADR) validado por el autor.

> **Instrucción IA:** La rama del kill-switch con un menor presente nunca continúa la sesión ni le pregunta al menor si vio algo: corta directamente. Si una tarea deja dudas sobre cuál de los dos casos aplica, tratala como si hubiera un menor.
> **Respuesta IA:** Implementación del backend del kill-switch con dos ramas diferenciadas. Verificación: prueba de extremo a extremo de la rama de seguridad completa (sesión con menor, corte, suspensión, alerta y resolución del administrador).

## Consultas de contraste

Gemini y ChatGPT se consultaron de forma esporádica, como segunda y tercera opinión sobre decisiones puntuales. Sus respuestas no se incorporaron como texto al documento.
*Transcribir, si se conservaron, una o dos consultas representativas y la decisión que motivaron.*

## Elaboración del documento

Los siguientes prompts se utilizaron con Claude Code durante la revisión y redacción de los capítulos~[§cap:economica] y~[§cap:riesgos] y de los apéndices.

> **Instrucción IA:** Agregué los resultados de la encuesta y el Excel con el presupuesto y las proyecciones. Revisá si tengo que modificar algo en la tesis en función de esto y decime todo lo que falta completar.
> **Respuesta IA:** Detectó inconsistencias entre capítulos: un equipo de cuatro perfiles en la evaluación económica frente a un desarrollo unipersonal en el resto del documento, el costo del servidor de aplicación omitido, un precio de sesión sin respaldo frente a la disposición a pagar relevada, y diferencias entre el documento y el repositorio. Además, redactó el apéndice~[§apx:encuesta a partir de los datos crudos. Verificación: cada inconsistencia se contrastó con el texto y el repositorio, y las frecuencias de la encuesta se recalcularon sobre el archivo original.]

> **Instrucción IA:** Busquemos y analicemos empíricamente los costos de las plataformas con sus planes reales actuales, pensando qué es lo mejor para este caso.
> **Respuesta IA:** Relevamiento de las tarifas públicas de Supabase, Vercel,
DigitalOcean, Hetzner, Upstash, LiveKit y los proveedores de LLM.
Identificó la baja de Gemini 2.0 Flash y el costo de grabar el audio de las sesiones, no contemplado hasta entonces. Verificación: cada tarifa se consultó en la página oficial del proveedor, citada en el capítulo~[§cap:economica.]

> **Instrucción IA:** Toda la tesis debe estar en dólares. Si necesitás el tipo de cambio, usá el del BNA al cierre de la encuesta.
> **Respuesta IA:** Conversión de los rangos de la encuesta con la cotización vendedora del 9 de septiembre de 2026. Verificación: cotización contrastada en la fuente citada.

> **Instrucción IA:** Quiero saber si las horas con las que se calcula la inversión son realistas o no, y compararlas con lo que costó de verdad.
> **Respuesta IA:** Estimación del esfuerzo registrado con el método
*git-hours* y del esfuerzo tradicional con COCOMO, y propuesta de evaluar la inversión incremental bajo el criterio de costo hundido.
Verificación: métricas recalculadas sobre el repositorio; la elección del criterio de evaluación fue del autor.

> **Instrucción IA:** Construí la tasa de descuento con fuentes reales.
> **Respuesta IA:** Tasa del 21,10 % por acumulación: tasa libre de riesgo, beta sectorial, prima de mercado y prima de riesgo país. Verificación: cada componente se consultó en su fuente primaria, citada en la tabla~[§tab:tasa.]

> **Instrucción IA:** Arrancá con el capítulo 6 siguiendo las indicaciones de la cátedra.
> **Respuesta IA:** Borrador del análisis de riesgos, con quince riesgos identificados a partir de la encuesta, el modelo financiero y el estado del repositorio. Verificación: cada riesgo se contrastó con la evidencia que cita, y se ajustaron los que contradecían decisiones de otros capítulos.

# Anexos

# Repositorios de código fuente

El código fuente de Tinku se aloja en un único repositorio público de GitHub, organizado como monorepo.

## usal-tinku

smercadocarbone/usal-tinku

**Contenido.** El repositorio agrupa los tres componentes desplegables del sistema, cada uno en su propia carpeta y con su propio
‘README‘ de ejecución local:

- ‘backend/‘: API REST en Java con Spring Boot, organizada como monolito modular.
- ‘matching-service/‘: servicio de matching semántico en Python, único proceso separado del monolito.
- ‘frontend/‘: cliente PWA en Next.js y React.

Se incluyen además la documentación de diseño (‘docs/‘), los flujos de integración continua (‘.github/workflows/‘) y un
‘docker-compose.yml‘ con la infraestructura local de desarrollo.

**Estado.** Activo, en desarrollo durante el cursado de la materia.

*Licencia del repositorio (actualmente no declarada).*

# Modelo financiero

Los cálculos de la evaluación económica del capítulo~[§cap:economica] se realizan en una planilla de cálculo con parámetros editables, que se entrega junto con este documento en el siguiente archivo:

    Presupuesto_y_Proyecciones_-_Proyecto_Tinku.xlsx

Todos los montos están expresados en dólares estadounidenses.

## Estructura de la planilla

**Tabla:** Hojas del modelo financiero

| **Hoja** | **Contenido** |
| --- | --- |
| Inversión Inicial | Inversión incremental del lanzamiento: horas y tarifa por perfil, dominio, asesoría legal y contingencia, más el costo hundido del MVP a título informativo (tabla~[§tab:inversion]) |
| Gastos Post-lanzamiento | Costos fijos mensuales por año: infraestructura, servidor de aplicación, video, asistente LLM, honorarios contables, dominio y marketing (tabla~[§tab:costos-fijos]) |
| Valor de Venta | Comisión, precio por hora, duración promedio de las sesiones, ticket, costo de la pasarela, costo, precio y adopción del resumen opcional, y margen neto por sesión (tabla~[§tab:unit-economics]) |
| Estimación de Demanda | Alumnos activos por año y escenario, y sesiones anuales resultantes (tabla~[§tab:demanda]) |
| VAN, TIR y Repago | Tasa de descuento construida (tabla~[§tab:tasa]), flujo de fondos de los tres escenarios, VAN, TIR, repago simple y descontado, y resumen comparativo (tablas~[§tab:flujo-caja] y~[§tab:indicadores-financieros]) |
| Gráficos | Flujo neto y flujo acumulado por escenario, y VAN comparado |

## Supuestos editables

Los valores de entrada están separados de los cálculos: al modificar cualquiera de ellos se recalculan los tres escenarios. Los principales son la comisión de plataforma, el precio por hora, la proporción de sesiones de 30 minutos, el precio y la adopción del resumen opcional, las tarifas horarias por perfil, los alumnos activos por año, las clases por alumno por mes y la tasa de descuento. Cada supuesto documenta su origen en la columna de observaciones o en un comentario de la celda.

Los indicadores se calculan con las funciones nativas ‘NPV‘ e
‘IRR‘, y los períodos de repago con la interpolación de la ecuación~[§eq:repago].

# Bibliografía

* `[breiman2001]` *Breiman, Leo. Random Forests (2001). Machine Learning. vol. 45 pp. 5--32 DOI: 10.1023/A:1010933404324*
* `[pedregosa2011]` *Pedregosa, Fabian and Varoquaux, Gaël and Gramfort, Alexandre and Michel, Vincent and Thirion, Bertrand and Grisel, Olivier and Blondel, Mathieu and Prettenhofer, Peter and Weiss, Ron and Dubourg, Vincent and Vanderplas, Jake and Passos, Alexandre and Cournapeau, David and Brucher, Matthieu and Perrot, Matthieu and Duchesnay, Édouard. Scikit-learn: Machine Learning in Python (2011). Journal of Machine Learning Research. vol. 12 pp. 2825--2830 https://jmlr.org/papers/v12/pedregosa11a.html*
* `[chen2016]` *Chen, Tianqi and Guestrin, Carlos. XGBoost: A Scalable Tree Boosting System (2016). Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. pp. 785--794 DOI: 10.1145/2939672.2939785*
* `[lundberg2017]` *Lundberg, Scott M. and Lee, Su-In. A Unified Approach to Interpreting Model Predictions (2017). Advances in Neural Information Processing Systems 30 (NIPS 2017). pp. 4765--4774 https://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions*
* `[sommerville2016]` *Sommerville, Ian. Software Engineering (2016). Pearson. *
* `[hernandezsampieri2014]` *Hernández Sampieri, Roberto and Fernández Collado, Carlos and Baptista Lucio, Pilar. Metodología de la investigación (2014). McGraw-Hill. *
* `[pmi2021]` *Project Management Institute. A Guide to the Project Management Body of Knowledge (PMBOK Guide) (2021). Project Management Institute. *
* `[nielsen1993]` *Nielsen, Jakob. Usability Engineering (1993). Academic Press. *
* `[funes2025]` *Funes, Norman. CASSIE: Comprehensive Analysis System for Sensing Imminent Ecosystem-changes (2025). *
* `[postgresqldocs]` *PostgreSQL Global Development Group. PostgreSQL 16 Documentation (2024). https://www.postgresql.org/docs/16/*
* `[torino2023]` *Torino, Michel. Deserción escolar en Argentina (2023). *
* `[olea]` *Olea, María Marta. Ruralidad y educación en Argentina: instituciones, políticas y programas (s. f.). *
* `[sciencedirect2022]` *EDITAR: autores del meta-análisis. Effects of private tutoring intervention on students' academic achievement: A systematic review based on a three-level meta-analysis model (2022). Disponible en ScienceDirect. *
* `[ondemand2026]` *EDITAR: autores. A Causal Framework for Estimating Heterogeneous Effects of On-Demand Tutoring (2026). arXiv:2602.19296. *
* `[isotropy2026]` *EDITAR: autores. Isotropy-Optimized Contrastive Learning for Semantic Course Recommendation (2026). arXiv:2601.11427. *
* `[paperrec2025]` *EDITAR: autores. Scientific Paper Recommendation System: Application of Sentence Transformers and Cosine Similarity Using arXiv Data (2025). Journal of Applied Informatics and Computing. vol. 9*
* `[beefore2024]` *EDITAR: autores. beeFormer: Bridging the Gap Between Semantic and Interaction Similarity in Recommender Systems (2024). arXiv:2409.10309. *
* `[webrtc2025]` *EDITAR: autores. Design and Implementation of WebRTC-based Remote Online Teaching System for English Courses (2025). Proceedings of the 3rd International Conference on Educational Knowledge and Informatization. *
* `[liang2013]` *Liang, Yu-Ling and Xing, Xinyu and Cheng, Hao and Dang, Jiaxiu and Huang, Shuang and Han, Richard and Liu, Xin and Lv, Qin and Mishra, Shivakant. SafeVchat: A System for Obscene Content Detection in Online Video Chat Services (2013). ACM Transactions on Internet Technology. vol. 12 pp. 13*
* `[reputation]` *EDITAR: autores del capítulo. Reputation, Feedback, and Trust in Online Platforms (s. f.). Reengineering the Sharing Economy. *
* `[carroll1963]` *Carroll, John B.. A Model of School Learning (1963). Teachers College Record. vol. 64 pp. 723--733*
* `[bloom1968]` *Bloom, Benjamin S.. Learning for Mastery (1968). Evaluation Comment. vol. 1 pp. 1--12*
* `[bloom1984]` *Bloom, Benjamin S.. The 2 Sigma Problem: The Search for Methods of Group Instruction as Effective as One-to-One Tutoring (1984). Educational Researcher. vol. 13 pp. 4--16*
* `[rochet2006]` *Rochet, Jean-Charles and Tirole, Jean. Two-sided Markets: A Progress Report (2006). The RAND Journal of Economics. vol. 37 pp. 645--667*
* `[grandview2024]` *Grand View Research. Online Tutoring Market Size, Share & Trends Analysis Report (2024). *
* `[researchmarkets2024]` *Research and Markets. Private Tutoring Market: Global Industry Report (2024). *
* `[preply]` *Preply. Preply -- Tutores online (s. f.). https://preply.com/es/*
* `[wyzant]` *Wyzant. Wyzant -- Tutoring (s. f.). https://www.wyzant.com/*
* `[superprof]` *Superprof. Superprof Argentina -- Profesores particulares (s. f.). https://www.superprof.com.ar/*
* `[tusclases]` *Tusclases. Tusclases -- Clases particulares en Argentina (s. f.). https://www.tusclases.com.ar/*
* `[profecom]` *profe.com. profe.com -- Clases particulares online (s. f.). https://www.profe.com/*
* `[lightnode2026]` *LightNode. Hosting VPS en Argentina (VDS) con CPU dedicado y precios por hora (s. f.). https://go.lightnode.com/es/argentina-vds*
* `[bna2026]` *El Cronista. Dólar oficial: cómo cerró su cotización hoy miércoles 9 de septiembre (s. f.). https://www.cronista.com/finanzas-mercados/dolar-oficial-como-cerro-su-cotizacion-hoy-miercoles-9-de-septiembre/*
* `[fred2026]` *Federal Reserve Bank of St. Louis. Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity (DGS10) (s. f.). https://fred.stlouisfed.org/series/DGS10*
* `[damodaranbeta2026]` *Damodaran, Aswath. Betas by Sector (US) (s. f.). https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html*
* `[damodaranctry2026]` *Damodaran, Aswath. Country Default Spreads and Risk Premiums (s. f.). https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html*
* `[damodaranerp2026]` *Damodaran, Aswath. Historical Implied Equity Risk Premiums (s. f.). https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histimpl.html*
* `[boehm1981]` *Boehm, Barry W.. Software Engineering Economics (1981). Prentice Hall. *
* `[githours]` *Brunfeldt, Kimmo. git-hours: Estimate time spent on a git repository (s. f.). https://github.com/kimmobrunfeldt/git-hours*
* `[nic2026]` *NIC Argentina. Dominios y Aranceles (s. f.). https://nic.ar/es/dominios/aranceles*
* `[digitalocean2026]` *DigitalOcean. Droplet Pricing (s. f.). https://www.digitalocean.com/pricing/droplets*
* `[hetzner2026]` *Hetzner Online. Price Adjustment 15 June 2026 (s. f.). https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/*
* `[supabase2026]` *Supabase. Pricing (s. f.). https://supabase.com/pricing*
* `[vercel2026]` *Vercel. Pricing (s. f.). https://vercel.com/pricing*
* `[upstash2026]` *Upstash. Redis Pricing (s. f.). https://upstash.com/pricing/redis*
* `[livekit2026]` *LiveKit. LiveKit Cloud Pricing (s. f.). https://livekit.com/pricing*
* `[gemini2026]` *Google. Gemini Developer API Pricing (s. f.). https://ai.google.dev/gemini-api/docs/pricing*
* `[geminidep2026]` *Google. Gemini API: Deprecations (s. f.). https://ai.google.dev/gemini-api/docs/deprecations*
* `[geminitokens2026]` *Google. Understand and count tokens (s. f.). https://ai.google.dev/gemini-api/docs/tokens*

# Tinku: una plataforma digital de marketplace educativo para conectar estudiantes y tutores académicos a escala nacional

> Autor: Santiago Mercado Carbone
> Año académico: 2026
> Palabras clave: marketplace educativo, tutorías particulares, inteligencia artificial, matching semántico, educación personalizada

## Agradecimientos

*Texto de los agradecimientos.*

## Declaración sobre el uso de IA

En este trabajo se utilizaron herramientas de inteligencia artificial generativa tanto en el desarrollo del sistema como en la elaboración del documento. La tabla~[§tab:herramientas-ia] resume cada herramienta y las tareas que asistió; el registro de las instrucciones más relevantes se presenta en el apéndice~[§apx:prompts].

**Tabla:** Herramientas de IA generativa utilizadas

| **Herramienta** | **Tareas asistidas** |
| --- | --- |
| OpenCode (modelo Big Pickle) | Implementación del código del MVP a partir de la Constitución, las especificaciones, los planes técnicos y la lista de tareas redactados previamente, en las primeras etapas del desarrollo |
| Claude Code (Claude Opus 5, Claude Opus 5.5 y Claude Sonnet 5) | En el sistema: implementación de código y de pruebas automatizadas, redacción de especificaciones y de registros de decisión que el autor validó, y pruebas exploratorias sobre el despliegue. En el documento: revisión de la consistencia, relevamiento de tarifas y fuentes, recálculo del modelo financiero, alineación del texto con el sistema implementado y redacción asistida de capítulos y apéndices |
| Gemini (Gemini 3.1 Pro) | Consultas esporádicas, como segunda opinión sobre decisiones puntuales |
| ChatGPT (modelo predeterminado) | Consultas esporádicas, como tercera mirada sobre decisiones puntuales |

La magnitud de la asistencia queda registrada en el historial de los repositorios (anexo~[§anx:repositorios]). Al 14 de octubre de 2026,
129 de los 482 commits de la rama principal del repositorio del sistema figuran con autor “Claude”, entre ellos 76 de los 196 que modifican pruebas automatizadas; en el repositorio de la tesis, al 15 de octubre de
2026, 13 de sus 24 commits. Los commits registrados a nombre del autor también pueden contener código generado con asistencia, en particular con OpenCode, que no firma sus cambios.

El uso se rigió por los siguientes criterios:

- **Autoría.** La definición del problema, la arquitectura, el alcance, los criterios de evaluación y las decisiones del proyecto son del autor. Las herramientas propusieron alternativas, código y redacciones; la elección entre ellas fue siempre del autor, y las decisiones de arquitectura se documentaron como registros de decisión validados por él.
- **Verificación.** Toda tarifa, cotización y dato de mercado se confirmó en la fuente original, que se cita en cada caso. Los indicadores financieros se reprodujeron con un cálculo independiente a partir de los parámetros declarados en el anexo~[§anx:modelo-financiero] antes de incluirlos en el texto. El código se verificó con las pruebas automatizadas, la integración continua, una auditoría técnica y pruebas sobre el despliegue real (capítulo~[§cap:resultados]); cada cambio se integró a la rama principal después de la revisión del autor.
- **Trazabilidad.** Las instrucciones con las que se desarrolló el sistema están versionadas en el propio repositorio (‘AGENTS.md‘, la Constitución, las especificaciones y la lista de tareas). Los prompts más relevantes de la elaboración del documento se registran en el apéndice~[§apx:prompts].
- **Comprensión.** El autor leyó, revisó y adaptó todo el contenido asistido, y asume la responsabilidad total sobre el contenido de este documento.

## Resumen (español)

Este proyecto nace como una red a lo largo del país, con una posibilidad de expandirse, para conectar el aprendizaje y el conocimiento, elevando la tradición del apoyo escolar en los hogares argentinos y brindándoles nuevas herramientas. La iniciativa busca facilitarle a cualquier estudiante, desde el nivel primario hasta el universitario, encontrar el apoyo académico ideal, permitiendo que el saber circule sin barreras geográficas o físicas.

Actualmente, el mercado de clases particulares opera de manera muy fragmentada. Si bien la utilización de redes de vínculos entre personas genera confianza, tiene un alcance muy limitado y se restringe a entornos geográficos inmediatos. El proyecto centraliza la oferta en un ecosistema digital donde la búsqueda, la reserva, las clases virtuales y los pagos conviven en un solo sitio. Esto profesionaliza la labor docente y ofrece a las familias un entorno transparente para potenciar los resultados escolares.

Un pilar central es el modelo de confianza para el resguardo de los alumnos, en especial de los menores de edad. La identidad de cada usuario se verifica leyendo su documento nacional de identidad en el propio servidor, las credenciales académicas de los tutores se revisan manualmente y quien quiera enseñar a menores debe presentar un certificado de antecedentes penales vigente. Durante cada clase, un clasificador de contenido que corre en el navegador actúa como corte de emergencia: si hay un menor presente, interrumpe la sesión de inmediato. El menor tiene cuenta propia, pero los pagos, las autorizaciones y las denuncias quedan a cargo de su adulto responsable.

La inteligencia artificial se aplica donde aporta valor concreto: un motor de matching semántico compara lo que el alumno busca con los temas que enseña cada tutor, y un resumen automático de la clase se ofrece como adicional opcional, solo entre adultos y con el consentimiento de ambos. Al poner en valor la labor de los tutores, formalizar el sector y sumar reputación dinámica y aulas virtuales integradas, el proyecto se posiciona como una infraestructura para conectar a los estudiantes con educadores calificados, superando las barreras geográficas y generando un sustento económico para estos últimos. El impacto de esta solución se observará en la eficiencia del motor de matching, la estabilidad de las conexiones remotas y el nivel de satisfacción de los usuarios.

## Abstract (English)

This project was born as a nationwide network, with room to expand, to connect learning and knowledge, elevating the tradition of academic support in Argentine homes and giving it new tools. The initiative seeks to make it easy for any student, from primary school to university, to find the right academic support, allowing knowledge to flow without geographical or physical barriers.

Today, the private tutoring market is highly fragmented. Although relying on personal networks builds trust, its reach is very limited and confined to the immediate geographical surroundings. The project centralizes the offer in a digital ecosystem where search, booking, virtual lessons, and payments coexist in a single place. This professionalizes teaching work and offers families a transparent environment to improve school results.

A central pillar is the trust model that safeguards students, especially minors. Each user's identity is verified by reading their national identity document on the platform's own server, tutors' academic credentials are reviewed manually, and anyone who wants to teach minors must submit a valid criminal record certificate. During every lesson, a content classifier running in the browser acts as an emergency cut-off: if a minor is present, it ends the session immediately. Minors have their own account, but payments, authorizations, and reports are handled by their responsible adult.

Artificial intelligence is applied where it adds concrete value: a semantic matching engine compares what the student is looking for with the topics each tutor teaches, and an automatic lesson summary is offered as an optional add-on, only between adults and with the consent of both. By valuing tutors' work, formalizing the sector, and adding dynamic reputation and integrated virtual classrooms, the project positions itself as an infrastructure that connects students with qualified educators, overcoming geographical barriers and providing the latter with a source of income. The impact of this solution will be observed in the efficiency of the matching engine, the stability of remote connections, and user satisfaction.

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

Tinku propone una plataforma digital de marketplace educativo que centraliza en un único ecosistema la búsqueda de tutores, la reserva de sesiones, el dictado de clases virtuales y la gestión de pagos, incorporando IA como eje diferenciador: un motor de matching semántico que compara lo que el alumno busca con los temas que enseña cada tutor, un clasificador de contenido que protege la clase en el propio navegador (*kill-switch*) y un resumen automático de la sesión, ofrecido como adicional opcional para las clases entre adultos, que extiende el valor de cada clase más allá del tiempo de pantalla.

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
- **OE2 — Diseño de arquitectura del sistema:** definir la arquitectura técnica completa de Tinku –un monolito modular organizado en los nueve módulos del alcance
          (sección~[§sec:alcance])–, incluyendo modelo de datos, contratos de API, diseño UX y flujos operativos principales.
- **OE3 — Implementación del motor de matching
          IA:** desarrollar e integrar el servicio de recomendación basado en embeddings semánticos semánticos (sentence-transformers, con el índice vectorial en pgvector dentro de la misma base
          PostgreSQL) que compara la búsqueda del alumno con cada uno de los temas del catálogo elegidos por el tutor, y que a un menor solo le muestra tutores con CAP aprobado y vigente.
- **OE4 — Desarrollo del aula virtual (LiveKit):**
          implementar el módulo de videollamada mediante
          LiveKit/WebRTC integrado nativamente en la plataforma, junto con el *kill-switch* de seguridad: un clasificador de contenido que corre en el navegador de cada participante sobre el video que recibe.
- **OE5 — Implementación del sistema de pagos:** integrar
          MercadoPago Marketplace de modo que cada tutor cobre en su propia cuenta, conectada por OAuth, la plataforma perciba su comisión sobre cada cobro y conserve, durante el escrow de 24 horas posterior a la sesión, la posibilidad de reembolsar.
- **OE6 — Desarrollo del módulo de IA educativa:**
          implementar el resumen automático de sesiones como adicional pago y opcional, disponible solo en clases entre adultos que lo contratan y con el consentimiento de ambas partes: se graba únicamente el audio, se transcribe, se anonimiza y el
          LLM recibe solo el texto.
- **OE7 — Implementación del sistema de reputación:**
          desarrollar el sistema de calificaciones bidireccional implementando un umbral mínimo de calificaciones para su exposición pública como medida anti-manipulación.
- **OE8 — Validación funcional:** realizar pruebas de aceptación de usuario (UAT) con un grupo piloto de tutores y alumnos reales –adultos mientras las clases con menores permanezcan deshabilitadas (sección~[§sec:limitaciones])–, midiendo usabilidad, confianza percibida y satisfacción con el matching propuesto.

**Objetivos reformulados durante la implementación..**  Cuatro objetivos específicos se redactaron antes de que se tomaran las decisiones que los afectan, y se reformularon para describir el sistema construido. Cada cambio queda registrado como ADR en el repositorio del sistema
(anexo~[§anx:repositorios]) y se resume en la sección~[§sec:decisiones-implementacion]:

- **OE3.** El diseño inicial preveía un índice FAISS en memoria y un multiplicador de puntaje (*boost*) para los tutores que validaran voluntariamente su CAP. El índice pasó a pgvector para tener una sola base y ningún índice en memoria que reconstruir (ADR-M2-01), y el puntaje de cada tutor es la máxima similitud con cada uno de sus temas, para que quien enseña muchos temas no quede relegado (ADR-M2-03). El
          CAP dejó de ser un incentivo de posicionamiento: un requisito de seguridad del menor no puede depender de que el tutor lo quiera cumplir, por lo que pasó a ser obligatorio y vigente, pero solo para enseñar a menores (ADR-M1-04).
- **OE4.** El estado de sala en Redis se descartó: el estado de la sala vive en LiveKit y en PostgreSQL, y el límite de tasa de peticiones se lleva en la memoria del único proceso del backend, con lo que se opera una dependencia menos
          (ADR-000-04).
- **OE5.** El escrow se concebía como una retención de fondos en una cuenta de la plataforma. Para no recaudar fondos de terceros, el dinero ingresa directamente a la cuenta del tutor y el escrow es una ventana lógica de 24 horas en la que la plataforma puede reembolsar (ADR-M5-02).
- **OE6.** El resumen se planteaba como un servicio general que procesaba el audio directamente en el LLM, y el objetivo incluía un asistente conversacional de repaso conceptual. Grabar audio es la única excepción a la regla de no grabar del proyecto y solo se admite entre adultos, con el adicional contratado y el consentimiento de ambos (ADR-M3-04); el audio no puede anonimizarse antes de salir del servidor, por lo que se transcribe primero y el LLM recibe solo texto anonimizado (ADR-M6-03). El asistente conversacional salió del alcance: el MVP quedó cerrado en nueve módulos y ninguno lo contiene, de modo que incorporarlo exigiría una enmienda explícita de los principios del proyecto (Constitución del proyecto, Art.~VI). Se documenta como trabajo futuro.

## Barreras e impedimentos

El análisis del problema revela un conjunto de barreras que explican por qué la solución propuesta no ha sido desarrollada previamente en el mercado argentino con el nivel de integración que Tinku propone:

- **Barreras de verificación y onboarding:** aunque el objetivo ideal incluye la validación automatizada de antecedentes penales e identidad, los organismos competentes
          (RENAPER, Registro Nacional de Reincidencia) no ofrecen
          API públicas. Esta restricción impide automatizar dicho proceso en el MVP. En consecuencia, la plataforma centra sus esfuerzos de seguridad y confianza en la verificación propia del DNI –mayoría de edad, nombre y unicidad, leídos por OCR en el propio servidor– y en la rigurosa verificación de los antecedentes académicos. Para mitigar la barrera de verificación de antecedentes penales, el
          CAP se carga de forma manual y es obligatorio y vigente
          (doce meses desde su emisión) para todo tutor que quiera dar clases a menores; lo revisa una persona con el rol de
          Moderación y Seguridad. Los tutores que solo enseñan a adultos no lo cargan, lo que evita pedir un dato sensible que ninguna regla de esas clases necesita. En el diseño inicial se preveía un CAP optativo que mejorara la visibilidad del tutor; se descartó porque dejaba la protección del menor librada a la voluntad del tutor (ADR-M1-04). Más allá del CAP, el registro exige la demostración empírica de los conocimientos del tutor mediante la presentación de historial académico, títulos de grado o certificaciones pertinentes. Esta estrategia no solo sortea el impedimento técnico estatal, sino que alinea el sistema de admisión directamente con el objetivo central de la plataforma: asegurar la excelencia académica del apoyo escolar.
- **Barrera de adopción cultural:** el mercado de tutorías en Argentina opera bajo una lógica de confianza interpersonal muy arraigada. La migración hacia una plataforma digital requiere demostrar que la calidad y la seguridad del servicio son equivalentes o superiores al modelo informal vigente.
- **Barrera de conectividad:** aunque la cobertura de internet ha mejorado sustancialmente –y tecnologías como
          Starlink están siendo adoptadas masivamente en localidades del interior argentino, llevando conectividad satelital de banda ancha a zonas que antes carecían de ella– sigue existiendo un segmento de la población, especialmente en contextos de bajos recursos, que no puede acceder a estos servicios ni cuenta con dispositivos adecuados. Esta realidad puede limitar el alcance efectivo de la plataforma en los contextos donde el impacto social sería mayor, y debe ser considerada en el diseño de la experiencia de usuario.
- **Barrera de la masa crítica (arranque en frío):** como todo marketplace bilateral, Tinku resulta más valioso cuantos más tutores y alumnos lo utilizan. La estrategia de lanzamiento deberá contemplar mecanismos de adquisición simultánea de usuarios en ambos lados de la plataforma.
- **Barrera técnica — IA en tiempo real:** la transcripción y resumen automático de sesiones implica procesamiento de audio post-sesión, lo que requiere gestión eficiente de recursos computacionales para mantener costos operativos controlados en la fase de MVP. Por eso el resumen se ofrece como adicional pago cuyo precio cubre el costo de los modelos según la duración de la clase
          (ADR-M5-06), y el *kill-switch* clasifica el video en el navegador de cada participante, sin costo de servidor ni envío de imágenes.

## Relevancia del proyecto

La relevancia de Tinku se articula en tres dimensiones complementarias:

**Relevancia social.** Argentina presenta tasas de repitencia y abandono escolar que afectan especialmente a estudiantes en situaciones de vulnerabilidad educativa –entre ellos, quienes no logran seguir el ritmo de enseñanza colectivo y carecen de acceso a apoyo extracurricular. El acceso a tutoría personalizada y oportuna es uno de los factores protectores más eficaces contra la deserción escolar.
Tinku busca extender ese acceso a estudiantes que hoy no pueden aprovecharlo, ya sea por razones geográficas, por desconocimiento de la oferta disponible, o por la ausencia de plataformas que concentren y estandaricen esa oferta.

**Relevancia económica.** El mercado latinoamericano de tutorías online generó USD 637,3 millones en ingresos en 2023 y se proyecta un crecimiento anual compuesto del 16,6 % hasta 2030, según
[grandview2024]. A nivel global, el mercado de tutorías privadas fue valorado en USD 124,5 mil millones en 2024 y se proyecta alcanzar
USD 238,5 mil millones hacia 2033, con una CAGR del 7,5 %
[researchmarkets2024]. En Argentina, el segmento opera en su mayoría de manera informal, sin registro de transacciones ni facturación formal. Tinku propone formalizar una porción de ese mercado, habilitando el cobro digital, generando historial de actividad y contribuyendo a la bancarización de los tutores.

**Relevancia tecnológica.** El proyecto aplica a un problema local concreto tecnologías de IA de vanguardia: embeddings semánticos semánticos para el matching, modelos de lenguaje de gran escala
(LLM) para el resumen de las sesiones y un clasificador de contenido que corre en el navegador para proteger a los participantes.
Esta aplicación constituye un aporte original al estado del arte en plataformas educativas adaptativas en el contexto latinoamericano, diferenciándose de soluciones globales por su foco en las particularidades del sistema educativo y la geografía argentina.

## Enfoque metodológico

El proyecto se abordará desde una metodología de desarrollo ágil (Scrum adaptado) combinada con un proceso de investigación aplicada. Las etapas principales son:

- **Investigación y relevamiento:** análisis del estado del arte, entrevistas con tutores y alumnos potenciales, relevamiento de plataformas competidoras (Preply, Wyzant,
          Superprof, Tusclases).
- **Diseño de arquitectura y UX:** definición del modelo de datos, diseño de wireframes y prototipos de alta fidelidad, validación con usuarios.
- **Desarrollo iterativo del MVP:** implementación por módulos funcionales con una revisión del incremento al cierre de cada sprint.
- **Integración y pruebas:** pruebas unitarias, de integración, E2E y de aceptación de usuario (UAT).
- **Piloto y validación:** lanzamiento controlado con grupo reducido de tutores y alumnos reales –adultos, mientras las clases con menores sigan deshabilitadas– para validar la hipótesis central.
- **Documentación y presentación:** elaboración del informe final y presentación del producto funcional.

## Alcance del proyecto

El presente proyecto abarca el diseño completo y la implementación funcional de la versión MVP de Tinku. Este desarrollo comprende un frontend web estructurado como PWA, el cual proveerá todas las interfaces de usuario necesarias para alumnos, tutores y administradores. El núcleo del sistema es un backend API
REST implementado en Java con el framework Spring Boot y organizado como un *monolito modular*: un único proceso dividido en nueve módulos de dominio con límites claros: (1)~Identidad y
Perfiles, (2)~Motor de matching, (3)~Aula Virtual, (4)~Reservas y
Agenda, (5)~Motor de Pagos, (6)~Resumen Automático, (7)~Calificaciones y Reputación, (8)~Panel de Administración y (9)~Denuncias y Seguridad.
Los módulos se comunican con llamadas síncronas dentro del mismo proceso y con eventos de dominio en memoria, sin intermediario de mensajes, y los plazos de negocio (escrow, cancelaciones, aprobaciones, *kill-switch*) se programan con Quartz persistido en la base, para que sobrevivan a un reinicio. La única pieza propia que corre como proceso aparte es el motor de matching, escrito en
Python, que es la excepción explícita a la regla del monolito. El modelo de datos reside en una base relacional PostgreSQL que también guarda los vectores semánticos mediante la extensión pgvector; no se utiliza
Redis (ADR-000-04).

Todo el ecosistema se despliega en un servidor propio administrado con
Coolify: cuatro contenedores (base de datos, motor de matching, backend y frontend) cuyas imágenes construye GitHub Actions, publicados en internet a través de Cloudflare Tunnel y con una copia de seguridad diaria y cifrada de la base en Cloudflare R2 (implementada; se activa al cargar las credenciales de R2, paso pendiente antes del piloto). En el diseño inicial se preveía repartir el sistema entre Supabase (base de datos), Vercel
(frontend) y Upstash (Redis); se abandonó porque el plan gratuito de
Vercel no admite uso comercial y porque concentrar todo en un solo servidor mantiene el costo dentro del presupuesto de cero a cien dólares mensuales con una sola operación que atender (ADR-000-07). El proyecto incluye la documentación correspondiente a su arquitectura.

A nivel funcional, la plataforma integra el servicio de matching semántico y un módulo de aula virtual soportado por la tecnología de
LiveKit (WebRTC), con un *kill-switch* de seguridad que clasifica el video en el navegador: con un menor presente corta la clase sin preguntar; entre adultos oculta el video y pide confirmación a la contraparte. El flujo económico se cubre mediante la integración con MercadoPago Marketplace: cada tutor conecta su propia cuenta por
OAuth, el dinero de la clase ingresa a esa cuenta, la plataforma percibe su comisión sobre cada cobro y el escrow es una ventana de 24 horas posterior a la sesión durante la cual la plataforma puede reembolsar. La integración usa un cliente HTTP propio, sin el
SDK oficial. Para potenciar la experiencia educativa, el
MVP ofrece un resumen automático de la sesión como adicional pago y opcional, solo para clases entre adultos y con el consentimiento de ambos: se graba únicamente el audio, que se borra al transcribirse (24 horas como máximo); la transcripción se anonimiza y el resumen lo genera GPT-4o a partir de ese texto. Si el resumen falla, se reembolsa el adicional. Adicionalmente, el MVP cuenta con un sistema de calificaciones y reputación bidireccional, junto con un panel de administración para la gestión interna de la plataforma. El módulo de denuncias permite que un usuario adulto denuncie una sesión o a otro usuario –el menor lo hace a través de su adulto responsable–, con un motivo de una lista cerrada y evidencia opcional que aporta quien denuncia. La identidad del denunciante no se revela, el denunciado dispone de 48 horas para presentar su descargo y, mientras el caso está abierto, se pausa la liberación del pago de esa sesión; la resolución final queda a cargo de una persona con el rol de
Moderación y Seguridad. La plataforma no preserva evidencia de la sesión ante una denuncia porque no graba las clases (el audio del resumen se borra al transcribirse): el único registro de video es el fragmento de 30 segundos que el *kill-switch* sube cuando se dispara, ya que guardar más contradiría el principio de minimización de datos del proyecto.

Por último, es importante delimitar que este proyecto no incluye ciertas características en su fase inicial. Quedan excluidos de este alcance: el desarrollo de aplicaciones móviles nativas; la integración automatizada mediante API con sistemas estatales (requiriéndose en su lugar la carga y revisión manual del CAP de los tutores que enseñan a menores, cuya verificación de firma digital queda diferida); el desarrollo de un módulo de accesibilidad completo; la implementación de un modelo de suscripción premium; la posibilidad de extender la duración de una sesión de videollamada en curso mediante un cobro adicional; la incorporación de tutores menores de edad; y el asistente conversacional de repaso conceptual, que el planteo original incluía en el objetivo OE6 y que quedó fuera porque el alcance del MVP está cerrado en los nueve módulos enumerados (Constitución del proyecto,
Art.~VI). Todas estas iniciativas y funcionalidades no incluidas quedan documentadas como propuestas para el trabajo a futuro.

## Limitaciones

- **Límite de validación:** la validación de la hipótesis se realizará con un grupo piloto acotado. Los resultados son indicativos de la validez funcional del sistema, no estadísticamente representativos del mercado total.
- **Límite de piloto sin menores:** aunque el sistema está diseñado para alumnos desde el nivel primario, el piloto corre sin clases con menores. Una opción de configuración
          (‘tinku.menores.sesiones-habilitadas‘) vale
          ‘false‘ por defecto y, mientras tanto, el sistema rechaza toda reserva o solicitud de sesión cuyo beneficiario sea un menor. Solo se habilita cuando estén cerrados el
          *kill-switch* en el cliente y el CAP de los tutores de menores: al momento de esta redacción el CAP está implementado y al *kill-switch* en el cliente le resta su prueba de punta a punta contra el servicio de video real, entre otras tareas previas al encendido. Se prefirió demorar las clases con menores antes que habilitarlas sin todas sus protecciones (Constitución del proyecto, Art.~II). En consecuencia, la validación del piloto no cubre el flujo con menores.
- **Límite de verificación de tutores:** en el MVP, la identidad se verifica con reconocimiento óptico de caracteres
          (OCR) sobre el DNI, ejecutado con Tesseract en el propio servidor: controla la mayoría de edad, el nombre y que el documento no esté ya registrado. La imagen no sale del servidor ni se conserva, y no hay revisión manual del
          DNI, por lo que se acepta el riesgo de una lectura errónea en fotos de baja calidad (ADR-M1-01, ADR-M1-08). La revisión manual existe para la credencial académica y para el
          CAP. La verificación automatizada de antecedentes vía
          API queda fuera de alcance; la reemplaza la exigencia y revisión manual del CAP tramitado por el tutor vía Mi
          Argentina, obligatorio y vigente (doce meses desde su emisión) solo para dar clases a menores. Se acepta el riesgo residual de un certificado adulterado o mal evaluado, ya que la verificación de su firma digital queda diferida.
- **Límite de conectividad:** el servicio requiere conexión a internet estable para el aula virtual. Si bien Starlink y otras soluciones satelitales amplían el universo de usuarios potenciales, persiste una porción de la población objetivo sin acceso adecuado a dispositivos o conectividad.
- **Límite del resumen automático:** el resumen existe solo para las clases entre adultos que contratan el adicional y en las que ambas partes aceptaron la grabación de audio; las clases con un menor nunca se graban ni se resumen. El resumen opera sobre la transcripción anonimizada de la sesión y el conocimiento del modelo subyacente, sin acceso a libros de texto o currículos oficiales del sistema educativo argentino, y depende de un proveedor externo: sin la configuración del proveedor, el sistema no lo genera.
- **Límite geográfico del piloto:** la validación funcional queda circunscripta al territorio argentino. La plataforma está diseñada para escalar regionalmente, pero dicha expansión excede el alcance de este trabajo.
- **Límite de alineación curricular:** dado que el sistema educativo argentino no tiene un diseño curricular único a nivel nacional, un tutor de una jurisdicción puede no estar alineado con los contenidos específicos que se enseñan en la escuela del alumno en otra provincia. Esta limitación no invalida la propuesta de valor de la plataforma, pero marca un límite real de la personalización ofrecida.
- **Límite de disponibilidad:** todo el sistema –base de datos, motor de matching, backend y frontend– corre en un único servidor propio, ubicado en un domicilio y sin dirección
          IP fija, y no en un proveedor con garantías de disponibilidad.
          Es un punto único de falla aceptado para el piloto: un corte de luz o de internet deja la plataforma fuera de línea mientras dure. Se mitiga con la copia de seguridad diaria y cifrada fuera del servidor y con un procedimiento de restauración documentado en el manual de operación, y la decisión se revisa si crece la operación (ADR-000-07). El plan original preveía migrar a un VPS alquilado antes del piloto; se optó por concentrar todo en el servidor existente por simplicidad operativa y costo.

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
| Infraestructura | Servidor propio ya existente, administrado con Coolify, con cuatro contenedores (PostgreSQL con pgvector, motor de matching, backend y frontend) publicados mediante Cloudflare Tunnel; imágenes construidas por GitHub Actions y publicadas en el registro de contenedores de GitHub; copia de seguridad diaria y cifrada de la base en Cloudflare R2 (capa gratuita, 14 días de retención). Sin costo de alquiler de hosting; el presupuesto de infraestructura se mantiene entre USD 0 y 100 mensuales. El plan original (Vercel, Supabase, Upstash y migración a un VPS de 10 a 25 USD mensuales antes del piloto) se reemplazó por esta topología (ADR-000-07, sección~[§sec:alcance]). |
| Servicios externos | Motor de matching semántico: sentence-transformers (modelo ‘paraphrase-multilingual-MiniLM-L12-v2‘, vectores de 384 dimensiones) con el índice en pgvector, con procesamiento local y sin costo de API por consulta. Resumen de sesión: transcripción con ‘gpt-4o-mini-transcribe‘ (ADR-M3-04) y resumen con GPT-4o sobre el texto anonimizado (ADR-M6-03), con un costo que cubre el precio del adicional (capítulos [§cap:marco-tecnologico] y [§cap:economica]). MercadoPago: sin costo fijo, comisión por transacción, integrado con un cliente HTTP propio y conexión OAuth de cada tutor. LiveKit Cloud: plan gratuito Build de 5.000 minutos de participante por mes. Resend (plan gratuito) para el correo transaccional (ADR-000-06). OCR con Tesseract local, sin servicio externo. |
| Herramientas de desarrollo | OpenCode + Neovim (editor principal), GitHub y GitHub Actions (control de versiones e integración continua), Figma (diseño UX), JUnit 5 con Testcontainers (pruebas del backend contra PostgreSQL real), Playwright con axe-core (pruebas E2E y de accesibilidad del frontend), pytest (motor de matching) y JaCoCo (medición de cobertura). La mención original de Jest se reemplazó porque las pruebas del frontend se resolvieron con Playwright. Todas en planes gratuitos o estudiantiles. |
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
Quedan fuera del alcance investigativo los mercados regionales, la integración con organismos estatales, los módulos de accesibilidad y suscripción premium y el asistente conversacional de repaso conceptual
(sección~[§sec:alcance]), los cuales se documentan como trabajo futuro. El piloto se realiza sin clases con menores
(sección~[§sec:limitaciones]), por lo que la validación no cubre ese flujo.

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
Google Forms orientado a estudiantes universitarios y familias con hijos en edad escolar, buscando un mínimo de 30 respuestas válidas. El guion de las entrevistas se transcribe en el apéndice~[§apx:entrevista] y la encuesta completa en el apéndice~[§apx:encuesta].

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

Scrum organiza el trabajo en **sprints** con objetivos concretos, revisión del incremento al final de cada ciclo y un backlog priorizado.
La duración de los sprints no es fija: se ajustó a los hitos académicos del cronograma y varía entre algo más de una semana y alrededor de un mes, según el bloque de trabajo (figura~[§fig:gantt]). En este contexto unipersonal, el desarrollador asume los roles de Product Owner, Scrum Master y Development Team, contando con el director del proyecto como stakeholder externo para la revisión académica. Los artefactos incluyen el Product Backlog, el
Sprint Backlog y el Incremento, mientras que las ceremonias adaptadas comprenden la Sprint Planning de una hora al inicio de cada ciclo, un
Daily Stand-up diario personal documentado en la bitácora de desarrollo, la Sprint Review y la Sprint Retrospective.

## Gestión del proyecto: dimensiones clave

En línea con los criterios de evaluación del proyecto y el perfil directivo en Project Management Professional, se detallan las dimensiones principales de gestión:

- **Alcance:** definido por los nueve módulos del MVP
          descritos en el capítulo~[§cap:introduccion]
          (sección~[§sec:alcance]): Identidad y Perfiles, Motor de matching, Aula Virtual, Reservas y Agenda, Motor de Pagos,
          Resumen Automático, Calificaciones y Reputación, Panel de
          Administración, y Denuncias y Seguridad. Cualquier funcionalidad adicional requiere una enmienda explícita de los principios del proyecto (Constitución del proyecto, Art.~VI), y toda decisión técnica que se aparte de lo planificado se registra como ADR en el repositorio del sistema
          (anexo~[§anx:repositorios]). El control del alcance se apoya, además, en el Product Backlog, el Sprint Backlog y los incrementos funcionales.
- **Tiempos:** el proyecto se estructura en sprints de duración variable a lo largo de seis meses entre junio y noviembre de 2026, con una dedicación estimada de 15 a 20 horas semanales e hitos académicos inamovibles, integrando las ceremonias del marco ágil adoptado.
- **Costos:** los costos operativos del MVP se estiman entre cero y cien dólares mensuales durante el desarrollo, cubiertos mediante un servidor propio y planes gratuitos de los servicios externos, detallándose plenamente en el capítulo~[§cap:economica].
- **Riesgos:** el análisis detallado se presenta en el capítulo~[§cap:riesgos], contemplando factores como demoras en la integración de API externas, costos de modelos de lenguaje superiores a los estimados y la dificultad para reclutar usuarios para el piloto.
- **Calidad:** cada historia de usuario de las especificaciones de los módulos se ejercita con al menos una prueba de integración de punta a punta, y los casos borde que cada especificación resuelve son casos de prueba obligatorios.
          El backend se prueba con JUnit 5 y Testcontainers contra una base PostgreSQL real; el frontend, con pruebas E2E en
          Playwright y controles de accesibilidad con axe-core; el motor de matching, con pytest. Las suites corren en integración continua en cada cambio, y una prueba E2E nocturna recorre el camino crítico contra la base, el motor de matching y el backend reales. La planificación original fijaba una cobertura mínima del 70 % por módulo; durante la implementación se optó por medir primero la cobertura de líneas con JaCoCo, sin un umbral que corte la compilación, y decidir el umbral con el valor medido (ADR-000-05). Al
          14 de octubre de 2026 el backend contaba con 661 pruebas y una cobertura de líneas del 85,6 %. La calidad percibida se mide mediante los indicadores específicos de la investigación.
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
| 22 sep 2026 | Cap.~6 Análisis de riesgos | Sprint 7: aula virtual (LiveKit) |
| 13 oct 2026 | Cap.~7 Resultados | Sprints 8–9: resumen automático + sistema de reputación |
| 27 oct 2026 | Cap.~8 Conclusiones | Sprint 10: integración end-to-end, pruebas de sistema y correcciones |
| 28 nov 2026 | Presentación final + producto funcional | Sprint 11: piloto con usuarios reales (adultos, sección~[§sec:limitaciones]), análisis de resultados, documentación final |

La planificación original incluía Redis en el Sprint 7 para el estado propio de la aplicación –chat en tiempo real y límite de tasa de peticiones–. Durante la implementación se descartó para operar una dependencia menos (ADR-000-04): el límite de tasa se lleva en la memoria del único proceso del backend, el estado de la sala vive en LiveKit y en
PostgreSQL, y no hay un módulo de chat propio, ya que los mensajes de texto del aula viajan por el canal de datos de LiveKit. La tabla~[§tab:hitos] y la figura~[§fig:gantt] presentan la planificación, con la línea de tiempo completa.

<!-- Figura: Cronograma de sprints del proyecto (ciclo lectivo 2026) -->

## Herramientas de gestión y seguimiento

Para garantizar la trazabilidad del trabajo y la calidad del proceso, se implementarán diversas herramientas tecnológicas de soporte. Se utilizará **GitHub Projects** para la gestión del backlog y los sprints mediante tableros Kanban integrados al repositorio, donde cada issue representa una tarea del sprint backlog. El control de versiones se efectuará en GitHub mediante ramas de características y solicitudes de revisión antes de la integración a la rama principal. Asimismo, se mantendrá una bitácora de desarrollo en formato de texto simple actualizada al cierre de cada jornada para registrar avances y decisiones técnicas como parte del seguimiento diario.

Para el diseño de interfaz se empleará Figma en la elaboración de prototipos de alta fidelidad, mientras que Postman servirá para la documentación y prueba de los endpoints de la API REST. En el backend Spring Boot, las pruebas se escriben con JUnit 5 y Mockito, y las de integración usan Testcontainers para correr contra una base
PostgreSQL real; la cobertura se mide con JaCoCo. En el frontend, las pruebas E2E se escriben con Playwright –con la API
simulada y controles de accesibilidad con axe-core– y el código se revisa con el analizador estático oxlint; la planificación original preveía Jest para las pruebas unitarias del frontend, pero se optó por
Playwright, que prueba los flujos tal como los recorre el usuario. El motor de matching se prueba con pytest. Todas las suites están integradas en el pipeline de integración continua mediante GitHub
Actions, y la rama principal solo admite cambios con las suites en verde. Para el despliegue, cada componente se empaqueta como imagen
Docker, construida por GitHub Actions y publicada en el registro de contenedores de GitHub, y se ejecuta mediante Coolify, una plataforma de despliegue autoalojada que gestiona contenedores y variables de entorno de forma equivalente a un PaaS gestionado. Coolify corre en un servidor propio, publicado en internet mediante Cloudflare Tunnel, que además cifra el tráfico entre los usuarios y el servidor. La planificación original preveía migrar a un VPS alquilado antes del piloto; se mantuvo el servidor propio por simplicidad operativa y costo, aceptando un punto único de falla para el piloto (ADR-000-07, sección~[§sec:limitaciones]).

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
sobre el progreso del alumno –el antecedente comercial más cercano encontrado al resumen automático post-sesión de Tinku, aunque aplicado sobre un modelo de plantilla docente curada y no sobre un marketplace abierto de tutores independientes. En Tinku ese resumen quedó como un adicional opcional, solo entre adultos; el asistente conceptual de repaso que el diseño inicial también planteaba no se implementó (capítulo~[§cap:marco-tecnologico], sección~[§sec:decisiones-implementacion]).

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
    Tinku serán menores de edad, se propone un mecanismo que analice localmente (*edge computing*) los fotogramas mediante un modelo de clasificación y que ante una detección positiva actúe en una de dos ramas: si en la clase hay un menor, corta automáticamente la transmisión, sin preguntar, y suspende preventivamente al tutor implicado; si ambos participantes son adultos, oculta el video del detectado y le pide confirmación a la contraparte antes de cortar.
    El mecanismo técnico completo, incluida la verificación de edad del tutor mediante OCR y DNI, se desarrolla en la sección~[§sec:seguridad].

    **Salvedades a considerar:** ningún clasificador automático tiene 0 % de falsos positivos/negativos; es una capa adicional, no una garantía absoluta. El procesamiento en el dispositivo (por ejemplo, TensorFlow.js) evita enviar video a un servidor, facilitando el cumplimiento de la Ley de Protección de Datos Personales
    (Ley~25.326). El proceso de reactivación manual debe contemplar la notificación a un adulto responsable. Al ser un desarrollo complejo
    (visión por computadora en tiempo real), debe evaluarse su viabilidad dentro de los plazos del MVP. En la implementación, el clasificador se integró en el navegador con NSFWJS sobre TensorFlow.js; mientras no se cierre su verificación completa, el piloto corre sin clases con menores (capítulo~[§cap:marco-tecnologico], sección~[§sec:decisiones-implementacion]).

- **Reputación con fricción reducida (señales implícitas).** — La literatura [reputation] señala que las calificaciones explícitas (estrellas) son propensas a sesgos. Se propone combinar una acción mínima (reacción rápida) con señales de comportamiento capturadas automáticamente: tasa de sesiones completadas, puntualidad, y la tasa de recontratación del mismo tutor por parte del mismo alumno (preferencia revelada).

- **Precio dinámico por poder adquisitivo regional.** — Se propone que la plataforma sugiera un rango de precio de referencia ajustado al poder adquisitivo de la provincia o localidad del alumno, calculado a partir de los datos transaccionales de la plataforma, manteniendo la decisión final en el tutor. En la implementación se redujo a un precio de referencia por provincia, no vinculante, que el rol de administración mantiene a mano y que el tutor ve como sugerencia al fijar su tarifa; el cálculo a partir de datos transaccionales queda como trabajo futuro.

- **Modo de baja conectividad.** — Se propone una degradación progresiva de calidad (video $$ solo audio
    $$ mensajería de texto) ante caídas de ancho de banda, sumado a la retención temporal de un buffer de video rotativo de 30
    segundos, el cual se persiste y envía como evidencia únicamente si se dispara el sistema de seguridad (kill-switch).

### Marco legal

El diseño de la relación contractual entre la plataforma, el adulto responsable y el menor se apoya en el sistema de capacidad progresiva del Código Civil y Comercial de la Nación, artículos 25 y 26, que establece que los adolescentes de entre 13 y 18 años tienen capacidad de ejercicio creciente, pero que los contratos que los comprometan patrimonialmente requieren la representación o el consentimiento de los progenitores según los artículos 682 y 690, salvo los de escasa cuantía de la vida cotidiana previstos en el artículo 684 bis, categoría en la que un paquete de clases particulares no encuadra. De ahí surge la decisión de que la cuenta contratante y pagadora sea siempre la del adulto responsable.

El mismo criterio se refuerza con un antecedente impositivo: el modelo de retención que aplican plataformas comparables en Argentina, como
Uber, Rappi, PedidosYa y Airbnb, donde AFIP obliga al agente de pago a retener hasta un 28 % de lo abonado a quien no esté inscripto en el régimen de Monotributo, funciona como antecedente directo de la estrategia de formalización tributaria de los tutores de Tinku, desarrollada en el capítulo~[§cap:economica]. A esto se suma la jurisprudencia laboral argentina sobre la relación de dependencia encubierta de repartidores de plataformas de delivery, que constituye un antecedente de riesgo legal relevante para el vínculo entre Tinku y sus tutores, documentado como riesgo en el capítulo~[§cap:riesgos].

## Bases teóricas

### Variable 1: matching semántico e inteligencia artificial aplicada a sistemas de recomendación

El motor de matching de Tinku se apoya conceptualmente en dos cuerpos teóricos: los sistemas de recomendación (*recommender systems*), que buscan predecir la afinidad entre dos entidades a partir de sus atributos; y el procesamiento de lenguaje natural (NLP) aplicado a la representación semántica de texto mediante embeddings semánticos. Un embeddings semánticos es una representación vectorial de un texto en un espacio de alta dimensionalidad. Modelos como los sentence-transformers generan vectores a partir de oraciones completas, superando las búsquedas por palabras clave. Sobre este espacio, estructuras como FAISS o extensiones de bases de datos relacionales como pgvector permiten búsquedas de similitud eficientes. Tinku usa pgvector: guarda los vectores en una columna de la misma base PostgreSQL que el resto del sistema, de modo que no hay un índice en memoria que reconstruir ni copiar al reiniciar el servicio, y el volumen del piloto no requiere las optimizaciones de FAISS para colecciones muy grandes. Los vectores se calculan con el modelo multilingüe ‘paraphrase-‘‘multilingual-‘‘MiniLM-L12-v2‘, de 384
dimensiones (capítulo~[§cap:marco-tecnologico], sección~[§sec:decisiones-implementacion]).

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
Sobre este, Tinku utiliza LiveKit, un framework open-source que simplifica la implementación de salas escalables, en su versión administrada (LiveKit Cloud). El estado en tiempo real de cada sala lo mantiene el propio LiveKit, y el estado de negocio de la clase se guarda en la base de datos del sistema; por eso no se usa un almacén en memoria como Redis, que el diseño inicial preveía.

En el circuito de pagos, se apoya en MercadoPago Marketplace con un escrow entendido como ventana lógica: cada tutor conecta su propia cuenta de MercadoPago, el pago del alumno entra a esa cuenta y la plataforma cobra su comisión en la misma operación. Durante las 24 horas posteriores a la clase la plataforma todavía puede ordenar el reembolso, por ejemplo ante una denuncia o una falta del tutor; Tinku no retiene ni recauda los fondos de terceros. El diseño inicial suponía que la plataforma retenía el dinero hasta la clase; se cambió para no recaudar fondos ajenos (capítulo~[§cap:marco-tecnologico], sección~[§sec:decisiones-implementacion]).

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

El capítulo describe el sistema tal como quedó construido. Varias decisiones del diseño inicial se modificaron durante la implementación; cada cambio se explica donde corresponde y se resume, con su fundamento, en la sección~[§sec:decisiones-implementacion].

## Arquitectura del sistema

### Estilo arquitectónico

Tinku es un **monolito modular**: un único backend en Spring
Boot organizado en nueve módulos de dominio –Identidad, Matching, Aula,
Reservas, Pagos, Resumen, Reputación, Admin y Seguridad–, cada uno con su propio paquete Java y su propio esquema en la base de datos. Los módulos se comunican de forma síncrona, dentro del mismo proceso, cuando el flujo necesita una respuesta inmediata, y mediante eventos de dominio en memoria (por ejemplo sesion.finalizada o denuncia.registrada) cuando un hecho dispara varias reacciones independientes. No se usa ningún *message broker* externo. Todo plazo de negocio que involucra dinero o seguridad –liberación del escrow, vencimiento de una reserva sin pagar, plazos del kill-switch y de las denuncias, borrado del audio del resumen– se programa con Quartz persistido en la misma base de datos, de modo que sobrevive a un reinicio del proceso (Constitución del proyecto, artículos VIII a X; ADR-000-01 y
ADR-000-02).

La única pieza propia que corre como proceso aparte es el **motor de matching**, un servicio en Python que calcula los embeddings semánticos y consulta la similitud semántica. Es una excepción explícita y documentada: el ecosistema de modelos de lenguaje que el motor necesita (sentence-transformers) es nativo de Python, y aislarlo evita mezclar dos entornos de ejecución en el mismo proceso. El backend lo invoca por HTTP de forma síncrona. Fuera de esa excepción, se descartó una arquitectura de microservicios propios porque, para un único desarrollador y un MVP de alcance acotado, la sobrecarga de versionar, comunicar y observar varios servicios no se justifica frente al beneficio.

El diseño inicial describía un estilo “cliente-servidor en capas” en el que toda la IA –incluido el matching– se delegaba a proveedores externos. Se reemplazó por el monolito modular porque los embeddings semánticos los calcula Tinku con un modelo abierto, sin costo por llamada y sin que los perfiles salgan del servidor; los proveedores externos quedaron acotados al video (LiveKit Cloud), el cobro
(MercadoPago), la transcripción y el resumen (OpenAI) y el correo transaccional (Resend). Los límites entre módulos son organizativos
–paquetes y esquemas separados– y no los impone el compilador: el acceso directo de un módulo a datos de otro está medido y aceptado como deuda técnica en ADR-000-03.

### Componentes y responsabilidades

La tabla~[§tab:componentes] resume los componentes del sistema y sus responsabilidades.

**Tabla:** Componentes del sistema y responsabilidades

| **Componente** | **Responsabilidad** | **Tecnología** |
| --- | --- | --- |
| Cliente web (PWA) | Interfaz para alumno, tutor, adulto responsable y administración; consume la API REST del backend. En el aula corre el clasificador del kill-switch sobre el video remoto y, solo con el adicional de resumen, graba el audio en el navegador del tutor | Next.js 16 + React 19; NSFWJS sobre TensorFlow.js; cliente de LiveKit |
| Backend (monolito modular) | Lógica de negocio de los nueve módulos, autenticación y autorización por tipo de usuario y por acción, plazos de negocio persistidos, orquestación de los servicios externos | Java 21 + Spring Boot 4.1.1, Spring Security + JWT, Quartz, JPA + Flyway |
| Motor de matching | Cálculo de embeddings semánticos de perfiles y temas, y consulta de similitud semántica contra la base | Python, FastAPI, sentence-transformers (‘paraphrase-‘‘multilingual-‘‘MiniLM-L12-v2‘, 384 dimensiones) |
| Base de datos | Persistencia de los nueve módulos (un esquema por módulo), índice semántico y tablas de Quartz | PostgreSQL 16 con pgvector, en contenedor propio |
| Aula virtual | Transmisión de audio, video, pizarra y mensajes de texto entre tutor y alumno | LiveKit Cloud (WebRTC); el backend emite los tokens de sala y cierra las salas por la API de LiveKit, sin SDK |
| Pasarela de pagos | Cobro con Checkout Pro en la cuenta de MercadoPago de cada tutor, conectada por OAuth; reembolsos durante la ventana de escrow | MercadoPago, cliente HTTP propio (sin SDK) |
| Transcripción y resumen | Transcripción del audio de la clase y resumen sobre el texto ya anonimizado, solo con el adicional contratado | OpenAI: ‘gpt-4o-mini-transcribe‘ y LLM GPT-4o |
| Correo transaccional | Avisos y recuperación de contraseña fuera de la aplicación | Resend (plan gratuito), por HTTP |
| Panel de administración | Moderación (credenciales, CAP, alertas del kill-switch, denuncias, sanciones), soporte financiero y salud de la infraestructura, con dos roles de administrador | Módulo Admin del backend + vistas /admin del frontend |
| Publicación y operación | Entrada desde internet sin abrir puertos, orquestación de contenedores y respaldo de la base fuera del servidor | Cloudflare Tunnel, Coolify, copia diaria cifrada en Cloudflare R2 |

### Flujo de datos

El cliente nunca se comunica con los servicios externos usando credenciales propias: todo pasa por el backend, que actúa como intermediario autenticado. El cliente se autentica contra el backend mediante JWT y consume la API REST para las operaciones habituales –búsqueda de tutores, reservas, pagos, calificaciones, denuncias. Para el aula virtual, el backend genera un token de acceso de
LiveKit con permisos acotados a la sala correspondiente y se lo entrega al cliente, que recién entonces se conecta directamente a LiveKit Cloud para el audio, el video y los mensajes de texto (que viajan por el canal de datos de la sala); así el tráfico de video no pasa por el backend.

Los pagos siguen una lógica equivalente: el backend crea la preferencia de pago contra la API de MercadoPago con el token del tutor de esa reserva, recibe la notificación por webhook cuando el pago cambia de estado y, además, concilia periódicamente los pagos pendientes con un trabajo de Quartz. El matching se resuelve con una llamada HTTP
síncrona al motor en Python: el backend acota primero los candidatos
(autorización, cuentas suspendidas, tutores habilitados) y el motor ordena ese subconjunto por similitud. El resumen, en cambio, es asincrónico sin necesidad de colas: al finalizar la sesión, un evento de dominio en memoria y un trabajo de Quartz persistido transcriben el audio, lo anonimizan y piden el resumen, con reintentos ante fallas. El diseño inicial preveía colas para el matching y la IA; se descartaron porque la Constitución del proyecto prohíbe un
*broker* externo y porque Quartz, que ya era necesario para los plazos de negocio, cubre el mismo caso sin otra pieza que operar.

### Diagrama de arquitectura

La figura~[§fig:arquitectura] muestra los componentes de la tabla~[§tab:componentes] y sus conexiones. Todo el tráfico de internet entra por Cloudflare Tunnel hasta el servidor propio, donde
Coolify ejecuta los contenedores del frontend, el backend, el motor de matching y la base de datos. El backend es el único componente con credenciales para hablar con MercadoPago, OpenAI y Resend; LiveKit Cloud es la única excepción, donde el cliente se conecta directamente una vez que el backend le entrega un token de corta duración.

<!-- Figura: Diagrama de arquitectura del sistema -->

## Prototipo / MVP construido

El alcance implementado y operativo frente al que todavía está simulado o mockeado se documenta en cada entrega: qué funcionalidades están activas
(por ejemplo, registro, login o búsqueda de tutores) frente a las pantallas de flujo de pago sin integración real. A eso se suman capturas de pantalla de las vistas principales, un enlace al repositorio de código en GitHub (anexo~[§anx:repositorios]) con la estructura de carpetas documentada, una descripción de cómo se probó lo construido hasta el momento –pruebas manuales, UAT con usuarios del piloto, pruebas automatizadas– junto con los resultados obtenidos, y las limitaciones puntuales del estado actual con los próximos pasos según el
Sprint Backlog vigente.

*Completar con el estado del MVP al momento de la entrega.*

## Stack de software

Las versiones exactas de cada dependencia se listan en el apéndice~[§apx:tecnicos].

### Frontend

**Tabla:** Frontend: decisión tecnológica

| **Ítem** | **Detalle** |
| --- | --- |
| Tecnología | Next.js 16 + React 19 (App Router), elegido por el posicionamiento en buscadores de los perfiles públicos de tutores |
| Por qué se eligió | Conocimiento previo del desarrollador (capítulo~[§cap:introduccion], sección~[§sec:recursos]), ecosistema maduro, gran disponibilidad de componentes para formularios, calendarios y videollamada embebida |
| Alternativas evaluadas | Vue.js – descartado por menor familiaridad del desarrollador, lo que hubiera consumido tiempo de aprendizaje no disponible en el cronograma de seis meses |
| Formato de despliegue | PWA, consistente con la exclusión de app móvil nativa del alcance (capítulo~[§cap:introduccion], sección~[§sec:alcance]); se sirve desde un contenedor propio en el mismo servidor que el backend |
| Clasificador del kill-switch | NSFWJS 4.3 sobre TensorFlow.js 4.22 (backend ‘wasm‘), con el modelo servido por el propio frontend: el video nunca sale del navegador para ser clasificado (ADR-M3-01) |

### Backend

**Tabla:** Backend: decisión tecnológica

| **Ítem** | **Detalle** |
| --- | --- |
| Tecnología | Java 21 + Spring Boot 4.1.1 (la rama 3.5 dejó de recibir parches gratuitos el 30/06/2026) |
| Por qué se eligió | Framework “batteries-included” (seguridad, ORM, validación, manejo de excepciones ya resueltos) que reduce el riesgo de un desarrollador único investigando y ensamblando librerías sueltas bajo un cronograma fijo; Quartz con persistencia en la base, necesario para que ningún plazo de negocio viva en memoria; alta disponibilidad de documentación y comunidad en español (ADR-000-02) |
| Alternativas evaluadas | Go – descartado pese a tener ventajas reales de footprint de memoria y simplicidad del lenguaje, porque su ecosistema requiere ensamblar manualmente router, ORM y librerías de autenticación, lo cual consume tiempo de decisión de arquitectura que un proyecto de 6 meses en solitario no puede permitirse. Node.js – descartado como backend principal por preferirse la robustez de tipado y el ecosistema de seguridad de Spring frente a un desarrollador que tampoco tenía experiencia consolidada previa en ninguno de los dos |
| Autenticación | Spring Security + JWT emitido y validado por el propio backend, sin un proveedor externo de identidad: el modelo de permisos de Tinku –adulto responsable, menor con permisos por acción, tutor, dos roles de administración– requiere reglas de autorización propias que conviene mantener dentro del mismo framework que gestiona el resto de las reglas de negocio |
| Motor de matching | Servicio aparte en Python 3.12 con FastAPI y sentence-transformers; modelo ‘paraphrase-‘‘multilingual-‘‘MiniLM-L12-v2‘ (384 dimensiones), elegido por ser multilingüe y correr en CPU dentro del mismo servidor, sin costo por consulta |

### Datos

**Tabla:** Capa de datos: decisión tecnológica

| **Ítem** | **Detalle** |
| --- | --- |
| Motor relacional | PostgreSQL 16 con la extensión pgvector (imagen pgvector/pgvector:pg16), en un contenedor propio con volumen persistente. Un solo motor y un esquema por módulo (‘identidad‘, ‘matching‘, ‘aula‘, ‘reservas‘, ‘pagos‘, ‘resumen‘, ‘reputacion‘, ‘admin‘, ‘seguridad‘) |
| Conexión | El backend y el motor de matching se conectan por JDBC y ‘psycopg‘ dentro de la red interna de los contenedores; la base no publica ningún puerto hacia internet |
| Índice semántico | Columna ‘vector(384)‘ de pgvector en la misma base: los embeddings semánticos de perfiles y temas se guardan junto al resto de los datos y no hay un índice en memoria que reconstruir al reiniciar (ADR-M2-01) |
| Estado en tiempo real | Sin Redis. El estado de la sala vive en LiveKit Cloud y en la base; los límites de pedidos por IP y el bloqueo por intentos de login se cuentan en memoria del backend, válido mientras haya una sola instancia (ADR-000-04) |
| Migraciones | Flyway, con el esquema validado al arrancar (‘ddl-auto: validate‘): si el código y la base divergen, el backend no inicia. Una migración ya aplicada nunca se edita; las correcciones se agregan como migraciones nuevas |
| Respaldo | Copia diaria de la base con pg_dump, cifrada y subida a Cloudflare R2, fuera del servidor, con 14 días de retención (ADR-000-07). El contenedor está desplegado; la copia sale del servidor recién cuando se cargan las credenciales de R2, paso pendiente antes del piloto |

El diseño inicial ubicaba la base en Supabase (conectada por su
*pooler*), un índice FAISS en memoria del proceso de matching y Redis en Upstash para el estado del chat y el control de pedidos. Las tres piezas se descartaron: Supabase y Upstash porque todo el sistema se concentró en un único servidor propio (sección~[§sec:infraestructura]);
FAISS porque obligaba a mantener un segundo mecanismo de copia y reconstrucción del índice, mientras que pgvector deja el índice como una columna más de la misma base (ADR-M2-01); y Redis porque, con una sola instancia del backend, una dependencia menos simplifica la operación sin perder nada (ADR-000-04, decisión D8). No existe un módulo de chat: los mensajes de texto del aula viajan por el canal de datos de LiveKit.

## Infraestructura y hosting

La tabla~[§tab:infra] resume dónde se aloja cada componente.

**Tabla:** Infraestructura y hosting de cada componente

| **Componente** | **Dónde se aloja** | **Notas** |
| --- | --- | --- |
| Frontend, backend, motor de matching y base de datos | Un servidor propio de 8~GB de memoria, en el domicilio del desarrollador, sin IP fija, administrado con Coolify (PaaS autoalojado). Cada componente es un contenedor del mismo *Docker Compose*, con límites de memoria propios | Ningún contenedor publica puertos. Las imágenes se construyen en GitHub Actions y se publican en GitHub Container Registry; el servidor solo las descarga y las ejecuta (ADR-000-07) |
| Entrada desde internet | Cloudflare Tunnel, desde un contenedor ‘cloudflared‘ en el mismo servidor | Cloudflare pone el HTTPS y enruta el dominio público al frontend y el subdominio de la API al backend, sin abrir puertos en el router |
| Respaldo de la base | Cloudflare R2 (capa gratuita) | Copia diaria cifrada, 14 días de retención; restauración documentada en el manual de operación del repositorio |
| Aula virtual | LiveKit Cloud | Plan gratuito (Build): 5.000 minutos de participante por mes sin necesidad de tarjeta de crédito, equivalente a más de 40 horas de clases de 1 a 1 mensuales – cobertura suficiente para el piloto. Se descartó el auto-hospedaje de LiveKit porque requiere una IP pública alcanzable por UDP para el protocolo WebRTC, algo que el servidor propio no tiene |
| Pagos, transcripción y resumen, correo | MercadoPago, OpenAI y Resend | Servicios externos invocados solo desde el backend; sin configuración, cada integración queda apagada y falla de forma segura (*fail-closed*) |

El diseño inicial repartía la operación entre Vercel (frontend),
Supabase (base de datos), Upstash (Redis) y un backend en la computadora del desarrollador que se migraría a un VPS alquilado (por ejemplo,
Hetzner) antes del piloto. Se reemplazó por un único servidor con
Coolify por tres motivos registrados en ADR-000-07: el plan gratuito de
Vercel no admite uso comercial, concentrar todo en un proveedor reduce la operación de un único desarrollador, y el costo queda dentro del techo de 0–100 USD mensuales. La decisión acepta riesgos explícitos: el servidor es un único punto de falla y, al estar en un domicilio, un corte de luz o de internet deja al sistema fuera de línea mientras dure. Se mitigan con la copia diaria fuera del servidor (pendiente de activar con las credenciales de R2), una restauración a ensayar antes del piloto y, como recomendación del mismo ADR, una UPS y un aviso externo de caída; la decisión se revisa si la operación crece.

En cuanto a la escalabilidad: para el rango de tráfico esperado durante el MVP y el piloto (capítulo~[§cap:metodologia]), una única instancia de cada componente es suficiente. Escalar el backend a más de una instancia exige antes revisar dos decisiones que hoy suponen una sola
–Quartz sin *clustering* y los contadores de pedidos en memoria
(ADR-000-04)–, por lo que el escalado horizontal queda como trabajo futuro, condicionado a que el volumen de uso real lo justifique.

Los costos por componente y por etapa (desarrollo, piloto, eventual escalado) se presentan en el capítulo~[§cap:economica], consistente con el techo de 0–100 USD mensuales declarado en el capítulo~[§cap:metodologia].

## Modelo de datos

El modelo se organiza en nueve esquemas, uno por módulo, versionados con
Flyway. Las tablas principales y sus atributos clave se describen en el diccionario de datos del apéndice~[§apx:tecnicos]; esta sección resume las entidades y sus relaciones.

**Usuario** (identidad.usuarios) es la entidad base. Su tipo es
ADULTO, MENOR o TUTOR; un ADULTO tiene una o dos capacidades
–estudiante y adulto responsable–. El menor tiene una cuenta y una sesión propias (tipo MENOR) vinculadas obligatoriamente a su Adulto
Responsable, con permisos restringidos a nivel de endpoint: no puede pagar, no puede autorizar tutores nuevos ni presentar denuncias, y no crea Reservas. El Adulto Responsable autoriza explícitamente a cada tutor con el que el menor puede tomar clase (**Autorización de tutor**). El tutor concentra su perfil público, su foto, sus temas, su tarifa y su disponibilidad; cada **Credencial académica** (título, certificado analítico o matrícula) tiene un estado de revisión (pendiente, aprobada, rechazada), y el **CAP** tiene además los estados en_revision_legal y ‘vencido‘. El CAP no es requisito para activar el perfil del tutor ni para reservarle una clase entre adultos: solo habilita a dar clases a menores, y sin un CAP
aprobado y vigente el tutor no aparece en las búsquedas de un menor ni se le puede reservar con uno (ADR-M1-04). Los administradores no son un tipo de usuario: **Admin** (admin.admins) es una entidad aparte, vinculada a un usuario, con exactamente uno de dos roles
(sección~[§sec:seguridad]).

En el módulo de reservas, el menor genera una **Solicitud de Sesión**: una entidad separada que no bloquea el horario ni genera cobro y que el
Adulto Responsable aprueba y paga para convertirla en una **Reserva**.
La Reserva vincula a quien paga, a quien recibe la clase y al tutor; congela el precio y la duración (de 30 a 180 minutos en bloques de 30) y recorre los estados pendiente_pago, ‘confirmada‘, en_curso, ‘finalizada‘, ‘cancelada‘ y tres variantes de ausencia (no_show_estudiante, no_show_tutor y no_show_doble). Un **Paquete**
mensual agrupa cuatro Reservas que se pagan juntas. Cada Reserva tiene a lo sumo una **Sesión** de aula (1 a 1), que guarda la asistencia y el estado de la clase –no una grabación–, y puede originar
**Alertas de seguridad** del kill-switch. En pagos, cada Reserva tiene su
**Transacción** con el estado del escrow (retenido, liberado, reembolsado o pausado por denuncia); en un paquete, un único pago de
MercadoPago genera una Transacción por clase. Completan el modelo el
**Resumen** de la sesión, la **Calificación** bidireccional, la
**Denuncia** (con la evidencia que adjunta el denunciante, si la hay) y la **Sanción**.

**Relaciones clave:** un Adulto Responsable $$ uno o más menores; un tutor $$ varias Reservas; una Solicitud de Sesión
$$ a lo sumo una Reserva; una Reserva $$ una Sesión
(1 a 1) y una Transacción; una Sesión $$ cero o más
Calificaciones, Alertas y Denuncias.

**Integridad:** dos restricciones de exclusión a nivel de base de datos (no solo validación de aplicación) impiden dos Reservas no canceladas cuyos rangos horarios se superpongan, una para el mismo tutor y otra para el mismo alumno, dado que una validación exclusivamente en el backend es vulnerable a condiciones de carrera cuando dos solicitudes llegan casi simultáneamente.

## Diseño y experiencia de usuario (UX/UI)

El onboarding de Términos y Condiciones reemplaza el documento de scroll continuo por un paso propio del registro, “Cómo funciona Tinku”, con los puntos clave de los términos –incluido el funcionamiento de la plataforma– presentados como tarjetas: cada una tiene un título corto y grande, un párrafo breve y una ilustración al costado que representa el concepto. Los puntos cubren que Tinku conecta pero no dicta las clases, la verificación de identidad, que las recomendaciones son una ayuda y no una garantía, el pago retenido hasta después de la clase, la protección de los menores, que las clases no se graban salvo el audio del resumen contratado, y la minimización de datos. El tutor ve un conjunto propio, escrito desde su lado: que es independiente y fija su precio, la verificación de su identidad y de su formación contra registros oficiales, la foto obligatoria, cómo y cuándo cobra, los requisitos para dar clases a menores, la grabación del audio solo si habilita el resumen, y cómo se construye su reputación. Los plazos que se citan salen de la Tabla de Tiempos, nunca escritos a mano. Al final, un checkbox de aceptación explícita, desactivado por defecto, habilita el paso siguiente. La foto de perfil del tutor es obligatoria: sin ella no aparece en búsquedas ni recomendaciones, porque alumnos y familias tienen que ver con quién toman clase. La interfaz se diferencia según el rol: la de un menor no muestra ni expone controles de las acciones reservadas al adulto –pago, autorización de tutores, denuncias–, y esa restricción opera tanto en el diseño de interfaz como en los permisos de la API, no solo a nivel visual. El aula degrada la calidad ante una conectividad deficiente (video, luego solo audio, luego texto), y los mensajes de texto viajan por el canal de datos de la propia sala de
LiveKit.

En accesibilidad, el MVP no incluye un módulo completo
(capítulo~[§cap:introduccion], sección~[§sec:alcance]), pero aplica buenas prácticas básicas: contraste adecuado, tamaños de fuente legibles y navegación con foco visible, verificadas de forma automática con axe-core en las pruebas del frontend. La validación del diseño con usuarios se apoya en las entrevistas y encuestas ya definidas en el capítulo~[§cap:metodologia], y en UAT con el grupo piloto
(OE8).

<!-- Figura: Mockups de pantallas principales -->

## Decisiones incorporadas durante la implementación

El diseño inicial de Tinku –el que describen los capítulos~[§cap:introduccion] a~[§cap:marco-teorico] y las primeras versiones de este capítulo– se ajustó durante la construcción. Los cambios responden a cuatro causas: las restricciones de un único desarrollador y un presupuesto de 0 a 100 USD mensuales, que obligaron a elegir en cada caso la opción más simple de operar; la seguridad del menor, que prevalece sobre cualquier funcionalidad; la minimización de datos, que impide guardar lo que ninguna regla de negocio necesita; y las fallas observadas al poner el sistema en producción. Cada decisión quedó registrada como un ADR en el repositorio del sistema (anexo~[§anx:repositorios]), donde se documentan las alternativas evaluadas y los riesgos aceptados. La tabla~[§tab:decisiones-implementacion] es el registro central de esos cambios: los demás capítulos remiten a ella. Las filas cuyo diseño original dice “—” son decisiones nuevas, sin un antecedente en el diseño inicial.

{

| **Tema** | **Diseño original** | **Lo implementado** | **Fundamento** |
| --- | --- | --- | --- |
| Estilo arquitectónico | Cliente-servidor en capas; la IA, incluido el matching, delegada a proveedores externos | Monolito modular de nueve módulos más un único servicio propio aparte, el motor de matching en Python. Comunicación síncrona en proceso y eventos de dominio en memoria, sin *broker*; plazos de negocio con Quartz persistido en la base | Constitución, art.~VIII a X; ADR-000-01, ADR-000-02 |
| Hosting | Supabase (base), Vercel (frontend), Upstash (Redis); backend en la computadora propia y migración a un VPS alquilado antes del piloto | Todo en un servidor propio con Coolify (contenedores de base con pgvector, matching, backend y frontend), publicado por Cloudflare Tunnel; copia diaria cifrada en Cloudflare R2 (14 días); imágenes construidas por GitHub Actions | ADR-000-07: Vercel gratuito no admite uso comercial; un solo proveedor; costo dentro del techo. Se acepta el punto único de falla para el piloto |
| Redis | Estado de chat y de salas, *rate limiting* | Sin Redis: límites por IP y bloqueo de login en memoria del proceso; estado de la sala en LiveKit y en la base; sin módulo de chat | ADR-000-04 (D8): una dependencia menos con una sola instancia |
| Índice semántico | FAISS en memoria | pgvector en la misma base; modelo ‘paraphrase-‘‘multilingual-‘‘MiniLM-L12-v2‘ (384 dimensiones); el puntaje de un tutor es su máxima similitud con cada uno de sus temas | ADR-M2-01 (sin índice que reconstruir), ADR-M2-03 |
| Orden de los resultados | Similitud y reputación combinadas | La similitud se calcula contra cada tema del tutor, no contra todos juntos, para que quien enseña muchos temas no quede relegado. La reputación solo desempata entre tutores de relevancia parecida, y los resultados por debajo de un mínimo de relevancia no se muestran | ADR-M2-02, ADR-M2-03 |
| Recomendaciones | — | Las puntuaciones funcionan como un sistema de recomendación, no como un aval; un tutor nuevo arranca sin calificaciones y la decisión de con quién aprender es siempre del alumno o de su adulto responsable | ADR-M1-06 (decisión 2), ADR-M2-02 |
| LLM del resumen | GPT-4o o Gemini 2.0 Flash, a confirmar; el audio enviado directo al modelo | Dos pasos: transcripción con ‘gpt-4o-mini-transcribe‘, anonimización y GPT-4o, que recibe solo texto. Sin configuración, no sale nada (*fail-closed*). Gemini se descartó por decisión del dueño del producto | ADR-M6-03 (FR-SUM-005: el audio no se puede anonimizar), ADR-M3-04 |
| Resumen automático | Servicio general para todas las sesiones | Adicional pago y opcional, solo entre adultos y con consentimiento de ambos; precio según la duración. Si el resumen no se genera, se reembolsa solo el adicional | Constitución v2.4; ADR-M3-04, ADR-M5-06 |
| Grabación | Ninguna | Única excepción a no grabar: solo audio, solo con el adicional, nunca con menores, con consentimiento de ambos y borrado al transcribir (24 horas como máximo). La graba el navegador del tutor porque la grabación del lado del servidor de LiveKit incluye solo 60 minutos gratuitos por mes | Constitución v2.4 (art.~V), ADR-M3-04 |
| Asistente conversacional de repaso | Objetivo específico del proyecto | No se implementó: no forma parte de los nueve módulos. Queda como trabajo futuro | Constitución, art.~VI (alcance cerrado) |
| CAP | Optativo con mejora de visibilidad, u obligatorio para todos los tutores | Obligatorio y vigente (12 meses) solo para dar clases a menores, con revisión manual del rol de Moderación y Seguridad. Al vencer, se cancelan las clases futuras con menores con reembolso total. La verificación de la firma digital del CAP queda diferida | ADR-M1-04, enmienda v2.3; FR-ID-021 a FR-ID-026. A quien enseña solo a adultos no se le pide (minimización) |
| Verificación de identidad | OCR con Tess4J y revisión manual del DNI | Tesseract invocado como programa del sistema en el propio servidor; controla mayoría de edad, nombre y unicidad del DNI; la imagen no sale del servidor ni se guarda. La revisión manual existe solo para la credencial académica y el CAP | ADR-M1-01; ADR-M1-08 (Tess4J nunca funcionó en producción) |
| Especialidades y triaje de credenciales | Presentados como implementados en versiones anteriores de este capítulo | Decidido y **pendiente de implementar**: especialidades verificadas o declaradas y triaje automático contra registros oficiales (tareas T-ESP-01 a T-ESP-04). Hoy el rol de Moderación aprueba la credencial manualmente | ADR-M1-06 |
| Kill-switch | Una sola rama (cortar y bloquear); desenfoque del video entre adultos | NSFWJS en el navegador sobre el video remoto (cámara y pantalla), buffer rotativo de 30 segundos que se descarta salvo disparo. Con un menor corta directo, sin preguntar; entre adultos oculta el video del detectado y pide confirmación a la contraparte (plazo de 5 minutos). Evidencia: clip de 30 segundos que se sube solo ante un disparo y se conserva 30 días desde la resolución de la Alerta | ADR-M3-01, ADR-M3-07; Tabla de Tiempos |
| Denuncias | Suspensión preventiva al denunciar; evidencia de la sesión preservada | La denuncia entra en revisión con 48 horas de descargo del denunciado y pausa el escrow de esa sesión; evidencia opcional que adjunta el denunciante; el denunciado no conoce su identidad. La suspensión automática existe solo en las Alertas del kill-switch | Spec M9; minimización (no hay grabación que preservar) |
| Menores | El menor puede reservar con un tutor autorizado | El menor tiene cuenta propia pero no paga, no autoriza tutores ni denuncia: pide una Solicitud de Sesión que su Adulto Responsable aprueba y paga. El piloto corre **sin menores**: la opción tinku.menores.sesiones-habilitadas queda apagada hasta cerrar el kill-switch en el cliente (T-M3-06) y el CAP (T02) | Constitución, art.~II; T-TES-10 |
| Cobro | escrow que retiene los fondos en la cuenta de la plataforma; SDK oficial de Java; reparto por OAuth “abierto” | Modelo A: cada tutor conecta su cuenta de MercadoPago por OAuth (con PKCE); la preferencia se crea con su token y el dinero entra a su cuenta; Tinku cobra su comisión con marketplace_fee. El escrow es una ventana lógica de 24 horas en la que Tinku todavía puede reembolsar. Cliente HTTP propio, sin SDK | ADR-M5-02: Tinku no recauda fondos de terceros |
| Comisión | 27 % con la pasarela como costo de la plataforma | 27 % sobre el bruto de cada sesión (BR-PAG-01), a cargo del tutor; MercadoPago descuenta su comisión (cerca del 6,04 %) de los fondos del tutor, que recibe el 66,96 % | ADR-M5-05, que declara la discrepancia con el modelo económico del capítulo~[§cap:economica] |
| Reembolsos | Siempre totales, nunca parciales | Totales como regla general. Excepciones: el adicional de resumen (BR-PAG-11) y la clase de un paquete devuelta por falta del tutor (FR-PAG-022); parciales manuales por disputa (FR-PAG-010) | Spec M5, FR-PAG-009 (enmienda v2.5) |
| Paquete mensual | — | Cuatro clases semanales con un solo pago, vigencia de cuatro semanas y un descuento de 0 a 30 % que fija el tutor | ADR-M5-03 |
| Duración de la clase | Estándar de 60 minutos | De 30 a 180 minutos en bloques de 30, la elige quien reserva; piso de tarifa de USD~4 por hora ($6.140) | FR-RES-023; BR-PAG-04 |
| Reservas y cambios de horario | — | Se reserva hasta 30 minutos antes de la clase, para que el pago (que puede tardar hasta 15 minutos en confirmarse) llegue con margen. Con menos de 24 horas se puede cambiar de horario sin volver a pagar hasta una hora antes; el horario liberado queda abierto a otra reserva. Con menos de una hora el cambio se rechaza y la clase sigue en pie | Tabla de Tiempos; FR-RES-016 |
| Foto de perfil del tutor | — | Obligatoria: sin foto el tutor no aparece en búsquedas ni recomendaciones | FR-ID-028 |
| Catálogo de contenidos | Catálogo cerrado | Sigue cerrado y curado, pero *vivo*: se cuentan de forma agregada los temas buscados sin un tutor que los dé (un contador por tema, sin datos de quién buscó, sin las búsquedas de menores, con un máximo de 500 temas) y el rol de administración incorpora los más pedidos | ADR-M2-04 |
| Búsqueda sin coincidencia exacta | — | Si nadie enseña exactamente lo buscado, se reconoce el área del tema (materia y nivel) y se recomiendan tutores de esa área, aclarando que no es una coincidencia exacta; el nivel escrito en la búsqueda se toma como filtro | ADR-M2-04 |
| Términos y Condiciones | Documento de scroll continuo | Paso propio del registro con los puntos clave en tarjetas y aceptación explícita, que incluye el consentimiento de la grabación del audio del resumen | ADR-M3-05 |
| Correo transaccional | — | Resend (plan gratuito) por HTTP, con una cola de salida en la base y reintentos por Quartz; sin configuración no envía | ADR-000-06 |
| Pruebas | Jest en el frontend; cobertura mínima del 70 % por módulo | Backend: JUnit 5 y Testcontainers con PostgreSQL real; frontend: Playwright (con la API simulada) y axe-core, más oxlint; pruebas del motor de matching y prueba nocturna contra el sistema completo. Cobertura medida con JaCoCo, sin umbral que corte la construcción | ADR-000-05 |
| Roles | ADMIN como un rol más de Usuario, con un rol único de administración | Usuario de tipo ADULTO, MENOR o TUTOR; el administrador es una entidad aparte con uno de dos roles: Moderación y Seguridad, o Soporte Financiero | Spec M8 (FR-ADM-008) |
| Monitoreo | Paneles de Supabase y Upstash | Panel propio “Salud de Infraestructura” en la administración, más los paneles de Coolify y LiveKit | ADR-M8-01 |
| Versiones | — | Spring Boot 4.1.1 y Next.js 16.3.6, para mantener parches de seguridad durante el piloto | Apéndice~[§apx:tecnicos] |

}

## Seguridad, calidad y despliegue

### Seguridad

La autenticación se resuelve con JWT emitido por el propio backend a través de Spring Security, con contraseñas almacenadas mediante hash bcrypt y sin un proveedor externo de identidad, por el motivo ya explicado en la sección~[§sec:stack-backend]. Los pedidos públicos
(registro, login, recuperación de contraseña, verificación del DNI y webhooks) tienen un límite por IP y el login se bloquea tras varios intentos fallidos. El control de accesos distingue el tipo de usuario
(ADULTO, MENOR, TUTOR) y, para la administración, los dos roles de Admin
–*Moderación y Seguridad* (credenciales, CAP, alertas del kill-switch, denuncias y sanciones) y *Soporte Financiero* (pagos fallidos y tabla de precios)–, con colas y permisos separados y un registro de auditoría de cada acción. Las restricciones del menor (sección~[§sec:modelo-datos]) se implementan como reglas de autorización explícitas en cada endpoint, no como una restricción de interfaz que pudiera sortearse llamando directamente a la API.
Además, mientras dure el piloto, las clases con menores están apagadas: la creación de Reservas y de Solicitudes de Sesión con un menor se rechaza hasta que se habiliten de forma explícita, una vez cerrados el kill-switch en el cliente y el circuito del CAP.

Toda la comunicación desde internet viaja cifrada con TLS hasta Cloudflare y por el túnel cifrado hasta el servidor, y el backend usa HTTPS con los servicios externos. Los tokens de MercadoPago de los tutores se guardan cifrados con AES-256-GCM con una clave que no vive en la base
(ADR-M5-02), y las copias de la base se cifran antes de salir del servidor (ADR-000-07).

La verificación de identidad lee el DNI mediante OCR con
Tesseract, que el backend ejecuta como programa del sistema dentro del propio servidor: la imagen se escribe en un archivo temporal que se borra al terminar, nunca se envía a terceros ni se guarda. El OCR controla la mayoría de edad de todo adulto –rechaza automáticamente a cualquier tutor menor de 18 años–, el nombre y que el DNI no esté ya registrado; no hay una revisión manual del DNI. La integración original usaba la librería Tess4J dentro del proceso Java; se reemplazó porque en producción nunca llegó a funcionar –las librerías nativas de la imagen del servidor no eran compatibles– y ninguna persona real podía completar el registro (ADR-M1-08).

La credencial académica la revisa hoy manualmente el rol de Moderación y
Seguridad. Como un PDF se falsifica en minutos, lo que prueba un título es el registro oficial que lo respalda: el Registro Público de Graduados
Universitarios para títulos universitarios desde 2012 [rpgu], el
Registro Federal de Egreso (ReFE) con el código QR de Mi Argentina para títulos secundarios y superiores digitales desde noviembre de 2023
[refe], el validador de SIU-Guaraní para certificados de alumno regular y los buscadores de cada colegio para las matrículas. Como ninguno de esos registros ofrece una API pública, se decidió (ADR-M1-06) combinar un triaje automático –rechazo inmediato de lo que claramente no es un título, lectura por OCR del nombre para compararlo con el del
DNI y control de que el enlace de verificación pertenezca a un dominio oficial– con la decisión final del administrador contra el registro, y asociar cada credencial a especialidades verificadas o declaradas. Esa decisión está tomada pero **pendiente de implementar**
(sección~[§sec:decisiones-implementacion]). La verificación del
CAP vigente es manual y solo se exige a quienes dan clases a menores.

El kill-switch de seguridad, presentado como SafeVchat en la sección~[§sec:estado-del-arte], se apoya en el clasificador NSFWJS, que corre sobre TensorFlow.js en el navegador de cada participante durante la videollamada (ADR-M3-01). Cada cliente clasifica el video que
*recibe* –cámara y pantalla compartida del otro–, de modo que el clasificador que protege al menor corre en el dispositivo del menor y un cliente modificado del otro lado no puede apagarlo. Una detección se confirma con tres muestras consecutivas por encima de un umbral de 0,85
(ADR-M3-07). Mientras tanto, el navegador mantiene un buffer rotativo de
30 segundos de video que vive solo en memoria y se descarta salvo disparo. Ante una detección confirmada, el sistema ejecuta una de dos ramas: si hay un menor presente, corta la clase de inmediato sin preguntarle nada a nadie y el tutor implicado queda suspendido preventivamente; si ambos participantes son adultos, oculta el video del detectado y le pregunta a la contraparte si quiere cortar, con un plazo de 5 minutos: sin respuesta se restaura el video y no se genera una
Alerta. Solo ante un disparo se sube como evidencia el clip de 30
segundos (sin audio), que se conserva 30 días desde la resolución de la
Alerta; la Alerta la revisa el administrador de Moderación y Seguridad dentro de las 12 horas. El diseño inicial preveía un filtro de desenfoque en la rama de adultos; se reemplazó por ocultar el video, que no deja a la vista ninguna parte de la imagen.

Las denuncias siguen un circuito separado de las Alertas (Spec M9): la presenta un adulto –el menor nunca, lo hace su Adulto Responsable–, con un motivo de una lista cerrada y la evidencia que el denunciante quiera adjuntar. El denunciado recibe el motivo sin conocer la identidad de quien denunció y tiene 48 horas para su descargo; si la sesión tiene dinero en la ventana de escrow, se pausa la liberación de esa sesión. La decisión final es del administrador de Moderación y
Seguridad. Una denuncia no suspende por sí sola al denunciado: la suspensión preventiva automática existe únicamente en el circuito del kill-switch. Tampoco hay evidencia de la sesión que preservar, porque las clases no se graban; el diseño inicial suponía lo contrario, lo que habría exigido una grabación continua incompatible con la minimización de datos.

La protección de datos personales sigue la Ley 25.326, con especial cuidado en el procesamiento de video de menores y en la definición de una política de retención y baja de datos a solicitud del titular o su responsable.

### Calidad y pruebas

Las pruebas del backend se escriben con JUnit 5 y Mockito, y las de integración corren con Testcontainers contra una base PostgreSQL real con pgvector, la misma imagen que se usa en producción. Las del frontend son pruebas de punta a punta con Playwright, que simulan la API del backend, e incluyen controles automáticos de accesibilidad con axe-core; el código del frontend se revisa además con el analizador estático oxlint. El motor de matching tiene sus propias pruebas en Python.
El diseño inicial preveía Jest para el frontend, que no se usa: las pruebas del frontend quedaron en Playwright, que ejercita los flujos completos en un navegador real, el mismo entorno en el que corren el kill-switch y el aula.

La metodología (capítulo~[§cap:metodologia]) fijaba una cobertura mínima del 70 % por módulo. En la implementación la cobertura se mide con JaCoCo sobre todo el backend, sin un umbral que corte la construcción: primero se mide y después se decide (ADR-000-05). Al
14/10/2026 la suite del backend sumaba 661 pruebas sin fallas y una cobertura de líneas del 85,6 %. La suite exige JDK~21 y se ejecuta con
‘./mvnw -B test‘ (apéndice~[§apx:tecnicos]). Las UAT se realizan con el grupo piloto, según lo definido en el capítulo~[§cap:metodologia] y el OE8. Los resultados se reportan en el capítulo~[§cap:resultados].

### Despliegue

El control de versiones se lleva en GitHub, con una rama por bloque de trabajo y revisión antes de integrar a la rama principal, que es la de producción y solo acepta cambios por *pull request* con las pruebas en verde. El pipeline de CI/CD corre en GitHub Actions con cinco flujos: ‘ci-backend‘ (pruebas del backend con Tesseract instalado y publicación del reporte de cobertura), ‘ci-frontend‘ (oxlint y
Playwright), ‘ci-matching‘ (pruebas del motor), ‘ci-e2e‘
(una prueba nocturna que levanta la base, el motor y el backend reales y recorre por la API el registro, la búsqueda semántica, la reserva y el pago en modo de prueba hasta la confirmación) y ‘deploy‘, que en cada integración a la rama principal vuelve a correr las tres suites, publica las imágenes de los contenedores en GitHub Container Registry y llama al webhook de despliegue de Coolify. Las imágenes nunca se construyen en el servidor de producción; para volver atrás, alcanza con desplegar la imagen anterior.

El monitoreo se apoya en el panel propio “Salud de Infraestructura”
de la administración, que consulta en vivo el estado de la base, el motor de matching, MercadoPago, LiveKit y el OCR (ADR-M8-01), más los paneles de Coolify (estado y recursos de cada contenedor) y de LiveKit
Cloud. Un sistema de monitoreo unificado, como Grafana, queda fuera del alcance del MVP.

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

Todos los cálculos se apoyan en un modelo financiero parametrizado, en el cual el VAN, la TIR y los períodos de repago se calculan con las expresiones de la sección~[§sec:indicadores-formulas]. Esto permite que al modificar cualquier supuesto de entrada —el ticket promedio, la comisión, las horas de desarrollo o el volumen de sesiones— los tres escenarios, el VAN y la TIR se recalculen de forma inmediata.
Cada parámetro de entrada se declara en las tablas de este capítulo, con su origen, de modo que todos los resultados son reproducibles a partir de ellas.

Los parámetros que dependen del funcionamiento de la plataforma
—comisión, reparto del cobro con MercadoPago, piso de tarifa, duración de las clases, precio del resumen y paquete mensual— se tomaron del sistema efectivamente implementado y de sus registros de decisión de arquitectura (ADR), que viven en el repositorio del sistema (anexo~[§anx:repositorios]). Una versión anterior de este capítulo suponía que la plataforma pagaba la comisión de MercadoPago; el sistema implementado no funciona así
(sección~[§sec:costos-variables]), y todas las cifras de este capítulo se recalcularon con el reparto real.

## Justificación institucional, legal, ambiental y social

El desarrollo de Tinku se fundamenta en un impacto transversal comprobable:

- **Justificación social:** el proyecto busca democratizar el acceso al apoyo escolar, eliminando las barreras geográficas que afectan especialmente a estudiantes en comunidades rurales o del interior del país. A su vez, propone formalizar el mercado de tutorías particulares, el cual opera mayormente en la informalidad.
- **Justificación legal e impositiva:** el modelo de contratación se apoya en el Código Civil y Comercial de la
          Nación (artículos 25, 26, 682 y 690), exigiendo que la cuenta pagadora pertenezca siempre a un adulto responsable para resguardar patrimonialmente a los menores. En materia impositiva, el cobro se resuelve con MercadoPago Marketplace en el llamado *modelo A* (ADR-M5-02): cada tutor conecta su propia cuenta de MercadoPago, el dinero de la clase ingresa a esa cuenta y la plataforma percibe únicamente su comisión, mediante el campo ‘marketplace_fee‘ del pago. Tinku no recauda ni retiene fondos de terceros: el escrow es una ventana lógica de 24 horas durante la cual la plataforma todavía puede ordenar un reembolso. Se descartó la alternativa de recaudar todo en la cuenta de la plataforma y transferir luego a cada tutor porque hacía ingresar el monto bruto de todas las clases como ingreso propio, con su carga impositiva, y obligaba a transferencias manuales semanales (ADR-M5-02). La formalización que el sistema aporta es otra: cada cobro queda registrado en la cuenta del tutor y la plataforma le permite exportar sus cobros del mes, con los datos del adulto pagador, para facturar y declarar ante la ARCA (ex AFIP). Asimismo, la plataforma aplica el principio de minimización de datos para cumplir estrictamente con la Ley de
          Protección de Datos Personales (Ley 25.326).
- **Justificación institucional:** Tinku se desarrolla como el proyecto final de la carrera de Ingeniería en
          Informática, demostrando la aplicación de tecnologías de vanguardia (IA y WebRTC) para resolver una problemática concreta del sistema educativo argentino.
- **Justificación ambiental:** al centralizar el apoyo académico en un ecosistema digital y virtual, se elimina la necesidad de desplazamiento físico de alumnos y tutores, reduciendo la huella de carbono asociada al transporte. A nivel de infraestructura tecnológica, se dimensiona al mínimo: todos los servicios propios (base de datos, motor de matching, backend y frontend) corren como contenedores en un único servidor preexistente administrado con Coolify, sin réplicas ni entorno de pruebas duplicado, y las imágenes se construyen fuera de él, en
          GitHub Actions (ADR-000-07). La detección de contenido inapropiado del kill-switch se ejecuta en el navegador de cada participante y no en el servidor.

## Modelo de monetización y alternativas descartadas

El ingreso que se modela proviene de una única fuente: una
**comisión de plataforma del 27 % sobre el precio de cada sesión** (regla BR-PAG-01 del sistema, ADR-M5-05), descontada exclusivamente del pago que recibe el tutor. El ticket promedio se fija en
**USD 7,42 por sesión**, derivado del relevamiento de precios de
Superprof descripto en la sección~[§sec:origen-ticket]. El estudiante abona el precio final fijado por el docente, sin cargos de servicio visibles: la comisión nunca aparece como línea aparte. El único cargo adicional es el resumen automático, opcional y de precio a costo
(sección~[§sec:adicional-resumen]), que no se incorpora al flujo de fondos. Se excluyen explícitamente vías de ingreso como la publicidad, la venta de datos o las suscripciones premium durante la etapa de MVP.

Además de la clase suelta, el sistema ofrece un **paquete mensual**
de cuatro clases semanales, con una vigencia de cuatro semanas y un único pago (ADR-M5-03). El tutor decide si lo habilita y puede aplicarle un descuento de 0 a 30 % sobre su precio por hora, sin quedar por debajo del piso de tarifa (sección~[§sec:piso-tarifa]); la comisión se calcula clase por clase sobre el precio con descuento. El paquete no agrega una fuente de ingreso: es la misma comisión sobre un ticket eventualmente menor. Como no hay datos de su adopción, el modelo base no lo incluye y su efecto se evalúa como sensibilidad del ticket
(sección~[§sec:sensibilidad]).

Durante el diseño del modelo de negocio se evaluaron y descartaron dos metodologías alternativas de intermediación:

- **Suscripción mensual al estudiante (modelo Superprof):** se descartó porque la imposición de una barrera de entrada fija contradice el objetivo principal de reducir la fricción económica para familias de bajo poder adquisitivo.
          Adicionalmente, no genera un ingreso proporcional al valor efectivo entregado en cada sesión.
- **Comisión de alta retención en el extremo superior del mercado (33 %):** se descartó replicar las bandas tarifarias máximas de Preply. Una comisión percibida como excesiva incentiva la desintermediación —acuerdos de pago por fuera de la plataforma tras el primer contacto— lo cual erosiona los ingresos y vulnera el modelo de confianza diseñado.

### Origen del ticket promedio

El ticket no es un supuesto: se obtuvo relevando 414 avisos de apoyo escolar publicados en Superprof Argentina [superprof], la plataforma de referencia del segmento. La suma de los precios horarios declarados fue de $5.544.467 y el promedio de $13.392,43 por hora
(mediana $12.000; detalle en el apéndice~[§apx:precio]). Como el modelo trabaja con una duración media de 51 minutos por sesión
(ecuación~[§eq:duracion]), el precio horario se pondera por
$51/60 = 0{,}85$ y se convierte a dólares al tipo de cambio de
$1.535 por USD, el mismo con el que el sistema expresa en pesos el piso de tarifa (sección~[§sec:piso-tarifa]) y el precio del resumen (BNA,
09/09/2026; estimación propia declarada como tal):

    Ticket = 13.392{,43 0{,}85}{1.535} = USD~7{,42}.

El tipo de cambio es un parámetro del modelo y no un dato: la sensibilidad del resultado frente a él se presenta en el apéndice~[§apx:precio].

### Calibración de la comisión

La comisión se calibró en tres etapas, y la última cambia el sentido del
27 %. Una primera formulación del modelo adoptó una comisión del
15 %, valor que posiciona a la plataforma por debajo de toda la banda de
Preply (18 % a 33 %) [preply]. Sin embargo, al incorporar al modelo los costos financieros de la pasarela de pago y proyectar un volumen de demanda realista para un MVP, esa comisión arrojaba un
VAN negativo en los tres escenarios.

La comisión se recalibró entonces al 27 %. En esa versión del modelo la comisión de MercadoPago (6,04 %) se restaba como un costo de la plataforma y, con un ticket de USD 7 y un costo de IA imputado a cada sesión, el VAN del escenario base se anulaba con una comisión de aproximadamente 26,9 %: el 27 % era, en efecto, el mínimo necesario. Con el ticket actualizado a USD 7,42 y el costo de IA
fuera de la sesión, ese umbral había bajado a aproximadamente 25,3 %.

Ambas cifras quedaron superadas. El sistema implementado cobra con el modelo A (ADR-M5-02), en el que MercadoPago descuenta su comisión de los fondos del tutor y la plataforma recibe el 27 % completo
(sección~[§sec:costos-variables]); además, la partida fija de procesamiento de LLM se eliminó por no tener contraparte en el sistema (sección~[§sec:costos-recurrentes]). Con el modelo corregido, el VAN del escenario base se anula con una comisión de
**aproximadamente 18,2 %**. La afirmación anterior de que el
27 % era el mínimo para que el proyecto se justificara deja, por lo tanto, de ser cierta: el 27 % se mantiene como una decisión del dueño del producto (ADR-M5-05) con un margen de unos nueve puntos porcentuales sobre el equilibrio del escenario base, cuyo fundamento se expone en la sección~[§sec:fundamento-comision].

### Unidad de cobro y duración de las sesiones

El tutor fija un precio por hora y quien reserva elige la duración de la clase entre 30 y 180 minutos, en bloques de 30 (regla FR-RES-023 del sistema); el precio de la sesión es el precio por hora multiplicado por la duración elegida y queda congelado en la reserva. La duración es, por lo tanto, económicamente relevante: el ticket por sesión crece con ella, y también el costo de IA del resumen opcional, que escala con los minutos de audio procesados y no con la cantidad de sesiones.

El sistema no fija una duración típica y, antes del piloto, no hay datos de la distribución real. El modelo trabaja con una **duración media supuesta**, que se declara como estimación propia: se asume que un
30 % de las sesiones usa el bloque mínimo de 30 minutos y el resto dura
60 minutos, de modo que la duración promedio ponderada resulta:

    d = 60 (1 - 0{,}30) + 30 0{,}30 = 51  minutos.

Las clases de 90 a 180 minutos que el sistema admite no se incluyen en la mezcla; si se dictaran, elevarían el ticket promedio. La sensibilidad del resultado frente a la duración media se presenta en la sección~[§sec:sensibilidad].

El ticket promedio de USD~7,42 se interpreta como el promedio ya ponderado sobre esa misma mezcla de duraciones y precios horarios. El procesamiento de IA no se imputa a cada sesión: es un servicio opcional que quien paga contrata y que se cobra aparte, tal como se describe a continuación.

### Piso de la tarifa por hora

El precio lo fija el tutor, pero el sistema no le permite fijar un precio por hora inferior a un piso de **USD 4 por hora**, expresado en pesos: **$6.140** al tipo de cambio de $1.535 (regla BR-PAG-04).
El valor es un parámetro que un administrador revisa una vez por mes, sin consumir una API de tipo de cambio, y no es retroactivo: una tarifa ya guardada por debajo sigue vigente hasta que el tutor la edita. El descuento del paquete mensual tampoco puede llevar el precio por hora por debajo del piso.

El modelo permite cuantificar qué protege ese piso y qué no. Una clase de duración media (51 minutos) al piso cuesta USD~3,40; con el reparto del modelo A (sección~[§sec:costos-variables]) le deja a la plataforma
USD~0,918 (USD~1,08 por hora de clase) y al tutor USD~2,28, una vez descontada la comisión de MercadoPago. Si todas las sesiones de cada escenario se dictaran al piso:

- en el **escenario base**, la comisión cubriría los costos fijos de todos los años (bastaría un precio de USD~2,26 por hora), pero no recuperaría la inversión: el VAN sería de
          USD~-12.340;
- en el **escenario pesimista**, la comisión ya no cubriría los costos fijos del Año 2 (flujo de USD~-40): el precio por hora que los cubre en todos los años de ese escenario es de aproximadamente USD~4,04, prácticamente el piso.

El piso, entonces, no garantiza la viabilidad del proyecto, que depende del ticket promedio: el VAN del escenario base se anula con unos
USD~5,87 por hora (sección~[§sec:sensibilidad]), por encima del piso.
Lo que el piso asegura es una cota inferior: con un volumen como el del escenario pesimista, una tarifa por debajo de él dejaría a la comisión sin cubrir siquiera los costos fijos de operación. Esa es la lectura que sostiene el cálculo de la afirmación con la que el sistema fundamenta la regla («por debajo, la comisión no cubre la operación»).

### Resumen automático como adicional opcional

Al reservar una clase, quien paga puede sumar un resumen automático de la sesión (transcripción y síntesis por IA). Es un servicio opcional, disponible solo en clases entre adultos y con el consentimiento de ambas partes —con un menor nunca se contrata ni se graba—, y su precio se fija a costo más un 50 % (ADR-M5-06):

    P_{resumen}(d) = 1{,}50 C_{IA}(d),
           C_{IA}(d) = c_{t} d + c_{e} d + c_{s} ,

donde $d$ es la duración de la clase en minutos, de modo que el precio
**crece con la duración** y no es un monto fijo. Los parámetros, con su fuente, son los de la tabla~[§tab:parametros-ia].

**Tabla:** Parámetros del costo de ia

     del resumen

| **Parámetro** | **Origen** | **Valor** |
| --- | --- | --- |
| $c_t$ — transcripción (por minuto) | Tarifa de lista de ‘gpt-4o-mini-transcribe‘, estimada en USD 0,003 por minuto [openaitranscribe2026] | 0,0030 |
| $c_e$ — entrada del LLM (por token) | Tarifa de lista de GPT-4o: USD 2,50 por millón de tokens [openaipricing2026] | $2{,}510^{-6}$ |
| $$ — tokens de transcripción por minuto | Estimación propia: unos 13.000 tokens por hora de clase (10.000 a 15.000 según el diseño del módulo), redondeada a 217 por minuto, el valor que usa el sistema | 217 |
| $c_s$ — salida del LLM (por token) | Tarifa de lista de GPT-4o: USD 10,00 por millón de tokens [openaipricing2026] | $110^{-5}$ |
| $$ — tokens de salida y de instrucciones | Estimación propia: resumen de cinco puntos (unos 800 tokens) más instrucciones fijas | 840 |

Con esos valores, el costo de IA es de unos USD 0,22 por hora de clase, de los cuales unos USD 0,18 corresponden a la transcripción. La tabla~[§tab:precio-resumen] muestra el precio resultante según la duración, convertido al tipo de cambio de $1.535 por USD y redondeado hacia arriba a la decena de pesos; los montos en pesos son los que cobra el sistema. El adicional ingresa **íntegro a la plataforma**: se suma al ‘marketplace_fee‘ de la sesión y la comisión del 27 % no se calcula sobre él (regla BR-PAG-11). La comisión de MercadoPago sobre el adicional, en cambio, se descuenta de los fondos del tutor junto con la de la clase (modelo A, ADR-M5-02): son USD~0,017 en una clase de duración media. Por eso la columna final es el margen de la plataforma, precio menos costo de IA, sin descontar la pasarela.

**Tabla:** Costo y precio del resumen según la duración de la clase

| **Duración** | **Costo de IA (USD)** | **Precio (USD)** | **Precio (ARS)** | **Margen de la plataforma (USD)** |
| --- | --- | --- | --- | --- |
| 30 min | 0,1147 | 0,1720 | 270 | 0,0573 |
| 51 min (promedio) | 0,1891 | 0,2836 | 440 | 0,0945 |
| 60 min | 0,2209 | 0,3314 | 510 | 0,1105 |
| 90 min | 0,3272 | 0,4908 | 760 | 0,1636 |
| 120 min | 0,4335 | 0,6502 | 1.000 | 0,2167 |
| 180 min | 0,6461 | 0,9691 | 1.490 | 0,3230 |

Tres consecuencias de este diseño son relevantes para la evaluación:

- **No es una fuente de ingreso relevante.** El adicional se fija a costo más un 50 %, y deja a la plataforma USD 0,0945
          por resumen de duración promedio. Si, a modo de referencia, se contratara en una de cada cinco sesiones del escenario base, el aporte sería de unos USD 165 anuales. Por eso
          **no se incorpora al flujo de fondos**: su función es ofrecer el servicio sin que el costo de IA recaiga sobre las sesiones que no lo usan.
- **El costo de IA sale de la economía unitaria de la sesión.** En la formulación anterior se imputaban USD 0,0255 a cada sesión, calculados con un costo de USD 0,03 por hora que la investigación de tarifas no respalda (el costo vigente es unas siete veces mayor). Al pasar a cobrarse aparte y en proporción a la duración, las sesiones sin resumen no cargan costo de
          IA y el margen unitario base sube en esa cantidad.
- **Riesgo de falla.** Si el resumen no llega a generarse, se reembolsa el monto exacto del adicional —una de las dos excepciones a la regla de reembolsos totales
          (sección~[§sec:reembolsos])—, pero el costo de transcripción ya incurrido no se recupera. Además, si MercadoPago prorrateara ese reembolso parcial entre el tutor y la plataforma, la diferencia que se le descuente al tutor la devuelve la plataforma por la cola de reembolsos manuales (ADR-M5-02, pendiente de verificar en el entorno de pruebas de MercadoPago).
          Nada de esto se cuantifica en el modelo base y se declara como una restricción del análisis; su magnitud es de centavos de dólar por incidente.

Las tarifas de lista se verificaron en fuentes secundarias y en la documentación del proveedor, y deben contrastarse con la página oficial de precios antes de fijar el monto definitivo, ya que se expresan en dólares y pueden cambiar.

## Estructura de costos

### Inversión inicial

La inversión inicial corresponde a las erogaciones necesarias para llevar el MVP a producción, concentradas en el semestre de desarrollo
(Año 0). Se compone del costo del equipo de desarrollo valorizado a tarifas de mercado según el perfil, los costos administrativos de puesta en marcha y una reserva de contingencia. La tabla~[§tab:inversion] presenta el desglose.

La partida de personal es una **valorización a precio de mercado**
y no una medición del esfuerzo real. El desarrollo efectivo lo lleva adelante un único desarrollador; la tabla estima cuánto costaría construir el mismo producto contratando los cuatro perfiles a tarifas de mercado, que es el costo de oportunidad relevante para evaluar la inversión con independencia de quién la ejecute. Las horas por perfil son, por lo tanto, una estimación propia del trabajo que el producto requiere, no un registro de horas trabajadas.

**Tabla:** Inversión inicial desglosada por rol y concepto (en USD)

| **Categoría** | **Concepto** | **Cant.** | **Valor unit.** | **Total** |
| --- | --- | --- | --- | --- |
| Personal | Senior — arquitectura, IA y WebRTC | 192 hs | 50 | 9.600 |
| Personal | Mid — backend y pasarela de pagos | 250 hs | 30 | 7.500 |
| Personal | Junior — frontend PWA e interfaz | 250 hs | 15 | 3.750 |
| Personal | Junior — UAT y pruebas | 120 hs | 15 | 1.800 |
| Infraestructura | Servidor propio preexistente y capas gratuitas (LiveKit, GitHub) | 6 meses | 0 | 0 |
| Administrativo | Registro de dominio | 1 año | 15 | 15 |
| Legal | Asesoría en privacidad de datos y TyC | único | 800 | 800 |
| Riesgo | Contingencia por imprevistos (10 % del desarrollo) | único | 2.265 | 2.265 |
| **Total inversión inicial** | **25.730** |  |  |  |

Las tarifas horarias por perfil (USD 50 para el rol senior, USD 30 para el semi-senior y USD 15 para los roles junior) se adoptan como estimación propia basada en valores de mercado para desarrollo remoto en la región, y se declaran como tal. Las horas asignadas a los perfiles mid y junior se dimensionaron considerando que el uso de un marco de desarrollo maduro para el backend (Java con Spring Boot, ADR-000-02), de una única base de datos PostgreSQL que también aloja el índice semántico (pgvector,
ADR-M2-01) y de bibliotecas de componentes para la interfaz reduce sustancialmente el trabajo de construcción desde cero.

La reserva de contingencia del 10 % sobre el costo de desarrollo se incorpora para absorber retrabajo, subestimación de horas y corrección tardía de defectos. Su inclusión responde a un criterio conservador: un presupuesto de desarrollo sin margen de imprevistos presenta un riesgo de desvío elevado.

La infraestructura durante el desarrollo no genera erogación en el
Año 0: todos los servicios propios corren en un servidor preexistente del desarrollador, administrado con Coolify y publicado mediante un túnel de Cloudflare, y los servicios de terceros se usan en sus capas gratuitas
(ADR-000-07). Esta decisión reemplazó al diseño inicial, que repartía la infraestructura entre Supabase (base de datos), Vercel (frontend) y un
VPS alquilado: el plan gratuito de Vercel no admite uso comercial y concentrar todo en un solo servidor simplifica la operación para un único desarrollador, dentro del presupuesto de infraestructura de USD 0 a 100
mensuales que el proyecto se fijó para el desarrollo. El costo aceptado es un único punto de falla —un corte de luz o de conectividad del servidor deja la plataforma fuera de línea—, mitigado con respaldos diarios cifrados fuera del servidor (a activar antes del piloto), y la decisión se revisa si la operación crece. Como referencia del costo alternativo de alquilar un VPS, uno de recursos medios de un proveedor local (8 vCore/16~GB) cuesta
USD~158,7 mensuales y los planes de entrada arrancan en USD~7,71
mensuales [lightnode2026].

### Costos recurrentes post-lanzamiento

Los costos operativos se proyectan mensualmente y se anualizan para el flujo de fondos. La tabla~[§tab:costos-fijos] muestra su evolución a lo largo del horizonte de evaluación.

**Tabla:** Costos fijos mensuales post-lanzamiento (en USD)

| **Categoría** | **Concepto** | **Año 1** | **Año 2** | **Año 3** | **Año 4** | **Año 5** |
| --- | --- | --- | --- | --- | --- | --- |
| Infraestructura | Servidor, base de datos y respaldos | 45 | 45 | 50 | 55 | 60 |
| Infraestructura | Transmisión de video (LiveKit) | 60 | 60 | 65 | 70 | 75 |
| Administrativo | Honorarios contables | 150 | 150 | 150 | 150 | 150 |
| Administrativo | Renovación de dominio | 1,25 | 1,25 | 1,25 | 1,25 | 1,25 |
| Comercial | Adquisición de usuarios | 40 | 50 | 60 | 70 | 80 |
| **Total mensual** | **296,25** | **306,25** | **326,25** | **346,25** | **366,25** |  |
| **Total anual** | **3.555** | **3.675** | **3.915** | **4.155** | **4.395** |  |

Tres decisiones de este cuadro merecen justificación explícita:

- **Sin partida fija de procesamiento de LLM.** Una versión anterior del cuadro incluía una partida de
          USD~55 a USD~70 mensuales de «procesamiento LLM
          (base)». El sistema implementado no tiene un consumo base de
          LLM: el único uso es el resumen automático, que se cobra aparte a costo más un 50 % a quien lo contrata
          (sección~[§sec:adicional-resumen]); los embeddings del matching se calculan con un modelo propio en el servidor y el OCR del documento de identidad también corre en él, sin API paga. La partida se eliminó: mantenerla imputaba un costo sin contraparte. Su efecto sobre los indicadores se muestra por separado en la sección~[§sec:sensibilidad].
- **Ausencia de equipo de soporte rentado.** El modelo no incorpora personal técnico contratado dentro de los costos fijos durante los cinco años proyectados. Con el volumen de sesiones proyectado, el escenario base admite como máximo unos
          USD~469 mensuales constantes de costo adicional antes de que el VAN se anule (sección~[§sec:sensibilidad]): a la tarifa junior de la tabla~[§tab:inversion] (USD~15 por hora) equivale a unas 31 horas mensuales, una dedicación parcial y no un equipo. El mantenimiento correctivo y evolutivo queda a cargo del equipo fundador. La incorporación de soporte pago se difiere hasta que el volumen efectivo de sesiones lo justifique, lo cual constituye una restricción operativa declarada del modelo y no un supuesto de costo cero.
- **Presupuesto de adquisición de usuarios.** Se incorpora una partida de marketing, modesta pero creciente, dado que la proyección de demanda no se sostiene por sí sola: un modelo que proyecta captación de usuarios sin asignar presupuesto de adquisición incurre en una inconsistencia interna.

### Costos variables por transacción y reparto del cobro

El reparto de cada pago lo determina el modelo de cobro que el sistema implementa (modelo A, ADR-M5-02). Cada tutor conecta su cuenta de
MercadoPago y la orden de pago se crea con esa cuenta como vendedora; la plataforma percibe su comisión mediante el campo ‘marketplace_fee‘.
En ese esquema, MercadoPago descuenta primero su propia comisión de procesamiento (6,04 % con IVA, para dinero disponible de forma inmediata) de los fondos del vendedor —el tutor— y la comisión de la plataforma se descuenta del saldo restante. La tabla~[§tab:unit-economics] presenta la economía unitaria de una sesión promedio con ese reparto.

**Tabla:** Economía unitaria y reparto de una sesión promedio (en USD)

| **Concepto** | **Cálculo** | **Valor** |
| --- | --- | --- |
| Ticket promedio de la sesión | Precio fijado por el tutor | 7,4200 |
| Comisión de MercadoPago (a cargo del tutor) | Ticket $$ 6,04 % | $-0{,}4482$ |
| Comisión de plataforma (‘marketplace_fee‘) | Ticket $$ 27 % | $-2{,}0034$ |
| **Neto que recibe el tutor** | Ticket $$ 66,96 % | **4,9684** |
| **Margen de la plataforma por sesión** | Ticket $$ 27 % | **2,0034** |

El tutor recibe, entonces, $1 - 0{,}27 - 0{,}0604 = 66{,}96 %$ del precio que fija: unos USD~4,97 por sesión promedio o, al precio horario promedio del relevamiento ($13.392,43), unos $8.968 por hora. La pantalla de precio del tutor le muestra ese neto aproximado, con la comisión de la plataforma y la estimada de MercadoPago por separado (regla FR-PAG-019); es aproximado porque la tasa real de MercadoPago depende del plazo de acreditación que tenga configurado cada cuenta. Ese neto es parte de la propuesta de valor para el tutor y, a la vez, el punto sensible del modelo: el descuento total sobre su precio es del 33,04 %, y cuanto menor es su neto mayor es el incentivo a acordar las clases por fuera de la plataforma (sección~[§sec:fundamento-comision]).

**Cambio respecto de la versión anterior del modelo..**  La versión anterior de este capítulo restaba la comisión de MercadoPago
(USD~0,4482 por sesión) como un costo de cobranza de la plataforma y obtenía un margen de USD~1,5552 por sesión. Ese tratamiento correspondía al diseño inicial, en el que todo el dinero ingresaba a la cuenta de la plataforma y se transfería después a cada tutor. El sistema descartó ese esquema porque obligaba a recaudar fondos de terceros, con su carga impositiva y transferencias manuales (ADR-M5-02), y también descartó que la plataforma absorbiera la comisión de MercadoPago dentro del modelo A, porque exigiría conocer la comisión real de cada pago, variable según la cuenta de cada tutor (ADR-M5-05). El registro de decisiones del sistema declara explícitamente la discrepancia y señala que el ajuste corresponde a esta evaluación y no al código (ADR-M5-05). Con el reparto real, el margen de la plataforma es la comisión completa, USD~2,0034 por sesión, un 29 % más que en la versión anterior; la comisión de MercadoPago sigue existiendo, pero recae sobre el tutor.

Se reconoce además la existencia de fricción financiera adicional sobre la comisión que factura la plataforma —retenciones de ingresos brutos, percepciones impositivas y contracargos— cuya magnitud depende de la jurisdicción y del comportamiento efectivo de los usuarios. Tampoco se modelan ciertos costos que el sistema pone a cargo de la plataforma: la diferencia de comisión en los reembolsos parciales que resuelve manualmente el área de soporte financiero ante una disputa (regla
FR-PAG-010) y los reembolsos que la plataforma debe afrontar con fondos propios cuando el tutor revocó el acceso a su cuenta de MercadoPago con una ventana de reembolso abierta (ADR-M5-02). Ninguno de estos conceptos se cuantifica en el modelo base: se tratan como una sensibilidad adicional sobre el margen (sección~[§sec:sensibilidad]), lo cual se declara como una restricción del análisis.

## Beneficios del proyecto

El análisis costo-beneficio contempla tanto los beneficios directamente monetizables como aquellos que, sin traducirse en flujo de caja, inciden sobre la viabilidad del proyecto. La tabla~[§tab:beneficios] los sistematiza.

**Tabla:** Beneficios tangibles e intangibles del proyecto

| **Tipo** | **Beneficio** | **Cuantificación** |
| --- | --- | --- |
| Tangible | Ingreso por comisión sobre sesiones concretadas | USD~2,0034 de margen por sesión; es la única fuente de ingreso del flujo |
| Tangible | Infraestructura de desarrollo sin erogación (servidor propio preexistente, ADR-000-07) | Evita alquilar un VPS durante el Año 0, de USD~7,71 a USD~158,7 mensuales [lightnode2026]; no se imputa al flujo |
| Tangible | Ahorro en desplazamiento para alumnos y tutores | No se imputa al flujo del proyecto; es un excedente que capta el usuario |
| Intangible | Formalización de los cobros de los tutores | Cada cobro ingresa a la cuenta de MercadoPago del tutor y se exporta para facturar ante la ARCA; la plataforma no recauda fondos de terceros |
| Intangible | Trazabilidad y seguridad en la interacción con menores | Barrera de entrada frente a competidores informales |
| Intangible | Acceso a apoyo escolar en zonas sin oferta presencial | Impacto social; amplía el mercado direccionable |

Únicamente el primer beneficio se incorpora al flujo de fondos. El ahorro de infraestructura, los ahorros que captura el usuario final y los beneficios intangibles se declaran pero no se monetizan, con el fin de no sobrestimar la rentabilidad del proyecto.

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

La tasa de descuento resume el costo de inmovilizar capital en este proyecto en lugar de destinarlo a su mejor alternativa de riesgo comparable. Incorpora tres componentes: el rendimiento de una colocación alternativa, la cobertura frente a la pérdida de poder adquisitivo y una prima por el riesgo de que los flujos proyectados no se materialicen.

Se adopta una **tasa de descuento del 15 % anual en dólares**.
Dado que la totalidad del modelo está expresada en dólares estadounidenses, la tasa debe interpretarse como una tasa real en esa moneda y no incorpora la inflación en pesos. El valor refleja el costo de oportunidad de un desarrollo tecnológico temprano, sin ingresos históricos ni base de usuarios consolidada, categoría que exige primas de riesgo sensiblemente superiores a las de un activo financiero tradicional.

El factor de descuento aplicado a cada año $t$ es $1/(1+0{,}15)^t$. La sensibilidad de los resultados frente a esta elección se examina en la sección~[§sec:sensibilidad].

## Flujo de fondos proyectado

El flujo de fondos cruza los ingresos derivados del volumen de sesiones contra los costos fijos anuales, imputando la inversión inicial íntegramente en el Año 0. Los ingresos netos de cada año se obtienen multiplicando las sesiones anuales por el margen unitario de la plataforma, USD~2,0034. La tabla~[§tab:flujo-caja] presenta el flujo del escenario base.

**Tabla:** Flujo de fondos proyectado — escenario base (en USD)

| **Concepto** | **Año 0** | **Año 1** | **Año 2** | **Año 3** | **Año 4** | **Año 5** |
| --- | --- | --- | --- | --- | --- | --- |
| Sesiones anuales | 0 | 7.200 | 9.360 | 7.560 | 10.440 | 9.000 |
| Ingreso neto | 0 | 14.424 | 18.752 | 15.146 | 20.915 | 18.031 |
| Costos fijos anuales | 0 | $-3.555$ | $-3.675$ | $-3.915$ | $-4.155$ | $-4.395$ |
| Inversión inicial | $-25.730$ | 0 | 0 | 0 | 0 | 0 |
| **Flujo neto** | **$-25.730$** | **10.869** | **15.077** | **11.231** | **16.760** | **13.636** |
| **Flujo acumulado** | **$-25.730$** | **$-14.861$** | **216** | **11.447** | **28.208** | **41.843** |
| **Flujo descontado** | **$-25.730$** | **9.452** | **11.400** | **7.384** | **9.583** | **6.779** |
| **Acum. descontado** | **$-25.730$** | **$-16.278$** | **$-4.878$** | **2.506** | **12.089** | **18.869** |

La comparación entre las dos últimas filas ilustra el efecto del descuento: mientras el flujo acumulado nominal cambia de signo al cierre del Año 2, el acumulado descontado recién lo hace durante el Año 3. Esa distancia es, precisamente, el precio del tiempo.

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
| Pesimista | $-4.410$ | 8{,}09 % | 4,22 años | No recupera en 5 años |
| Base | 18.869 | 41{,}57 % | 1,99 años | 2,66 años |
| Optimista | 51.990 | 78{,}24 % | 1,34 años | 1,56 años |

La lectura de cada indicador es la siguiente:

- **VAN del escenario base:** USD~18.869. Es positivo, por lo que el proyecto crea valor por encima de la tasa exigida del 15 % y se acepta: además de recuperar la inversión y rendir el 15 % anual, deja un excedente equivalente a aproximadamente el 73 % de la inversión de USD~25.730, expresado en dinero de hoy.
- **TIR del escenario base:** 41,57 %. Supera a la tasa de corte del 15 % por 26,57 puntos porcentuales. Ese diferencial es el margen de seguridad: la tasa exigida podría subir hasta casi el 41,6 % antes de que el proyecto dejara de convenir.
- **Período de repago:** 1,99 años en el escenario base. La inversión nominal se recupera al cierre del Año 2.
- **Repago descontado:** 2,66 años. Medido en dinero de hoy, el recupero se alcanza durante el Año 3, con más de dos años de holgura dentro del horizonte proyectado.

El escenario pesimista, en cambio, no se justifica: con un VAN de
USD~-4.410 y una TIR de 8,09 %, inferior a la tasa de corte, los flujos devuelven el capital nominal invertido (repago simple de 4,22
años) pero no alcanzan a remunerarlo al 15 % exigido, y el repago descontado no se produce dentro del horizonte. El escenario optimista presenta holgura en las cuatro métricas.

Estos resultados mejoran sustancialmente los de la versión anterior del modelo (VAN base de USD~3.573, TIR de 20,47 % y
VAN pesimista de USD~-14.499). La diferencia no proviene de supuestos de demanda más favorables —los escenarios son los mismos— sino de dos correcciones de alineación con el sistema implementado, cuyo efecto se separa en la tabla~[§tab:puente].

**Tabla:** Efecto de cada corrección sobre el escenario base

| **Versión del modelo** | **Margen por sesión** | **VAN base** | **TIR base** | **Comisión de equilibrio** |
| --- | --- | --- | --- | --- |
| Anterior: pasarela a cargo de la plataforma y partida fija de LLM | 1,5552 | 3.573 | 20,47 % | $$ 25,3 % |
| Reparto del modelo A (ADR-M5-02, ADR-M5-05) | 2,0034 | 16.459 | 38,43 % | $$ 19,3 % |
| **Vigente**: además, sin partida fija de LLM | **2,0034** | **18.869** | **41,57 %** | **$$ 18,2 %** |

El reparto del modelo A explica la mayor parte del cambio: confirma lo que el propio registro de decisiones del sistema anticipaba, que el modelo anterior era una cota inferior conservadora del margen real
(ADR-M5-05). Con solo esa corrección, el escenario pesimista mejora de
USD~-14.499 a USD~-6.820; con ambas, a USD~-4.410.

## Análisis de sensibilidad

Los resultados de la sección anterior dependen de un conjunto acotado de variables. El análisis de sensibilidad realizado sobre el modelo permite identificarlas y cuantificar su incidencia; en cada caso se modifica una variable y se mantiene constante el resto de los supuestos del escenario base.

- **Volumen de sesiones.** Es la variable de mayor impacto.
          El punto de equilibrio operativo se obtiene dividiendo los costos fijos anuales por el margen unitario: en el Año 1 se requieren $3.555 / 2{,}0034 1.774$ sesiones anuales para cubrir los costos fijos, y en el Año 5 aproximadamente 2.194.
          Por debajo de ese umbral la operación genera pérdidas antes de considerar la recuperación de la inversión. Para que el
          VAN del escenario base no sea negativo, el volumen puede caer hasta un 32,8 % en todos los años: el promedio anual de sesiones no puede bajar de unas 5.858, frente a las 8.712 del escenario base.
- **Comisión de plataforma.** El VAN del escenario base se anula con una comisión de aproximadamente 18,2 %. La tabla~[§tab:sens-comision] muestra el efecto de otros valores sobre el escenario base, sobre el pesimista y sobre el neto que recibe el tutor.
- **Ticket promedio.** Con la comisión en 27 %, el
          VAN del escenario base se anula con un ticket de aproximadamente USD~4,99 por sesión de duración media, es decir, unos USD~5,87 por hora ($9.010 al tipo de cambio de
          $1.535): un precio horario que queda entre el primer cuartil
          ($8.000) y la mediana ($12.000) del relevamiento de Superprof.
          Como el ticket depende del tipo de cambio, el resultado es sensible a él: el VAN base se anula por encima de unos
          $2.281 por USD (apéndice~[§apx:precio]).
- **Paquete mensual con descuento.** El descuento de 0 a
          30 % que el tutor puede aplicar al paquete (ADR-M5-03) reduce el ticket de las clases vendidas en paquete. Si la mitad de las sesiones se vendiera en paquetes con el descuento máximo, el ticket efectivo bajaría a USD~6,31 y el VAN base a
          USD~10.228; aun si todas las sesiones se vendieran así, el ticket sería de USD~5,19 y el VAN base seguiría siendo positivo (USD~1.587). El descuento medio que anula el VAN
          base es de 32,8 %, por encima del máximo que el sistema admite.
          No se dispone de datos de adopción del paquete, por lo que estas cifras son cotas y no una proyección.
- **Duración media de las sesiones.** Como el precio de la sesión es proporcional a su duración, el ticket se mueve con el supuesto de 51 minutos (ecuación~[§eq:duracion]): con una duración media de 45 minutos el ticket sería de USD~6,54 y el
          VAN base de USD~12.037; con 60 minutos, de USD~8,72 y
          USD~28.961. El VAN base se anula con una duración media de unos 34 minutos, cercana al bloque mínimo de 30.
- **Estructura de costos fijos.** La incorporación de un equipo de soporte rentado —evaluada en una formulación previa del modelo con perfiles junior, mid y senior incorporados de forma escalonada— tornaba negativo el VAN en los tres escenarios. Con el modelo vigente, el escenario base podría absorber como máximo unos USD~469 mensuales constantes de costo adicional durante los cinco años antes de que el VAN
          se anule. Ese mismo margen es el que debe cubrir los costos que la plataforma absorbe y el modelo no cuantifica
          (sección~[§sec:costos-variables]): una dedicación parcial de soporte y esos costos compiten por el mismo excedente.
- **Partida fija de LLM.** Si se mantuviera la partida de USD~55 a USD~70 mensuales que se eliminó
          (sección~[§sec:costos-recurrentes]), el VAN base sería de USD~16.459 y la comisión de equilibrio de aproximadamente
          19,3 % (tabla~[§tab:puente]).

**Tabla:** Sensibilidad a la comisión de plataforma

| **Comisión** | **VAN base (USD)** | **TIR base** | **VAN pesimista (USD)** | **Neto del tutor** |
| --- | --- | --- | --- | --- |
| 18,2 % (equilibrio del base) | 0 | 15,00 % | $-15.653$ | 75,8 % |
| 21 % | 6.068 | 24,14 % | $-12.038$ | 72,96 % |
| 23 % | 10.335 | 30,18 % | $-9.495$ | 70,96 % |
| 25 % | 14.602 | 35,97 % | $-6.952$ | 68,96 % |
| **27 % (vigente)** | **18.869** | **41,57 %** | **$-4.410$** | **66,96 %** |
| 30 % | 25.269 | 49,67 % | $-596$ | 63,96 % |
| 33 % | 31.669 | 57,50 % | 3.218 | 60,96 % |

Cabe señalar que la tasa de descuento afecta al VAN y al repago descontado, pero no a la TIR, que depende exclusivamente del perfil de los flujos.

### Por qué se mantiene la comisión del 27 %

Con el modelo corregido, el escenario base tolera una comisión de hasta aproximadamente 18,2 %. El 27 % no se mantiene, entonces, porque sea el mínimo que el proyecto necesita —eso dejó de ser cierto
(sección~[§sec:calibracion-comision])—, sino por los siguientes fundamentos:

- **Es la decisión vigente del dueño del producto.** El sistema la fija en la regla BR-PAG-01 (ADR-M5-05), con conocimiento de que el tutor recibe el 66,96 % del precio. La misma decisión reemplazó a una comisión del 21 % que había estado vigente durante el desarrollo (ADR-M5-04).
- **Colchón frente al escenario pesimista.** Aun con el
          27 %, el escenario pesimista tiene un VAN de
          USD~-4.410; para que se anule haría falta una comisión de aproximadamente 30,5 %. Bajar la comisión al equilibrio del escenario base dejaría el VAN pesimista en
          USD~-15.653 (tabla~[§tab:sens-comision]). La holgura del escenario base es la que permite absorber una demanda menor a la proyectada.
- **Costos que el modelo no cuantifica.** La plataforma absorbe la diferencia de comisión en los reembolsos parciales por disputa (FR-PAG-010), los reembolsos que debe afrontar con fondos propios cuando un tutor revoca el acceso a su cuenta
          (ADR-M5-02), la fricción impositiva sobre su comisión y el soporte que hoy presta el equipo fundador. Todos compiten por el mismo excedente, de unos USD~469 mensuales en el escenario base.
- **Dentro de la banda de referencia.** El 27 % se ubica dentro de la banda de comisiones de Preply (18 % a
          33 %) [preply] y por debajo de su extremo superior, que se descartó por el riesgo de desintermediación.

El costo de esta decisión recae sobre el tutor y se reconoce explícitamente. Al sumarse la comisión de MercadoPago, el descuento total sobre su precio es del 33,04 %: seis puntos más de lo que se había calibrado cuando la plataforma absorbía la pasarela. El propio registro de decisiones del sistema señala que, con ese neto, vuelven a pesar dos riesgos: la **desintermediación** —que tutor y alumno acuerden las clases siguientes por fuera de la plataforma— y la mayor dificultad para
**sumar tutores** (ADR-M5-05). Por eso la comisión no se considera definitiva: la métrica con la que se revisará después del piloto quedó diferida deliberadamente hasta ese momento (regla BR-PAG-03), y la tabla~[§tab:sens-comision] muestra el margen disponible para hacerlo
—una reducción a 23 o 25 % mantiene el escenario base con VAN
positivo— a costa de agravar el pesimista.

## Política de reembolsos y su costo real

La regla general del sistema es que todo reembolso a quien pagó es
**total**: se ejecuta a través de la API de MercadoPago sin indicar monto, y está prohibido el reembolso parcial automático que traslade la comisión al estudiante (regla FR-PAG-009). La regla previene riesgos legales de retención indebida frente a la Ley de Defensa del
Consumidor y reduce la exposición de la plataforma a contracargos. Tiene dos excepciones automáticas y una manual:

- el **adicional de resumen** que no llega a generarse se devuelve por su monto exacto, con un reembolso parcial (regla
          BR-PAG-11);
- la **clase de un paquete mensual** que no se dicta por falta del tutor se devuelve por el precio de esa clase; lo que
          MercadoPago no reintegre de su comisión en ese parcial queda a cargo del tutor (regla FR-PAG-022, ADR-M5-03);
- los **reembolsos parciales por disputa** los resuelve manualmente el área de soporte financiero, y la diferencia de comisión la absorbe la plataforma (regla FR-PAG-010).

El costo de un reembolso total para la plataforma se considera nulo: deja de percibir la comisión de una sesión que no se concretó, y el modelo solo computa ingresos de sesiones concretadas. Esa conclusión descansa en un
**supuesto** que se declara: que el reembolso total revierte tanto la comisión de MercadoPago como el ‘marketplace_fee‘ de la plataforma. El sistema dejó esa verificación pendiente en el entorno de pruebas de MercadoPago (ADR-M5-02); si no se cumpliera, el reembolso tendría un costo que el modelo no incluye.

## Conclusión de la evaluación económica

El proyecto se justifica económicamente, bajo condiciones que corresponde explicitar.

En el escenario base, los cuatro indicadores apuntan en la misma dirección: el VAN es positivo (USD~18.869), la TIR supera holgadamente la tasa de corte (41,57 % frente a 15 %) y tanto el repago simple (1,99 años) como el descontado (2,66 años) se producen dentro de los primeros tres años del horizonte. Conforme al criterio de decisión estándar, el proyecto se acepta. El escenario optimista confirma esa conclusión con holgura.

Estos resultados reemplazan a los de la versión anterior del capítulo, que restaba la comisión de MercadoPago como costo de la plataforma. Con el modelo de cobro que el sistema implementa, esa comisión la paga el tutor, que recibe el 66,96 % de su precio, y la plataforma percibe el
27 % completo. El escenario pesimista sigue sin justificarse
(VAN de USD~-4.410): recupera el capital nominal invertido, pero no lo remunera a la tasa exigida. De ello se desprenden tres condiciones de viabilidad:

- **Sostener un volumen mínimo de entre 1.774 (Año 1) y
          2.194 (Año 5) sesiones anuales**, umbral por debajo del cual la operación no cubre siquiera sus costos fijos, y de unas 5.858
          sesiones anuales en promedio para que el VAN no sea negativo.
- **No bajar la comisión por debajo de aproximadamente
          18,2 %**, valor con el que el VAN del escenario base se anula. El 27 % vigente deja un margen de unos nueve puntos porcentuales, que se mantiene deliberadamente como colchón frente al escenario pesimista y a los costos que el modelo no cuantifica, y que se revisará después del piloto considerando su efecto sobre el neto del tutor y el riesgo de desintermediación.
- **Operar sin equipo de soporte rentado**, o con una dedicación parcial que, sumada a los costos no modelados, no supere unos USD~469 mensuales, durante el horizonte evaluado, difiriendo la incorporación de un equipo hasta que el volumen efectivo la justifique.

Que el escenario pesimista no resulte viable no invalida el proyecto, sino que delimita con precisión el terreno en que debe moverse. Ante una tracción inferior a la proyectada, las alternativas disponibles no pasan por reducir costos —el margen de recorte es escaso— sino por revisar el modelo de negocio: segmentar la oferta por niveles de precio, incorporar modalidades de clase grupal que eleven el ingreso por hora de tutor, o explorar acuerdos institucionales que aporten volumen agregado. El análisis de riesgos del capítulo siguiente retoma estas contingencias.

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

Los identificadores de los riesgos son estables: el registro de decisiones del sistema (anexo~[§anx:repositorios]) cita varios de ellos por su número —por ejemplo, ADR-M5-05 remite a R-02 y R-07, y
ADR-M1-04 a R-10—, por lo que la numeración no sigue el orden de exposición.

## Identificación y evaluación

La tabla~[§tab:matriz-riesgos] presenta los diecisiete riesgos identificados, ordenados por exposición descendente. Las fuentes de identificación fueron la encuesta de validación
(apéndice~[§apx:encuesta]), el modelo financiero
(capítulo~[§cap:economica] y anexo~[§anx:modelo-financiero]), los registros de decisión y la documentación de operación del sistema
(anexo~[§anx:repositorios]), la auditoría técnica y las pruebas en producción del capítulo~[§cap:resultados], y las condiciones de los proveedores relevadas en el capítulo~[§cap:marco-tecnologico]. Su estado corresponde al 15 de octubre de 2026.

**Tabla:** Ubicación de los riesgos en la matriz de exposición (probabilidad $$ impacto)

    {4pt}

|  | **1 Insignif.** | **2 Menor** | **3 Moderado** | **4 Importante** | **5 Severo** |
| --- | --- | --- | --- | --- | --- |
| **5 Muy probable** | | | | | |
| **4 Probable** | | | R-08 | R-02, R-03 | |
| **3 Posible** | | R-06, R-13 | R-11, R-14, R-15 | R-05, R-07 | R-04, R-17 |
| **2 Poco probable** | | | | R-12, R-16 | R-01, R-09, R-10 |
| **1 Muy improbable** | | | | | |

| **ID** | **Descripción (causa, evento, efecto)** | **Naturaleza (origen)** | **Etapa** | **P** | **I** | **E** | **Respuesta** | **Resp.** | **Contingencia** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-02 | Debido a que solo el 35,2 % de los encuestados prefiere pagar dentro de una plataforma antes que por transferencia, y a que el tutor recibe el 66,96 % de su precio una vez descontadas la comisión de la plataforma y la de MercadoPago (ADR-M5-05), podría ocurrir que alumnos y tutores acuerden las clases siguientes por fuera después del primer contacto, lo que provocaría la pérdida de la comisión, única fuente de ingreso. | Terceros: usuarios (externo) | Operación | 4 | 4 | 16 | Mitigar: la verificación, la reputación, el cobro con ventana de reembolso y el resumen solo existen dentro de la plataforma | Autor | Revisar la comisión después del piloto con la métrica diferida en BR-PAG-03; una comisión de 23 a 25 % mantiene positivo el VAN base (tabla~[§tab:sens-comision]) |
| R-03 | Debido a que el piloto se extiende del 27 de octubre al 27 de noviembre de 2026, el capítulo~[§cap:conclusiones] vence el 27 de octubre y un único desarrollador debe cerrar además las tareas previas al encendido de las clases con menores y las acciones operativas previas al piloto, podría ocurrir que la hipótesis deba responderse sin datos del piloto, lo que provocaría conclusiones sin evidencia suficiente. | Alcance (interno) | Durante | 4 | 4 | 16 | Mitigar: alcance del MVP congelado; lo no esencial se difiere de forma explícita (video de presentación del tutor, firma digital del CAP, especialidades verificadas) | Autor | Presentar la respuesta a la hipótesis como preliminar y completarla con el piloto para la entrega final |
| R-04 | Debido a que el escenario pesimista tiene un VAN de USD~-4.410, podría ocurrir que la demanda no alcance unas 5.858 sesiones anuales en promedio, lo que provocaría que la inversión no se recupere a la tasa exigida; por debajo de 1.774 a 2.194 sesiones anuales la operación ni siquiera cubre sus costos fijos (capítulo~[§cap:economica]). | Recursos: mercado (externo) | Operación | 3 | 5 | 15 | Mitigar: presupuesto de adquisición de usuarios y acuerdos institucionales (O-02) | Autor | Si a los 12 meses el volumen anualizado queda por debajo del umbral: revisar el modelo de negocio (segmentación de precios, clases grupales, acuerdos institucionales); si persiste, cierre ordenado |
| R-17 | Debido a que, después de las pruebas en producción del 14 de octubre de 2026, el plan de remediación registra que el despliegue quedó con configuraciones propias de un entorno de pruebas (datos y cuentas de prueba, pagos simulados y la opción de clases con menores encendida; acciones O-1 a O-6), podría ocurrir que el piloto se abra a usuarios reales en ese estado, lo que provocaría reservas confirmadas sin cobro o la reserva de un menor real sin todas sus protecciones. | Cumplimiento y datos (interno) | Pasaje a producción | 3 | 5 | 15 | Evitar: las acciones O-1 a O-6 del plan de remediación son criterio de entrada al piloto | Autor | Desactivar el modo simulado desde el panel de administración (efecto inmediato, ADR-M5-01), volver a apagar la opción de menores y dar de baja o renovar las cuentas de prueba |
| R-05 | Debido a que el ticket del modelo (USD~7,42 por sesión de 51 minutos) surge del precio promedio publicado en Superprof ($13.392 por hora), mientras que la mediana de la disposición a pagar relevada en la encuesta es de USD~4,56 por hora, podría ocurrir que el precio efectivo de las clases quede por debajo del ticket de equilibrio (USD~5,87 por hora), lo que provocaría un VAN base negativo. | Recursos: mercado (externo) | Operación | 3 | 4 | 12 | Mitigar: piso de tarifa de USD~4 por hora (BR-PAG-04), que protege los costos fijos pero no la inversión; medir el precio efectivo en el piloto | Autor | Si el ticket observado queda por debajo del de equilibrio: revisar comisión y piso con los datos del piloto (sección~[§sec:sensibilidad]) |
| R-07 | Debido a que solo 9 tutores respondieron la encuesta, a que el marketplace es bilateral y a que el tutor recibe seis puntos menos de neto que con la comisión anterior (ADR-M5-05) y debe conectar su cuenta de MercadoPago para aparecer en las búsquedas (ADR-M5-02), podría ocurrir que no haya suficientes tutores verificados al iniciar el piloto, lo que provocaría búsquedas sin candidatos e impediría medir la aceptación del matching (I-01). | Recursos: oferta (externo) | Antes de arrancar | 3 | 4 | 12 | Mitigar: reclutar tutores antes del piloto en la comunidad universitaria; recomendación por área cuando no hay coincidencia directa (FR-MATCH-011) | Autor | Acotar el piloto a una o dos materias con oferta suficiente |
| R-08 | Debido a que el 90,9 % de las respuestas de la encuesta proviene de la provincia de Buenos Aires y de la Ciudad Autónoma de Buenos Aires, podría ocurrir que la demanda y el precio del interior difieran de los relevados, lo que provocaría que la hipótesis de reducción de la brecha geográfica quede sin evidencia. | Datos (interno) | Antes de arrancar | 4 | 3 | 12 | Mitigar: reencuesta dirigida al interior y entrevistas a docentes de zonas rurales | Autor | Declarar la limitación y acotar el alcance de la conclusión |
| R-01 | Debido a que el kill-switch en el cliente todavía no tiene su prueba de punta a punta formal contra el servicio de video real ni la medición de latencia en dispositivos reales (T-M3-06f y T-M3-06g), y a que la exactitud del clasificador con contenido real no se probó, podría ocurrir que, al habilitar las clases con menores, una detección falle o llegue tarde, lo que provocaría la exposición de un menor a contenido inapropiado. | Técnico (interno) | Pasaje a producción | 2 | 5 | 10 | Evitar: piloto sin menores (opción de configuración de clases con menores apagada); el encendido exige cerrar T-M3-06f a T-M3-06i; sin clasificador listo el menor no entra al aula | Autor | Volver a apagar la opción de menores; ante una detección, corte, suspensión preventiva y revisión de la Alerta en 12 horas |
| R-09 | Debido a que el desarrollo y la operación dependen de una sola persona, podría ocurrir una enfermedad, una sobrecarga o un abandono, lo que provocaría la detención del desarrollo o de la operación. | Recursos (interno) | Operación | 2 | 5 | 10 | Aceptar: el modelo económico no admite un equipo rentado (capítulo~[§cap:economica]); documentación y pruebas reducen la dependencia | Autor | Prórroga ante la cátedra; en operación, pausa sin pérdida de datos y traspaso a partir del repositorio documentado |
| R-10 | Debido a que la verificación de antecedentes depende de la revisión manual del CAP, un documento que presenta el propio tutor y cuya firma digital no se verifica en el MVP, podría ocurrir que un certificado adulterado o evaluado con un criterio incorrecto habilite a un tutor con antecedentes para dar clases a menores, lo que provocaría un daño grave al menor y responsabilidad legal para la plataforma. | Cumplimiento (interno) | Operación | 2 | 5 | 10 | Mitigar: CAP vigente (12 meses) obligatorio solo para dar clases a menores, revisado por el rol de Moderación y Seguridad, con criterio de rechazo definido con la asesoría legal presupuestada (ADR-M1-04) | Autor y asesoría legal | Suspensión inmediata, conservación del certificado y del registro de auditoría, y denuncia ante la autoridad |
| R-11 | Debido a que el modelo de cobro con conexión de la cuenta de MercadoPago de cada tutor se implementó según la documentación del proveedor y quedó pendiente de verificar en su entorno de pruebas (ADR-M5-02), podría ocurrir que en producción el reembolso total no devuelva el ‘marketplace_fee‘, que no pueda reembolsarse a un tutor que revocó el acceso o que el contrato de OAuth difiera del documentado, lo que provocaría reembolsos a cargo de la plataforma o reservas que no pueden cobrarse. | Técnico: terceros (externo) | Pasaje a producción | 3 | 3 | 9 | Mitigar: verificación en el entorno de pruebas con dos usuarios antes del cobro real; notificaciones idempotentes y conciliación periódica contra la API (FR-PAG-017) | Autor | Modo de pago simulado (ADR-M5-01) y cola manual del rol de Soporte Financiero |
| R-14 | Debido a que todo el sistema corre en un único servidor propio, ubicado en un domicilio y sin IP fija (ADR-000-07), podría ocurrir un corte de luz, de internet o una falla del equipo, lo que provocaría que la plataforma quede fuera de línea mientras dure, incumpliendo la disponibilidad del 95 % mensual. | Técnico (interno) | Operación | 3 | 3 | 9 | Aceptar: alternativa compatible con el presupuesto de USD 0 a 100 mensuales y un único desarrollador; mitigación con copia diaria cifrada fuera del servidor (implementada, se activa al cargar las credenciales de R2 antes del piloto) y restauración documentada | Autor | Restaurar el último respaldo y desplegar las imágenes publicadas en otro servidor con la misma configuración |
| R-15 | Debido a que las pruebas exploratorias en producción encontraron tres hallazgos de severidad alta que la suite automatizada no detectaba, y a que su remediación, integrada a la rama principal el 15 de octubre de 2026, todavía no se repitió por rol en producción, podría ocurrir que el piloto arranque con defectos de seguridad o de uso no detectados, lo que provocaría pérdida de confianza de los primeros usuarios. | Técnico (interno) | Pasaje a producción | 3 | 3 | 9 | Mitigar: cada hallazgo con una prueba que falla antes del arreglo; repetir las pruebas por rol en producción antes del piloto | Autor | Corregir con prueba de regresión y desplegar la imagen corregida; volver a la imagen anterior si el arreglo falla |
| R-12 | Debido a la jurisprudencia laboral sobre repartidores de plataformas de delivery, podría ocurrir que un tutor reclame una relación de dependencia con la plataforma, lo que provocaría costos laborales no previstos. | Cumplimiento (externo) | Operación | 2 | 4 | 8 | Transferir: términos y condiciones redactados por asesoría legal; el tutor fija precio y horarios y cobra en su propia cuenta | Asesoría legal | Defensa legal con los registros de autonomía del tutor |
| R-16 | Debido a que el adicional de resumen graba el audio de la clase en el navegador del tutor y lo envía a un proveedor extranjero para transcribirlo (ADR-M3-04), podría ocurrir que la voz y los datos personales de los participantes se transfieran sin un consentimiento con validez legal suficiente, lo que provocaría un incumplimiento de la Ley 25.326. | Cumplimiento (interno) | Operación | 2 | 4 | 8 | Evitar: el adicional está apagado en producción hasta contar con el texto legal de la cláusula; nunca con menores; solo texto anonimizado llega al LLM; el audio se borra al transcribir (máximo 24 horas) | Autor y asesoría legal | Desactivar el adicional, solicitar la eliminación al proveedor y notificar a los titulares |
| R-06 | Debido a que los proveedores de LLM discontinúan modelos y modifican precios, podría ocurrir que el modelo de transcripción o el de resumen deje de estar disponible o se encarezca, lo que provocaría la interrupción del resumen o la pérdida de su margen. | Terceros (externo) | Operación | 3 | 2 | 6 | Mitigar: el backend accede al proveedor por un puerto intercambiable (‘ResumenProveedor‘) que, sin configuración, no envía nada; el precio del adicional se calcula sobre el costo (ADR-M5-06) | Autor | Cambiar de proveedor y ajustar el precio del adicional; si no es viable, suspenderlo sin afectar el núcleo |
| R-13 | Debido a que varios servicios se usan en planes gratuitos o se cotizan en dólares (LiveKit, Cloudflare, Resend, GitHub), podría ocurrir que un proveedor cambie las condiciones de su plan o sus tarifas, lo que provocaría un aumento de los costos fijos y una reducción del VAN. | Terceros (externo) | Operación | 3 | 2 | 6 | Mitigar: despliegue en contenedores portables y presupuesto de video ya incluido en los costos fijos; el escenario base absorbe hasta unos USD~469 mensuales adicionales | Autor | Cambiar de proveedor o de plan con la misma configuración de contenedores |

## Tratamiento de los riesgos principales

Los diez primeros riesgos concentran la exposición del proyecto. Su tratamiento se detalla a continuación; el resto se monitorea.

- **R-02, desintermediación (16).** Es el riesgo con mejor respaldo empírico: el 34,1 % de los encuestados se mostró en desacuerdo con pagar dentro de una plataforma
          (apéndice~[§apx:encuesta]). La decisión de mantener la comisión del 27 % lo agrava, y el propio registro de decisiones del sistema lo reconoce (ADR-M5-05): con la comisión de MercadoPago a cargo del tutor, el descuento total sobre su precio es del 33,04 %. La respuesta apunta a que el valor diferencial solo exista dentro de Tinku: las funciones más valoradas en la encuesta —profesores verificados (58 %), resumen automático (56,8 %) y pago seguro (48,9 %)— dependen de que la transacción ocurra en la plataforma. La contingencia no es improvisada: el capítulo~[§cap:economica] muestra cuánto puede bajar la comisión sin volver negativo el escenario base.
- **R-03, alcance y cronograma (16).** Corresponde al
          “alcance que nunca cierra” señalado por la cátedra. Al 14 de octubre de 2026, la lista de tareas del sistema registraba 221
          tareas completadas y 9 pendientes. De las pendientes, seis corresponden al kill-switch en el cliente y a su encendido, y tres se difirieron de forma explícita: la verificación automática de la firma digital del CAP (opcional), el video de presentación del tutor (fuera del MVP) y las especialidades verificadas contra registros oficiales
          (ADR-M1-06). Cualquier funcionalidad nueva pasa al trabajo futuro.
- **R-04, inviabilidad económica (15).** Surge del escenario pesimista del capítulo~[§cap:economica]. La contingencia define un disparador medible y una decisión: si a los doce meses el volumen anualizado no alcanza el umbral, se revisa el modelo de negocio y, si no hay alternativa viable, se cierra la operación de forma ordenada. Cancelar a tiempo un proyecto inviable es una decisión de gestión, no un fracaso.
- **R-17, estado operativo de producción (15).** Es un riesgo que no existía en el diseño y surgió de una actividad de verificación: para probar el aula en vivo y los pagos sin dinero real, el despliegue de producción se usó como entorno de pruebas, con datos sembrados y con la opción de menores encendida. El plan de remediación lo registró y definió las acciones para revertirlo, todas operativas y a cargo del autor. Se responde evitándolo: ninguna de esas condiciones puede seguir vigente al abrir el piloto. La lección es que un entorno de pruebas separado
          (T-M3-06h), descartado al principio por costo de memoria
          (ADR-000-07), deja de ser opcional cuando hay usuarios reales.
- **R-05, precio efectivo (12).** El capítulo~[§cap:economica] fija el ticket con precios de oferta publicados, no con la disposición a pagar declarada en la encuesta, que es aproximadamente la mitad. Ninguno de los dos es un precio observado en la plataforma; el piloto es la primera fuente de precios reales y el indicador que dispara la revisión.
- **R-07, oferta de tutores (12).** Es la manifestación del problema de arranque en frío (arranque en frío) descrito en el capítulo~[§cap:marco-teorico], agravada por las condiciones que el sistema exige al tutor para aparecer en las búsquedas: identidad verificada, foto, cuenta de MercadoPago conectada y, para dar clases a menores, el CAP vigente. Cada una se justifica por sí misma (confianza, cobro directo al tutor, seguridad del menor), pero en conjunto elevan la fricción del lado más escaso del marketplace.
- **R-08, sesgo geográfico de la encuesta (12).** Afecta directamente a la hipótesis central, que pone el foco en las zonas con escasa oferta de tutores.
- **R-01, kill-switch y clases con menores (10).** El backend del kill-switch y el clasificador en el navegador están implementados y se probaron en vivo, con salas de video reales, en las dos ramas y ante la falla del clasificador
          (capítulo~[§cap:resultados]). Faltan la prueba formal de punta a punta, la medición en celulares reales y la decisión de encendido. La respuesta es evitar: sin esas condiciones no se habilitan clases con menores, y el sistema lo impone con una opción de configuración que rechaza toda reserva o solicitud para un menor.
- **R-09, dependencia de una persona (10).** Se acepta porque no existe una respuesta alternativa compatible con el proyecto: el análisis económico mostró que un equipo rentado torna negativo el VAN en los tres escenarios. Aceptarlo no equivale a ignorarlo: la Constitución del proyecto, las nueve especificaciones, los 37 registros de decisión, el manual de operación y una suite de 661 pruebas automatizadas
          (capítulo~[§cap:resultados]) permiten que otra persona retome el sistema.
- **R-10, antecedentes de los tutores de menores (10).**
          Una primera versión del sistema exigía el CAP a todos los tutores y se retiró (ADR-M1-02) por dos motivos: la fricción en el registro de tutores, el recurso más escaso de la plataforma
          (R-07), y la necesidad de decidir la descalificación de un tutor por sus antecedentes sin asesoría legal. La verificación se reincorporó acotada (ADR-M1-04, implementada el 25 de septiembre de 2026): el CAP vigente es obligatorio solo para dar clases a menores, y al vencer se cancelan las clases futuras con menores con reembolso total. Así, los tutores que enseñan a adultos se registran sin fricción adicional. El riesgo residual es la validez del documento y su evaluación manual, porque la verificación automática de la firma digital quedó diferida.

Dos riesgos de exposición media merecen una mención por su respuesta. El
**R-14** (punto único de falla) es el riesgo aceptado de forma explícita en el diseño de la infraestructura: se eligió concentrar todo en un servidor propio porque el plan gratuito de Vercel no admite uso comercial y un solo proveedor simplifica la operación para un único desarrollador (ADR-000-07). Aceptarlo exige que la mitigación exista de verdad: el manual de operación advierte que, mientras no estén cargadas las credenciales del almacenamiento externo, no hay copia de seguridad fuera del servidor, y prevé ensayar la restauración antes del piloto. El
**R-16** (privacidad del audio) reemplaza a un riesgo que figuraba en una versión anterior de este capítulo —el envío del audio de las clases directamente al LLM—, eliminado por diseño: el audio va solo al servicio de transcripción, el texto se anonimiza antes de llegar al modelo de resumen (ADR-M6-03) y las clases con un menor nunca se graban.

## Riesgos que cancelan proyectos

La tabla~[§tab:riesgos-fatales] vincula los siete riesgos que la cátedra señala como causas de cancelación con los riesgos identificados.

**Tabla:** Riesgos fatales y su tratamiento en Tinku{

    }

| **Riesgo fatal** | **Situación en Tinku** |
| --- | --- |
| Alcance que no cierra | R-03: alcance congelado, con las funcionalidades no esenciales diferidas de forma explícita |
| Pérdida del proveedor de datos | R-06, R-11 y R-13: los servicios de terceros se aíslan detrás de interfaces intercambiables, el resumen no envía nada sin configuración y existe un modo de operación sin cobro real |
| Equipo que se desarma | R-09: aceptado, con documentación y pruebas que permiten el traspaso |
| Tecnología inadecuada | R-01: el clasificador en el navegador funciona y se probó en vivo; faltan la medición en dispositivos reales y el encendido |
| Inviabilidad económica | R-04 y R-05: viable en los escenarios base y optimista, con disparadores de revisión |
| Barrera ética o legal | R-16 y R-17 se evitan; R-10 se mitiga con el CAP obligatorio para dar clases a menores; R-12 se transfiere |
| Falta de un responsable | El autor es responsable de todos los riesgos internos; los de cumplimiento se comparten con la asesoría legal |

## Oportunidades

El análisis también identificó dos riesgos positivos, que se gestionan buscando que ocurran:

- **O-01.** Debido a que el 56,8 % de los encuestados valoró el resumen automático, podría ocurrir que una parte relevante de las clases entre adultos lo contrate, lo que provocaría un motivo adicional para pagar dentro de la plataforma y reduciría la exposición a R-02. Su aporte económico directo es pequeño, porque se cobra a costo más un 50 %
          (sección~[§sec:adicional-resumen]). Respuesta: explotar, habilitando el adicional en cuanto se resuelva R-16 y destacándolo en el flujo de reserva.
- **O-02.** Debido a que algunas jurisdicciones ya recurren a escuelas mediadas por tecnología con docentes en las ciudades
          [olea], podría ocurrir que una institución educativa o un municipio contrate paquetes de sesiones, lo que provocaría un volumen agregado superior al del escenario optimista. Respuesta: mejorar la probabilidad, presentando el piloto a instituciones del interior.

## Supuestos y restricciones

Los supuestos son condiciones que se dan por ciertas para que el proyecto sea válido; si alguno falla, se convierte en un riesgo. Las restricciones son condiciones impuestas que limitan el tiempo, el costo o el alcance.

**Tabla:** Supuestos del proyecto y riesgo asociado si fallan

| **ID** | **Supuesto** | **Si falla** |
| --- | --- | --- |
| S-01 | Los alumnos activos por año se ubican en la banda del escenario base (200 a 290) | R-04 |
| S-02 | Cada alumno activo toma tres clases por mes | R-04 |
| S-03 | El precio horario promedio publicado en Superprof ($13.392) y una duración media de 51 minutos representan el ticket de la plataforma (USD~7,42) | R-05 |
| S-04 | El tipo de cambio se mantiene por debajo de unos $2.281 por dólar, valor con el que se anula el VAN base (apéndice~[§apx:precio]) | R-05 |
| S-05 | Las condiciones de los planes gratuitos y las tarifas de los proveedores se mantienen durante el horizonte | R-13 |
| S-06 | La mayoría de los pagos se realiza dentro de la plataforma | R-02 |
| S-07 | El reembolso total revierte también el ‘marketplace_fee‘ de la plataforma (sección~[§sec:reembolsos]) | R-11 |
| S-08 | El servidor propio sostiene la disponibilidad del 95 % mensual que exige la Constitución del proyecto | R-14 |

**Tabla:** Restricciones del proyecto

| **Tipo** | **Restricción** |
| --- | --- |
| Tiempo | Presentación final el 28 de noviembre de 2026, con entregas parciales por capítulo |
| Recursos | Un único desarrollador, con una dedicación de 15 a 20 horas semanales |
| Costo | Entre 0 y 100 USD mensuales durante el desarrollo y el piloto |
| Infraestructura | Un único servidor propio, sin entorno de pruebas separado mientras no haya usuarios reales (ADR-000-07) |
| Técnica | Los organismos estatales (RENAPER, Registro Nacional de Reincidencia, registros de títulos) no ofrecen API públicas |
| Legal | Ley 25.326 de protección de datos personales; tutores exclusivamente mayores de edad; piloto sin clases con menores |
| Alcance | PWA sin aplicaciones móviles nativas |

## Seguimiento y continuidad

Los riesgos se revisan en cada Sprint Review (capítulo~[§cap:metodologia]): se actualizan la probabilidad y el impacto, se incorporan los riesgos nuevos y se registran los que se materializaron como problemas. Durante la operación, los disparadores de las contingencias —el volumen anualizado de sesiones para R-04, el ticket efectivo para R-05 y la tasa de recompra dentro de la plataforma para R-02— se miden mensualmente.

En cuanto a la pregunta de quién mantiene el sistema una vez finalizado el proyecto académico: el modelo económico prevé que el equipo fundador asuma el mantenimiento correctivo y evolutivo durante los cinco años evaluados, sin personal rentado (capítulo~[§cap:economica]). Si el proyecto no continuara, el cierre se haría de forma ordenada: aviso a los usuarios, reembolso de las reservas pendientes a través de
MercadoPago, y exportación o eliminación de los datos personales conforme a la Ley 25.326.

# Capítulo 7: Presentación de resultados

Este capítulo presenta los resultados del proyecto al 15 de octubre de
2026: los requerimientos del sistema, su construcción, las pruebas técnicas —automatizadas, de auditoría y en producción—, la validación con usuarios y la evaluación económica. Se informan tanto los resultados favorables como los desfavorables. Las pruebas de aceptación con usuarios reales corresponden al piloto del Sprint~11 (capítulo~[§cap:metodologia]); sus resultados se incorporarán al finalizarlo, y las secciones afectadas lo indican.

## Requerimientos

### Requerimientos funcionales

Los requerimientos funcionales se especificaron por módulo, antes de implementarse, en las especificaciones del repositorio del sistema
(anexo~[§anx:repositorios]). Cada uno tiene un identificador, una descripción y criterios de aceptación expresados como escenarios verificables (“dado , cuando , entonces ”); las especificaciones se enmiendan con fecha cuando una decisión posterior las modifica. La tabla~[§tab:rf] resume los requerimientos registrados por módulo en la rama principal al 14 de octubre de 2026 y su estado de implementación.

**Tabla:** Requerimientos funcionales por módulo y estado de implementación

| **Módulo** | **Prefijo** | **RF** | **Estado** |
| --- | --- | --- | --- |
| M1 Identidad y perfiles | FR-ID | 30 | Implementado, incluido el CAP para tutores de menores (ADR-M1-04). Diferidos: video de presentación del tutor (FR-ID-034 a 036, fuera del MVP) y especialidades verificadas contra registros oficiales (ADR-M1-06) |
| M2 Motor de matching | FR-MATCH | 14 | Implementado |
| M3 Aula virtual | FR-AULA | 13 | Implementado, con el kill-switch en el cliente; faltan su prueba formal de punta a punta, la medición en dispositivos reales y el encendido de las clases con menores (T-M3-06) |
| M4 Reservas y agenda | FR-RES | 33 | Implementado; un requerimiento retirado (FR-RES-028, ADR-M4-01) |
| M5 Motor de pagos | FR-PAG | 23 | Implementado, con conexión de la cuenta de MercadoPago de cada tutor (ADR-M5-02), pendiente de verificar en el entorno de pruebas del proveedor, y modo de operación sin cobro real (ADR-M5-01) |
| M6 Resumen automático | FR-SUM | 8 | Implementado (transcripción y GPT-4o sobre texto anonimizado); apagado en producción hasta contar con el texto legal de la cláusula de grabación |
| M7 Reputación | FR-REP | 12 | Implementado |
| M8 Administración | FR-ADM | 11 | Implementado |
| M9 Denuncias y seguridad | FR-SEC | 16 | Implementado |
| **Total** | **160** |  |  |

La prioridad de cada requerimiento y su criterio de aceptación detallado se encuentran en la especificación del módulo correspondiente.
La verificación funcional con usuarios se traza a los indicadores del capítulo~[§cap:metodologia] (tabla~[§tab:indicadores]): el matching (M2) a la tasa de aceptación de sugerencias (I-01), el aula virtual (M3) a la calidad percibida (I-02) y a la cobertura geográfica (I-03), y la experiencia completa al NPS (I-04).

### Requerimientos no funcionales

La tabla~[§tab:rnf] presenta los requerimientos no funcionales, que la Constitución del proyecto define como no negociables.

**Tabla:** Requerimientos no funcionales

| **ID** | **Atributo** | **Umbral medible** | **Estado** |
| --- | --- | --- | --- |
| RNF-01 | Disponibilidad | 95 % mensual durante el piloto | A medir en el piloto; el servidor único es un riesgo aceptado (R-14, capítulo~[§cap:riesgos]) |
| RNF-02 | Seguridad | TLS 1.2 o superior; contraseñas con bcrypt o argon2; registro de auditoría de toda acción de administración | Implementado: TLS hasta Cloudflare y túnel cifrado, bcrypt, auditoría de las acciones de administración; los 36 hallazgos de la auditoría técnica, cerrados (sección~[§sec:auditoria]) |
| RNF-03 | Privacidad | Cumplimiento de la Ley 25.326, con especial cuidado en los datos de menores | Medidas implementadas (la imagen del DNI no sale del servidor, las clases no se graban salvo el adicional entre adultos, piloto sin menores); riesgos abiertos R-16 y R-17 |
| RNF-04 | Rendimiento | Latencia de videollamada menor a 200~ms; ajuste automático de calidad sin modo degradado visible | A medir en el piloto |
| RNF-05 | Mantenibilidad | Sostenible por uno o dos desarrolladores, sin conocimiento tácito no documentado | Cumplido: Constitución, especificaciones, registros de decisión y manual de operación versionados |

## Diseño

La arquitectura, el modelo de datos y las decisiones de diseño se documentan en el capítulo~[§cap:marco-tecnologico]. El resultado de esa etapa fue un monolito modular de nueve módulos de dominio, con un único servicio propio separado para el matching y con el video, los pagos, el correo y el resumen delegados en proveedores externos
(figura~[§fig:arquitectura]). Las decisiones que cambiaron el diseño original durante la implementación se registran en la sección~[§sec:decisiones-implementacion].

*Insertar capturas reales de las pantallas principales: búsqueda de tutores, reserva, aula virtual y panel de administración.*

## Construcción e integración

El sistema se construyó con el método dirigido por especificaciones descrito en el capítulo~[§cap:metodologia], con asistentes de programación con IA (declaración de uso de IA y apéndice~[§apx:prompts]). La tabla~[§tab:construccion] resume el resultado medido sobre la rama principal del repositorio del sistema.

**Tabla:** Métricas de construcción al 14 de octubre de 2026

| **Métrica** | **Valor** |
| --- | --- |
| Módulos de dominio con especificación propia | 9 |
| Requerimientos funcionales especificados | 160 |
| Migraciones de base de datos versionadas (V1 a V47) | 47 |
| Registros de decisión de arquitectura (ADR) | 37 |
| Tareas completadas / pendientes | 221 / 9 |
| Commits de la rama principal | 482 |
| Pruebas automatizadas del backend / cobertura de líneas | 661 / 85,6 % |

El listado~[§lst:puerto-resumen] muestra un fragmento representativo de la construcción: el puerto que aísla al proveedor de LLM. Si el proveedor no está configurado, la implementación activa rechaza toda solicitud (*fail-closed*), de modo que ningún dato sale hacia un modelo externo. El comentario del propio código registra por qué el modelo recibe solo texto: el audio no puede anonimizarse antes de salir, y por eso se descartó el envío directo del audio que preveía el diseño inicial (ADR-M6-03).

/**
 * Anonimizacion (FR-SUM-005): transcriptAnonimizado ES lo que se
 * envia [...] el audio crudo no es anonimizable antes de salir,
 * por eso ADR-M6-03 descarta el "audio directo" de la Constitucion
 * y el LLM solo recibe texto.
 */
public interface ResumenProveedor {
    ResumenResultado generarResumen(ResumenRequest request);
}

public class ResumenProveedorFailClosed implements ResumenProveedor {
    @Override public ResumenResultado generarResumen(ResumenRequest request) {
        throw new ResumenProveedorNoConfiguradoException();
    }
}

## Pruebas técnicas

### Pruebas automatizadas

El backend se prueba con JUnit~5 y Testcontainers contra una base
PostgreSQL real; el frontend, con pruebas de punta a punta en Playwright que simulan la API e incluyen controles de accesibilidad con axe-core; el motor de matching, con pytest. Las tres suites corren en la integración continua en cada cambio, y una prueba nocturna recorre el camino crítico —registro, búsqueda semántica, reserva y pago en modo de prueba hasta la confirmación— contra la base, el motor de matching y el backend reales (capítulo~[§cap:marco-tecnologico]).
Entre las pruebas de integración del backend hay dos de extremo a extremo sin simulaciones entre los módulos propios: el flujo principal completo y la rama de seguridad (sesión con un menor, disparo del kill-switch, suspensión, alerta y resolución del administrador).

La tabla~[§tab:evolucion-pruebas] muestra la evolución de la suite del backend en las mediciones registradas en el repositorio del sistema.

**Tabla:** Evolución de las pruebas automatizadas

| **Fecha** | **Medición** | **Pruebas del backend** | **Otros resultados** |
| --- | --- | --- | --- |
| 21/09/2026 | Auditoría técnica, sobre la rama principal | 383, sin fallas | — |
| 14/10/2026 | Línea de base de la rama principal | 661, sin fallas, 5 omitidas | Cobertura de líneas del 85,6 % (JaCoCo) |
| 15/10/2026 | Rama principal, con la remediación de las pruebas en producción y la ventana mínima de 21 minutos integradas | 739, sin fallas, 5 omitidas | Cobertura del 86,2 % (medida con 738 pruebas, antes del último cambio); Playwright: 222 exitosas y 3 omitidas; pytest: 26 de 26 |

Las cinco pruebas omitidas son las del OCR con Tesseract real, que se saltean en un equipo sin Tesseract instalado y corren en la integración continua. La metodología fijaba una cobertura mínima del
70 % por módulo; durante la implementación se optó por medir primero la cobertura de todo el backend, sin un umbral que corte la construcción, y decidir el umbral con el valor medido (ADR-000-05). El valor medido supera el umbral original, pero no se mide por módulo y nada impide hoy que baje.

### Auditoría técnica

El 21 de septiembre de 2026 se realizó una auditoría técnica del repositorio completo —backend, frontend, servicio de matching, migraciones, documentación, integración continua y configuración de despliegue—, que incluyó la ejecución de la suite de pruebas.
*Quién realizó la auditoría y con qué método o herramienta.*
La auditoría registró 36 hallazgos, que se gestionan en un registro con su estado: un hallazgo solo se da por cerrado con un cambio en el código y una prueba de regresión. La tabla~[§tab:auditoria] resume su estado.

**Tabla:** Hallazgos de la auditoría técnica por severidad y estado (registro del 28/09/2026)

| **Severidad** | **Hallazgos** | **Cerrados** | **Abiertos** |
| --- | --- | --- | --- |
| Crítica | 7 | 7 | 0 |
| Alta | 12 | 12 | 0 |
| Media | 13 | 13 | 0 |
| Baja | 4 | 4 | 0 |
| **Total** | **36** | **36** | **0** |

La auditoría concluyó que el proceso de desarrollo era disciplinado, pero que la implementación de los controles de seguridad era más débil de lo que la documentación sugería. Los siete hallazgos críticos afectaban directamente a la seguridad del menor y a la confianza:

- el kill-switch registraba el corte en la base de datos, pero no cerraba la sala de video, que seguía activa;
- los permisos de acceso a las salas de video otorgaban a los participantes privilegios de administración;
- el DNI del participante se usaba como identificador en la sala de video y se mostraba en pantalla, incluido el de los menores;
- la verificación de identidad por OCR funcionaba con una simulación activada por defecto;
- cualquier participante podía disparar el kill-switch sin aportar evidencia;
- la credencial académica se aprobaba sin que el administrador pudiera ver el documento;
- el enlace de restablecimiento de contraseña se registraba en claro en los registros del servidor.

Entre los de severidad alta estaban la ausencia de límites de intentos en los endpoints públicos, la falta de una infraestructura real de notificaciones, el servicio de matching expuesto sin autenticación y una restricción de reservas que comparaba horarios idénticos en lugar de superpuestos. Al 28 de septiembre de 2026 los 36 hallazgos figuraban cerrados, cada uno con el commit que lo resolvió y la prueba que lo cubre; de los siete subítems de calidad del hallazgo AUD-036, uno se aceptó sin cambio con su justificación.

### Pruebas en producción

El 14 de octubre de 2026 se ejecutaron pruebas exploratorias sobre el despliegue real (tinku.site), con datos sembrados y siete recorridos independientes, uno por rol (estudiante, tutor, menor y su adulto responsable, moderación, soporte financiero, seguridad y experiencia móvil), sobre la interfaz y la API. Los recorridos fueron asistidos por agentes de IA que operaron un navegador automatizado. El resultado no encontró bloqueantes: ninguna fuga de datos entre cuentas, ningún salto de rol ni de autenticación, y el corte de las clases con menores resistió por la API y por la interfaz. Sí encontró tres hallazgos de severidad alta que la suite automatizada no detectaba:

- un menor podía modificar sus propias capacidades por la
          API, aunque la restricción de fondo impidió que reservara;
- la cola de revisión del CAP fallaba en cuanto había un certificado pendiente;
- el tutor no podía dar de baja una franja horaria, algo que la especificación del módulo tampoco definía.

A ellos se sumaron un patrón transversal —los errores de validación respondían como si fueran de permisos—, problemas de relevancia de la búsqueda, de agenda y de accesibilidad en el móvil. El pago real, el flujo con menores en sesión y la verificación de identidad con un
DNI real no se probaron, por las reglas de la propia prueba.

Una segunda ronda, el mismo día, probó el aula en vivo y el kill-switch con salas de video reales, dos navegadores por escenario y el backend de producción. El kill-switch funcionó de punta a punta en sus dos ramas: con un menor presente, la clase se cortó 2,5 segundos después de que el modelo empezara a detectar, sin preguntarle nada al menor y con el clip de evidencia disponible para el administrador; entre adultos, el video se ocultó y, sin respuesta de la contraparte, la confirmación venció a los 300 segundos. Ante la falla del clasificador con un menor, el cliente ocultó el video, reintentó y cortó la clase al no poder reactivarlo. Se encontró un hallazgo de severidad media: tras un corte, el participante que no recibía el aviso del otro navegador quedaba en la pantalla de espera. La exactitud del clasificador con contenido real y su latencia en un celular no se probaron.

La remediación de los hallazgos de código se implementó el 15 de octubre de
2026, con una prueba que reproduce cada hallazgo y falla antes del arreglo, y se integró ese mismo día a la rama principal con la integración continua en verde; queda repetir las pruebas por rol en producción (riesgo R-15 del capítulo~[§cap:riesgos]). Como parte de ella se calibró el umbral de relevancia de la búsqueda con el modelo de embeddings semánticos real sobre 40 consultas (20 relevantes, 10 irrelevantes y 10 sin sentido): con el umbral anterior (0,30) pasaban 5 de 10 consultas irrelevantes; con el elegido (0,46) el 95 % de las relevantes conserva resultados y ninguna irrelevante ni sin sentido los obtiene. La consulta relevante que se pierde cae a la recomendación por área (FR-MATCH-011).
Las consultas son de elaboración propia, por lo que la medición calibra el umbral pero no reemplaza al indicador I-01 del piloto.

La lectura de estas dos actividades complementa la de la auditoría: cientos de pruebas exitosas no garantizan la ausencia de defectos graves, porque las pruebas verifican lo que se especificó y no lo que se omitió. La revisión independiente y la prueba sobre el despliegue real detectaron fallas que ninguna prueba cubría, y en un caso, un hueco de la propia especificación. El desarrollo asistido por IA acelera la construcción, pero no reemplaza la verificación.

### Pruebas de aceptación

Las pruebas de aceptación con usuarios (UAT) se realizan en el piloto del Sprint~11, entre el 27 de octubre y el 27 de noviembre de
2026, y miden los indicadores del capítulo~[§cap:metodologia]
(tabla~[§tab:indicadores-piloto]). Por el riesgo R-01 del capítulo~[§cap:riesgos], el piloto no incluye clases con menores.

**Tabla:** Indicadores del piloto

| **ID** | **Indicador** | **Umbral** | **Resultado** |
| --- | --- | --- | --- |
| I-01 | Aceptación de las sugerencias del matching | $> 60 %$ | *pendiente del piloto* |
| I-02 | Calidad percibida de la sesión (escala 1 a 5) | $4{,}0$ | *pendiente del piloto* |
| I-03 | Sesiones entre provincias distintas, con una del interior | $1$ | *pendiente del piloto* |
| I-04 | NPS del piloto | positivo | *pendiente del piloto* |

## Validación con usuarios

### Encuesta de validación

La encuesta, aplicada a 88 personas entre el 28 de agosto y el 9 de septiembre de 2026, se detalla en el apéndice~[§apx:encuesta]. Sus resultados se contrastan con los supuestos del proyecto:

- **El problema existe.** De quienes tomaron clases particulares, el 70 % encontró al profesor por recomendación, y las dificultades más mencionadas fueron saber si era bueno
          (30 %) y la confianza (20 %). El resultado respalda el diagnóstico de informalidad del capítulo~[§cap:introduccion].
- **La modalidad virtual es aceptada.** El 77,3 % tomaría clases virtuales con un buen profesor, lo que respalda el modelo remoto.
- **La verificación genera confianza.** El 81,8 % confía más en una plataforma con profesores verificados, que además fue la función más valorada (58 %).
- **La IA se valora por su resultado, no como etiqueta.** El 68,2 % querría que la plataforma le recomiende el tutor más adecuado, pero solo el 5,7 % eligió “IA que recomiende profesores” entre las funciones importantes, el último lugar. En cambio, el resumen automático, una función basada en IA descrita por su utilidad, fue la segunda más valorada (56,8 %).
- **El pago dentro de la plataforma no está asegurado.**
          Solo el 35,2 % prefiere pagar dentro de una plataforma antes que por transferencia, y el 34,1 % está en desacuerdo. Es el resultado más desfavorable para el modelo de negocio (riesgo
          R-02).
- **La disposición a pagar es menor que el precio de mercado.** La mediana de la disposición a pagar es de
          USD~4,56 por hora, aproximadamente la mitad del precio horario promedio publicado en Superprof ($13.392, unos
          USD~8,72 al tipo de cambio de $1.535), con el que el capítulo~[§cap:economica] calcula el ticket. El modelo toma el precio de la oferta publicada y no la intención declarada; la diferencia se trata como riesgo (R-05) y se resolverá con los precios efectivos del piloto.

La encuesta tiene limitaciones que acotan estas conclusiones: la muestra no es probabilística, el 90,9 % de las respuestas proviene de la provincia de Buenos Aires y de la Ciudad Autónoma de Buenos Aires, y solo 9 corresponden a tutores. Entre las funciones consultadas figuraba un chat, que el sistema no implementa como módulo propio: los mensajes de texto del aula viajan por el canal de datos del servicio de video
(capítulo~[§cap:metodologia]).

### Entrevistas a especialistas

*Síntesis de las entrevistas (apéndice~[§apx:entrevista*): fecha, entrevistado, aportes principales y contraste con los resultados de la encuesta.]

### Decisiones derivadas

La tabla~[§tab:feedback-decisiones] traduce los hallazgos en decisiones concretas.

**Tabla:** Traducción de los hallazgos en decisiones de diseño

| **Fuente** | **Hallazgo** | **Decisión** | **Estado** |
| --- | --- | --- | --- |
| Encuesta | La IA como etiqueta casi no se valora | Presentar las recomendaciones por su resultado, sin el rótulo “IA” (T-TES-12) | Aplicado |
| Encuesta | El resumen automático es la segunda función más valorada | Resumen como adicional opcional, a costo más un 50 % (ADR-M5-06) | Aplicado; apagado en producción (R-16) |
| Encuesta | Solo el 35,2 % prefiere pagar en la plataforma | Mitigación del riesgo R-02: valor exclusivo dentro de la plataforma | Planificado |
| Encuesta | Mediana de disposición a pagar de USD~4,56 por hora | Medir el precio efectivo en el piloto (riesgo R-05) | Planificado |
| Encuesta | 90,9 % de las respuestas de Buenos Aires | Reencuesta dirigida al interior (riesgo R-08) | Planificado |
| Auditoría | 36 hallazgos, 7 críticos | Corrección de cada uno con prueba de regresión | Aplicado |
| Pruebas en producción | 3 hallazgos altos y uno transversal | Remediación con prueba previa al arreglo | Implementado, por integrar |
| Pruebas en producción | Búsquedas sin relación devolvían tutores | Umbral de relevancia calibrado con el modelo real | Implementado, por integrar |
| Diseño | El audio de la sesión no puede anonimizarse antes del LLM | Transcripción previa y modelo de resumen solo con texto anonimizado; sin resumen con menores (ADR-M6-03) | Aplicado |

## Contraste con el estado del arte

El capítulo~[§cap:marco-teorico] comparó las plataformas existentes
(tabla~[§tab:comparativa]). Los resultados permiten contrastar la propuesta con ellas en tres ejes:

- **matching.** Las plataformas relevadas ofrecen filtros manuales; Tinku implementa un motor de matching semántico con embeddings semánticos. La calibración con consultas propias muestra que separa consultas relevantes de irrelevantes; su valor para los usuarios queda sujeto al indicador I-01 del piloto.
- **Aula y pagos integrados.** Tinku integra en un mismo flujo la reserva, el aula virtual y el cobro con una ventana de 24 horas en la que la plataforma todavía puede reembolsar (escrow), algo que las plataformas relevadas resuelven solo de forma parcial.
- **Seguridad del menor.** Es el diferencial más ambicioso y, a la vez, el que la auditoría encontró más débil. Tras corregir los hallazgos críticos, reincorporar el CAP para los tutores de menores e integrar el kill-switch en el cliente, que funcionó en la prueba en vivo, quedan pendientes su medición en dispositivos reales y la decisión de encendido (riesgo R-01 del capítulo~[§cap:riesgos]).

## Evaluación económica

La evaluación del capítulo~[§cap:economica], con un ticket de
USD~7,42 por sesión, la comisión del 27 % a cargo del tutor y una tasa de descuento del 15 %, arroja en el escenario base un
VAN de USD~18.869 y una TIR del 41,57 %, con un repago simple de 1,99 años y uno descontado de 2,66 años. El escenario pesimista no resulta viable (VAN de USD~-4.410). El VAN
base se anula con una comisión de aproximadamente 18,2 %. El resultado más relevante del proceso fue que la contrastación del modelo con el sistema implementado cambió la conclusión: una versión anterior del modelo restaba la comisión de MercadoPago como costo de la plataforma, pero con el modelo de cobro implementado esa comisión la paga el tutor
(sección~[§sec:costos-variables]). El detalle del cálculo se presenta en el anexo~[§anx:modelo-financiero].

## Síntesis

**Tabla:** Síntesis de resultados

| **Resultados favorables** | **Resultados desfavorables** |
| --- | --- |
| Nueve módulos implementados y desplegados, con 661 pruebas automatizadas en la rama principal y 85,6 % de cobertura | Las pruebas en producción encontraron tres hallazgos altos que la suite no detectaba; su remediación ya está en la rama principal y falta repetir las pruebas en producción |
| Los 36 hallazgos de la auditoría, cerrados con prueba de regresión | Producción quedó, tras las pruebas, en un estado que debe revertirse antes del piloto (R-17) |
| Kill-switch funcionando de punta a punta en la prueba en vivo | Sin medición en dispositivos reales: el piloto no incluye menores |
| La encuesta respalda el problema, la modalidad virtual y la verificación | Solo el 35,2 % prefiere pagar dentro de la plataforma, y la disposición a pagar es la mitad del precio de mercado |
| Escenarios base y optimista económicamente viables | Escenario pesimista no viable |
| CAP obligatorio para dar clases a menores, implementado | Resumen automático implementado pero apagado en producción hasta tener la cláusula legal |

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
- la disposición a pagar por una clase de una hora y a hacerlo dentro de la plataforma, supuestos sobre los que descansa el modelo de ingresos del capítulo~[§cap:economica].

El modelo de ingresos vigente no toma el precio de esta encuesta: el ticket se calcula con los precios publicados en Superprof
(apéndice~[§apx:precio]). La disposición a pagar relevada aquí se usa como contraste de ese precio, y la diferencia entre ambos se analiza como riesgo en el capítulo~[§cap:riesgos] (R-05).

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
- **Datos crudos:** la exportación del formulario, sin datos que identifiquen a las personas, se conserva en el repositorio de la tesis (anexos/encuesta-tinku.csv, anexo~[§anx:repositorios]).

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
- **Funciones consultadas:** la lista de funciones se redactó antes de cerrar el alcance del sistema. Algunas no existen como tales en la versión implementada: el chat no es un módulo propio (los mensajes del aula viajan por el canal de datos del servicio de video) y el resumen automático se ofrece solo como adicional pago en clases entre adultos.

# Entrevistas a especialistas

Como se detalla en el capítulo~[§cap:marco-teorico]
(sección~[§sec:entrevistas]), se definieron dos perfiles de especialista complementarios: un docente o gestor/a institucional y un/a profesional del campo psicopedagógico o del vínculo y la seguridad con menores. En cada caso se documenta el contexto, la ficha de la persona entrevistada y la transcripción por ejes temáticos.

**Estado: [PENDIENTE]** – las entrevistas no se realizaron en el
Sprint 3, como preveía originalmente el cronograma del capítulo~[§cap:metodologia], y se reprogramaron para
*fecha prevista*. Hasta entonces los guiones aquí transcritos constituyen la evidencia del diseño metodológico; los
*completar* marcan los datos que se completarán con la realización efectiva de cada entrevista.

Para el Perfil~1 se preparó además un guion ampliado, de 25 preguntas en seis ejes, que contrasta con la persona entrevistada los resultados de la encuesta (apéndice~[§apx:encuesta]) y los supuestos de los capítulos~[§cap:economica] y~[§cap:riesgos]. Se conserva en el repositorio de la tesis (entrevistas/guion-entrevista-profesor.md, anexo~[§anx:repositorios]).

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

Este apéndice reúne los detalles técnicos del sistema tal como están en la rama principal del repositorio de código (anexo~[§anx:repositorios]) al 14/10/2026. La fuente de cada valor son estos archivos del repositorio:

- backend/pom.xml, frontend/package.json y matching-service/requirements.txt (dependencias);
- backend/src/main/resources/application.yml
          (configuración);
- backend/src/main/resources/db/migration (migraciones de la base de datos).

## Versiones del stack

**Tabla:** Versiones de las dependencias principales

| **Componente** | **Versión** | **Fuente** |
| --- | --- | --- |
| Java (JDK) | 21 | pom.xml; el ‘maven-enforcer-plugin‘ exige ‘[21,22)‘ |
| Spring Boot | 4.1.1 | pom.xml (incluye Spring Security, Data JPA, Flyway, Quartz, Validation, Actuator) |
| jjwt (JWT) | 0.13.0 | pom.xml |
| Testcontainers | la que fija Spring Boot 4.1.1 | pom.xml |
| JaCoCo | 0.8.13 | pom.xml |
| Tesseract (OCR) | paquete del sistema | backend/Dockerfile: ‘tesseract-ocr‘ y ‘tesseract-ocr-spa‘ sobre ‘eclipse-temurin:21-jre‘ |
| Next.js | 16.3.6 | package.json |
| React | ‘\^{‘19.2} | package.json |
| livekit-client | ‘\^{‘2.22.3} | package.json |
| TensorFlow.js (y ‘wasm‘) | 4.22.0 | package.json |
| NSFWJS | 4.3.0 | package.json |
| Playwright / axe-core | ‘\^{‘1.63.0} / ‘\^{‘4.13.0} | package.json |
| oxlint | ‘\^{‘1.82.0} | package.json |
| Python (matching) | 3.12 | matching-service/Dockerfile y CI |
| FastAPI | ‘>=0.141.1‘ | requirements.txt |
| sentence-transformers | ‘>=6.1.0‘ | requirements.txt |
| psycopg / pgvector (Python) | ‘>=3.3.6‘ / ‘>=0.5.0‘ | requirements.txt |
| PostgreSQL + pgvector | 16 | Imagen pgvector/pgvector:pg16 en deploy/docker-compose.coolify.yml; la misma usan las pruebas |
| Copia de seguridad | 16 | Imagen eeshugerman/postgres-backup-s3:16 en el mismo archivo |

## Configuración de los modelos y parámetros

Tinku no entrena modelos propios: usa modelos preentrenados y parámetros de configuración que se pueden cambiar sin tocar el código.
La tabla~[§tab:hiperparametros] lista los valores por defecto.

**Tabla:** Modelos y parámetros por defecto

| **Parámetro** | **Valor** | **Fuente / criterio** |
| --- | --- | --- |
| Modelo de embeddings semánticos | ‘paraphrase-‘‘multilingual-‘‘MiniLM-L12-v2‘, 384 dimensiones | matching-service/main.py; multilingüe y ejecutable en CPU (ADR-M2-01) |
| Puntaje de un tutor | Máxima similitud coseno con cada uno de sus temas | ADR-M2-03 |
| Peso de la reputación | 0,05 (MATCHING_PESO_REPUTACION) | Solo desempata entre tutores de similitud parecida (ADR-M2-02) |
| Similitud mínima para mostrar | 0,3 (MATCHING_SCORE_MINIMO) | ADR-M2-02 |
| Clasificador del kill-switch | NSFWJS (MobileNetV2, 5 clases) | ADR-M3-01 |
| Umbral de detección | 0,85 en 3 muestras consecutivas; con un menor se suman las clases Porn, Hentai y Sexy, entre adultos solo Porn y Hentai | ADR-M3-07 |
| Intervalo de clasificación | 250~ms | Tabla de Tiempos del sistema |
| Transcripción | ‘gpt-4o-mini-transcribe‘ | ADR-M3-04 |
| Resumen | GPT-4o, temperatura 0,3 | ADR-M6-03 |
| Comisión de la plataforma | 27 % | Propiedad ‘marketplace-fee-percent‘; BR-PAG-01, ADR-M5-05 |
| Piso de la tarifa por hora | $6.140 (TARIFA_PISO_HORA_ARS) | BR-PAG-04 |
| Vigencia del JWT | 60 minutos | application.yml |

## Datos utilizados

El único conjunto de datos que el sistema carga es el catálogo cerrado de materias, niveles y temas, sembrado por migración
(V20__m2_temas_seed.sql) y ampliado luego a partir del catálogo vivo (ADR-M2-04). No se usa ningún conjunto de datos personales para entrenar o ajustar modelos. El relevamiento de precios de Superprof que respalda el capítulo~[§cap:economica] se conserva en apendices/superprof-precios.csv y se analiza en el apéndice~[§apx:precio].

## Arquitectura de la aplicación

### Estructura del repositorio

backend/            Spring Boot: un paquete por modulo (identidad, matching, aula, reservas, pagos, resumen, reputacion, admin, seguridad) y migraciones Flyway frontend/           Next.js: aplicacion web y pruebas Playwright (tests/) matching-service/   Python: FastAPI + sentence-transformers deploy/             docker-compose.coolify.yml (produccion) docs/               Constitucion, Tabla de Tiempos, specs, ADR (docs/adr), manual de operacion
.github/workflows/  ci-backend, ci-frontend, ci-matching, ci-e2e, deploy

### Esquema de base de datos

El esquema se construye con 47 migraciones de Flyway (‘V1‘ a
‘V47‘ al 14/10/2026). Como ninguna migración aplicada se edita, las tablas iniciales se completan con migraciones posteriores. Los listados siguientes son extractos textuales de las migraciones.

CREATE TABLE identidad.usuarios (
    id                           UUID PRIMARY KEY DEFAULT gen_random_uuid(), dni                          VARCHAR(20) NOT NULL UNIQUE, nombre                       VARCHAR(150) NOT NULL, apellido                     VARCHAR(150) NOT NULL, fecha_nacimiento             DATE NOT NULL, tipo                         VARCHAR(20) NOT NULL
                                 CHECK (tipo IN ('ADULTO', 'MENOR', 'TUTOR')), capacidad_estudiante         BOOLEAN NOT NULL DEFAULT FALSE, capacidad_adulto_responsable BOOLEAN NOT NULL DEFAULT FALSE, adulto_responsable_id        UUID REFERENCES identidad.usuarios(id), password_hash                VARCHAR(255) NOT NULL, estado_cuenta                VARCHAR(20) NOT NULL DEFAULT 'ACTIVA'
                                 CHECK (estado_cuenta IN ('ACTIVA', 'SUSPENDIDA')), created_at                   TIMESTAMPTZ NOT NULL DEFAULT now(),
    CONSTRAINT chk_adulto_tiene_capacidad CHECK (
        tipo != 'ADULTO' OR (capacidad_estudiante OR capacidad_adulto_responsable)
    ),
    CONSTRAINT chk_menor_tiene_responsable CHECK (
        (tipo = 'MENOR' AND adulto_responsable_id IS NOT NULL) OR
        (tipo != 'MENOR' AND adulto_responsable_id IS NULL)
    )
);

CREATE TABLE reservas.reservas (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(), pagador_id          UUID NOT NULL REFERENCES identidad.usuarios(id), beneficiario_id     UUID NOT NULL REFERENCES identidad.usuarios(id), tutor_id            UUID NOT NULL REFERENCES identidad.usuarios(id), solicitud_origen_id UUID REFERENCES reservas.solicitudes_sesion(id), horario             TIMESTAMPTZ NOT NULL, precio              NUMERIC(10,2) NOT NULL CHECK (precio >= 0), estado              VARCHAR(20) NOT NULL DEFAULT 'pendiente_pago'
                        CHECK (estado IN ('pendiente_pago', 'confirmada', 'en_curso',
                                          'finalizada', 'cancelada', 'no_show_estudiante',
                                          'no_show_tutor', 'no_show_doble'))
    – (se omiten motivo_cancelacion, created_at y sus restricciones)
);

– V30: sin superposicion de rangos horarios, por tutor y por alumno
ALTER TABLE reservas.reservas ADD CONSTRAINT ex_reservas_rango_tutor
    EXCLUDE USING gist (tutor_id WITH =, tstzrange(horario, horario_fin, '[)') WITH &&)
    WHERE (estado <> 'cancelada');
ALTER TABLE reservas.reservas ADD CONSTRAINT ex_reservas_rango_beneficiario
    EXCLUDE USING gist (beneficiario_id WITH =, tstzrange(horario, horario_fin, '[)') WITH &&)
    WHERE (estado <> 'cancelada');

CREATE TABLE pagos.transacciones (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(), reserva_id          UUID NOT NULL REFERENCES reservas.reservas(id), mp_payment_id       VARCHAR        NOT NULL, monto_bruto         NUMERIC(10, 2) NOT NULL CHECK (monto_bruto >= 0), comision_plataforma NUMERIC(10, 2) NOT NULL
                        CHECK (comision_plataforma >= 0 AND comision_plataforma <= monto_bruto), estado              VARCHAR(20) NOT NULL DEFAULT 'retenido_escrow'
                        CHECK (estado IN ('retenido_escrow', 'liberado',
                                          'reembolsado', 'pausado_denuncia')), liberar_at          TIMESTAMPTZ, intentos_liberacion INT NOT NULL DEFAULT 0 CHECK (intentos_liberacion >= 0), created_at          TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE matching.perfiles_tutor_matching (
    tutor_id                UUID PRIMARY KEY REFERENCES identidad.usuarios(id), materias_niveles_ids    UUID[] NOT NULL DEFAULT ”, embedding               VECTOR(384), activo_para_matching    BOOLEAN NOT NULL DEFAULT FALSE
);

El nombre retenido_escrow es anterior al modelo de cobro A
(ADR-M5-02): con ese modelo el dinero ya está en la cuenta del tutor, y el estado indica que todavía no cerró la ventana lógica –hasta 24 horas después de la clase– en la que Tinku puede ordenar el reembolso.

### Diccionario de datos

La tabla~[§tab:diccionario] resume las tablas principales de cada esquema. El detalle de columnas, restricciones e índices está en la migración que se indica y en las que la completan.

{

| **Tabla** | **Contenido** | **Migración** |
| --- | --- | --- |
| identidad.usuarios | Cuenta de cada persona: DNI único, tipo (ADULTO, MENOR, TUTOR), capacidades del adulto, Adulto Responsable del menor, hash de la contraseña y estado de la cuenta | V2 |
| identidad.credenciales_academicas | Título, analítico o matrícula del tutor, con su estado de revisión e intentos | V2 |
| identidad.autorizaciones_tutor | Tutores que el Adulto Responsable autorizó para cada menor | V2 |
| identidad.certificados_antecedentes_penales | CAP del tutor: estado (pendiente, aprobado, rechazado, en revisión legal, vencido) y vencimiento | V6 |
| identidad.aceptaciones_clausula | Quién aceptó qué versión de los Términos y de la cláusula de grabación, y cuándo | V36 |
| matching.temas | Catálogo cerrado de temas por materia y nivel, con su embeddings semánticos | V19, V42 |
| matching.perfiles_tutor_matching | embeddings semánticos del perfil del tutor y si está activo para el matching | V7 |
| matching.temas_sugeridos | Contador agregado de temas buscados sin tutor, sin datos de quién buscó | V43 |
| reservas.franjas_disponibilidad | Franjas semanales o puntuales que publica el tutor | V9 |
| reservas.solicitudes_sesion | Pedido de clase del menor, que no bloquea horario ni genera cobro | V9 |
| reservas.reservas | Clase reservada: pagador, beneficiario, tutor, horario, duración, precio congelado y estado | V9, V29, V46 |
| reservas.paquetes | Paquete mensual de cuatro clases con un solo pago | V46 |
| aula.sesiones_aprendizaje | Sesión de aula (1 a 1 con la reserva): asistencia y estado de la clase | V8 |
| aula.alertas_seguridad | Alertas del kill-switch y referencia al clip de evidencia | V8 |
| aula.confirmaciones_killswitch | Pregunta a la contraparte en la rama de adultos y su vencimiento | V12, V47 |
| pagos.transacciones | Cobro de cada reserva, comisión y estado del escrow | V11 |
| pagos.tarifas_tutor | Precio por hora del tutor y configuración del paquete | V17, V31, V46 |
| pagos.cuentas_mp_tutor | Cuenta de MercadoPago conectada por OAuth, con los tokens cifrados | V39 |
| resumen.resumenes_sesion | Resumen generado y su estado | V15 |
| reputacion.calificaciones | Calificaciones bidireccionales por sesión | V14 |
| seguridad.denuncias, seguridad.sanciones | Denuncias con su estado y evidencia opcional; sanciones aplicadas | V13 |
| admin.admins | Administradores, vinculados a un usuario, con uno de dos roles | V16 |
| admin.log_auditoria_admin | Registro de cada acción de un administrador | V16 |
| admin.notificaciones | Avisos a usuarios y cola de salida del correo | V32 |

}

Las tablas de Quartz (QRTZ_*) viven en el esquema
‘public‘ (ADR-000-01).

### Variables de entorno

La tabla~[§tab:variables-entorno] lista las variables que cambian el comportamiento del sistema en producción. Ninguna credencial se guarda en el repositorio: los valores secretos se cargan en Coolify.

**Tabla:** Variables de entorno principales (sin secretos)

| **Variable** | **Propósito (valor por defecto)** |
| --- | --- |
| TINKU_MENORES_SESIONES_HABILITADAS | Habilita las clases con menores (‘false‘: piloto sin menores) |
| TINKU_RESUMEN_ADICIONAL_HABILITADO | Habilita el adicional de resumen (‘false‘) |
| LLM_PROVEEDOR, LLM_API_KEY | Activa la transcripción y el resumen con OpenAI solo si vale ‘gpt-4o‘; vacío, no sale nada |
| MP_CLIENT_ID, MP_CLIENT_SECRET, MP_OAUTH_REDIRECT_URI | Aplicación de MercadoPago para el modelo A (OAuth por tutor) |
| TINKU_CLAVE_CIFRADO | Clave AES-256 que cifra los tokens de MercadoPago; sin ella no se conecta ninguna cuenta |
| LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET | Proyecto de LiveKit Cloud |
| RESEND_API_KEY, EMAIL_REMITENTE | Correo transaccional; vacíos, no se envía correo |
| MATCHING_SERVICE_URL, MATCHING_SERVICE_TOKEN | Dirección del motor de matching y token compartido |
| RATE_LIMIT_HEADER_IP | Encabezado del que se toma la IP real del cliente detrás de Cloudflare |
| OCR_COMANDO | Programa de OCR (‘tesseract‘) |
| TARIFA_PISO_HORA_ARS | Piso de la tarifa por hora (6140) |
| TINKU_TAG | Versión de las imágenes que despliega Coolify (‘latest‘); permite volver atrás |

## Ejecución de las pruebas

La suite del backend corre solo con JDK~21: el
‘maven-enforcer-plugin‘ rechaza otra versión y, en ese caso, no se ejecuta ninguna prueba. Las pruebas de integración necesitan Docker, porque Testcontainers levanta una base pgvector/pgvector:pg16.

# backend (desde backend/, con JAVA_HOME apuntando a un JDK 21)
./mvnw -B test        # reporte de cobertura: target/site/jacoco

# frontend (desde frontend/) bun run lint          # oxlint bun run test:e2e      # Playwright + axe-core

# motor de matching (desde matching-service/) uv run pytest -q

Al 14/10/2026 la suite del backend registraba 661 pruebas, 0 fallas, 0
errores y 5 omitidas –las pruebas del OCR real, que se saltean si el equipo no tiene Tesseract instalado y que en el CI sí corren–, con una cobertura de líneas del 85,6 % medida con JaCoCo (ADR-000-05).

# Prompts utilizados con herramientas de IA generativa

## Criterios de registro

- **Alcance.** Se registran las instrucciones cuyo resultado tuvo un impacto significativo en el sistema o en el documento.
          Los prompts se transcriben con leves correcciones de redacción, sin alterar su contenido.
- **Verificación.** Para cada resultado se indica cómo se verificó antes de incorporarlo (regla 3 de la declaración de uso de IA).
- **Autoría.** Las salidas se describen como evidencia; el texto final del documento surge de la revisión y adaptación del autor.
- **Vigencia.** Algunos resultados se reemplazaron después, al contrastar el documento con el sistema implementado. Cuando es así, se indica qué quedó vigente.

## Desarrollo del sistema

El desarrollo con asistentes de programación —OpenCode en las primeras etapas y Claude Code después— no se guió por prompts aislados, sino por instrucciones persistentes versionadas en el repositorio
(anexo~[§anx:repositorios]): el archivo ‘AGENTS.md‘, la
Constitución, las especificaciones, los planes técnicos y la lista de tareas. Ese conjunto constituye el registro completo de lo que se le pidió a cada agente: cada bloque de tareas en su propia rama, al menos una prueba de integración por historia de usuario, una prueba que falla antes de cada arreglo y un registro de decisión escrito para cada decisión técnica que lo requiere. Se transcriben dos de las reglas de
‘AGENTS.md‘ que más condicionaron el resultado.

> **Instrucción IA:** Ante dos soluciones que cumplen el mismo requisito, la más simple. No justifiques una decisión técnica con “buena práctica genérica”: justificala contra un desarrollador y un presupuesto de
USD 0 a 100 por mes, o no la tomes.
> **Respuesta IA:** Arquitectura de monolito modular con nueve módulos de dominio y un único servicio propio separado, el de matching.
Verificación: cada desvío quedó documentado en un registro de decisión
(ADR) validado por el autor.

> **Instrucción IA:** La rama del kill-switch con un menor presente nunca continúa la sesión ni le pregunta al menor si vio algo: corta directamente. Si una tarea deja dudas sobre cuál de los dos casos aplica, tratala como si hubiera un menor.
> **Respuesta IA:** Implementación del kill-switch con dos ramas diferenciadas, en el backend y en el cliente. Verificación: prueba de extremo a extremo de la rama de seguridad completa (sesión con menor, corte, suspensión, alerta y resolución del administrador) y prueba en vivo con salas de video reales (capítulo~[§cap:resultados).]

El historial de git deja registrada la magnitud de esta asistencia: al
14 de octubre de 2026, 129 de los 482 commits de la rama principal del repositorio del sistema figuran con autor “Claude”, entre ellos 76 de los 196 que modifican pruebas automatizadas. Las pruebas, por lo tanto, no se escribieron exclusivamente a mano: su confiabilidad no descansa en quién las escribió, sino en que cada una se revisó antes de integrarse y en que la auditoría técnica y las pruebas en producción verificaron el sistema desde fuera de la suite.

## Consultas de contraste

Gemini y ChatGPT se consultaron de forma esporádica, como segunda y tercera opinión sobre decisiones puntuales. Sus respuestas no se incorporaron como texto al documento.
*Transcribir, si se conservaron, una o dos consultas representativas y la decisión que motivaron.*

## Elaboración del documento

Los siguientes prompts se utilizaron con Claude Code durante la revisión y redacción de los capítulos~[§cap:economica] y~[§cap:riesgos] y de los apéndices.

> **Instrucción IA:** Agregué los resultados de la encuesta y el Excel con el presupuesto y las proyecciones. Revisá si tengo que modificar algo en la tesis en función de esto y decime todo lo que falta completar.
> **Respuesta IA:** Detectó inconsistencias entre capítulos: un equipo de cuatro perfiles en la evaluación económica frente a un desarrollo unipersonal en el resto del documento, el costo del servidor de aplicación omitido, un precio de sesión sin respaldo frente a la disposición a pagar relevada, y diferencias entre el documento y el repositorio. Además, redactó el apéndice~[§apx:encuesta a partir de los datos crudos. Verificación: cada inconsistencia se contrastó con el texto y el repositorio, y las frecuencias de la encuesta se recalcularon sobre el archivo original.]

> **Instrucción IA:** Busquemos y analicemos empíricamente los costos de las plataformas con sus planes reales actuales, pensando qué es lo mejor para este caso.
> **Respuesta IA:** Relevamiento de las tarifas públicas de los proveedores de alojamiento, video y LLM, y del costo de grabar el audio de las sesiones, no contemplado hasta entonces. Verificación: cada tarifa se consultó en la página del proveedor. Vigencia: la infraestructura finalmente adoptada es un servidor propio (ADR-000-07), y las tarifas vigentes son las citadas en el capítulo~[§cap:economica.]

> **Instrucción IA:** Toda la tesis debe estar en dólares. Si necesitás el tipo de cambio, usá el del BNA al cierre de la encuesta.
> **Respuesta IA:** Conversión de los rangos de la encuesta con la cotización vendedora del 9 de septiembre de 2026 [bna2026., Verificación: cotización, contrastada, en, la, fuente, citada., Vigencia:, el, mismo, tipo, de cambio, se, usa, en, el, capítulo~[§cap:economica] y en el sistema.]

> **Instrucción IA:** Quiero saber si las horas con las que se calcula la inversión son realistas o no, y compararlas con lo que costó de verdad.
> **Respuesta IA:** Estimación del esfuerzo registrado en el repositorio y propuesta de evaluar solo la inversión incremental. Verificación: métricas recalculadas sobre el repositorio; la elección del criterio fue del autor. Vigencia: el capítulo~[§cap:economica valoriza finalmente la inversión a precio de mercado
(tabla~tab:inversion]).

> **Instrucción IA:** Construí la tasa de descuento con fuentes reales.
> **Respuesta IA:** Tasa construida por acumulación de tasa libre de riesgo, beta sectorial, prima de mercado y prima de riesgo país. Verificación: cada componente se consultó en su fuente primaria. Vigencia: el capítulo~[§cap:economica adopta finalmente una tasa del 15 % anual en dólares.]

> **Instrucción IA:** Arrancá con el capítulo 6 siguiendo las indicaciones de la cátedra.
> **Respuesta IA:** Borrador del análisis de riesgos a partir de la encuesta, el modelo financiero y el estado del repositorio. Verificación: cada riesgo se contrastó con la evidencia que cita. Vigencia: el capítulo se actualizó después contra el estado del sistema al 15 de octubre de
2026; varios riesgos del borrador ya se habían resuelto o cambiado de causa, y se agregaron los que surgieron de las pruebas en producción.

> **Instrucción IA:** Alinear la tesis a lo que está en el sistema, refutando y justificando las decisiones de cambio.
> **Respuesta IA:** Relevamiento de las diferencias entre los capítulos y el repositorio del sistema, con la cita de cada fuente, y reescritura de los pasajes afectados, con el registro de cada cambio de diseño en la sección~[§sec:decisiones-implementacion. Verificación: cada afirmación nueva remite a una especificación, un registro de decisión o el código del sistema, y las cifras económicas se recalcularon con el modelo del anexo~anx:modelo-financiero].

# Defensa del precio: relevamiento de tarifas en Superprof

## Relevamiento

Se relevaron los avisos de apoyo escolar publicados en el sitio de
Superprof Argentina [superprof], registrando el precio por hora que cada profesor declara. El resultado fue:

**Tabla:** Resultado del relevamiento (pesos argentinos por hora)

| **Indicador** | **Valor** |
| --- | --- |
| Avisos relevados | 414 |
| Suma de precios horarios | $5.544.467 |
| Precio horario promedio | $13.392,43 |
| Mediana | $12.000 |
| Primer y tercer cuartil | $8.000 y $18.000 |
| Mínimo y máximo | $1.990 y $60.000 |
| Avisos en modalidad online | 387 (93 %) |

El detalle de los 414 avisos se conserva en
‘apendices/superprof-precios.csv‘. Este promedio funciona como precio de referencia de mercado: es lo que hoy cobra un profesor particular en la plataforma líder, contra lo cual compite la oferta de Tinku.

## Traslado al ticket promedio

El ticket del modelo es un promedio ya ponderado por la mezcla de duraciones (Ec.~[§eq:duracion], $d=51$ minutos, una duración media supuesta), por lo que el precio horario se multiplica por
$51/60 = 0{,}85$ y se convierte a dólares al tipo de cambio de $1.535
por USD (Ec.~[§eq:ticket]), el mismo con el que el sistema expresa en pesos el piso de tarifa de USD 4 por hora ($6.140, sección~[§sec:piso-tarifa]). El resultado es un ticket de USD~7,42.
Con el reparto del cobro que implementa el sistema
(sección~[§sec:costos-variables]), la plataforma percibe la comisión completa del 27 %, USD~2,0034 por sesión, y el tutor recibe el
66,96 % del precio, una vez descontada también la comisión de
MercadoPago.

El precio horario promedio del relevamiento ($13.392,43) supera holgadamente al piso de tarifa ($6.140). Aun así, 78 de los 414 avisos relevados (19 %), entre ellos los 36 publicados a $1.990, declaran un precio por hora inferior al piso: esos profesores no podrían publicar su tarifa actual en Tinku. El precio horario con el que el VAN del escenario base se anula, unos $9.010, queda entre el primer cuartil y la mediana del relevamiento; 129 avisos (31 %) están por debajo de él.

El tipo de cambio es un parámetro del modelo. La tabla~[§tab:sens-precio] muestra cómo cambian el ticket, los puntos de equilibrio y los indicadores del escenario base si se usara otro valor, manteniendo el resto de los supuestos.

**Tabla:** Sensibilidad del escenario base al tipo de cambio

| **ARS/USD** | **Ticket** | **Margen** | **Sesiones eq. Año 1** | **Sesiones eq. Año 5** | **VAN (USD)** | **TIR** |
| --- | --- | --- | --- | --- | --- | --- |
| 1.400 | 8,13 | 2,20 | 1.620 | 2.002 | 24.380 | 48,56 % |
| **1.535** | **7,42** | **2,00** | **1.774** | **2.194** | **18.869** | **41,57 %** |
| 1.700 | 6,70 | 1,81 | 1.965 | 2.430 | 13.279 | 34,20 % |
| 1.900 | 5,99 | 1,62 | 2.198 | 2.717 | 7.767 | 26,58 % |
| 2.100 | 5,42 | 1,46 | 2.429 | 3.003 | 3.342 | 20,13 % |

El margen de la tabla es la comisión completa del 27 % sobre el ticket, porque la comisión de MercadoPago la paga el tutor
(sección~[§sec:costos-variables]), y los costos fijos son los de la tabla~[§tab:costos-fijos]. Cuanto más pesos cuesta el dólar, menos dólares equivale el precio local y peor resulta el modelo: por encima de aproximadamente $2.281 por USD el VAN del escenario base pasa a ser negativo. En la versión anterior del modelo, que restaba la comisión de
MercadoPago como costo de la plataforma, ese umbral era de unos $1.670.

## Limitaciones

- Son precios *pedidos* por los profesores, no pagados por los alumnos; los avisos pueden incluir descuentos o primeras clases gratis.
- 36 avisos figuran a $1.990 por hora, probablemente un precio promocional o de entrada. Excluyéndolos, el promedio sube a
          $14.478 y la mediana a $14.000. Se adopta el promedio completo por ser el más conservador.
- El tipo de cambio es un parámetro del modelo, no un dato: la inflación en pesos erosiona el precio en dólares entre relevamientos.

# Diagramas UML

Este apéndice modela Tinku con nueve diagramas UML. Complementan la arquitectura del capítulo~[§cap:marco-tecnologico]
(sección~[§sec:infraestructura], tabla~[§tab:componentes] y figura~[§fig:arquitectura]) y el modelo de datos de la sección~[§sec:modelo-datos], sin repetir sus justificaciones: las diferencias entre el diseño inicial y lo implementado se registran en la sección~[§sec:decisiones-implementacion]. Los nombres de clases, estados, eventos, trabajos programados y *endpoints* que aparecen son los del código del sistema –el backend en Spring Boot, el frontend en
Next.js y el motor de matching en Python–, publicado en los repositorios del anexo~[§anx:repositorios]. Las fuentes editables, en
PlantUML, están en figuras/uml/.

Los plazos que muestran los diagramas (15 minutos para pagar, sala en
T$-$5, no-show en T$+$10, corte automático 5 minutos después del fin agendado, 24 horas de ventana de escrow) salen de la Tabla de
Tiempos del sistema. La ventana mínima de anticipación para reservar se nombra sin cifra, porque es un parámetro de esa tabla que se ajusta con la operación.

## Diagrama de actividad

La figura~[§fig:uml-actividad] recorre el ciclo completo de una clase, desde la búsqueda hasta la calificación, con tres carriles: quien paga
(Estudiante adulto o Adulto Responsable), el backend de Tinku y el tutor. Si la clase la pide un menor, la crea como Solicitud de Sesión y su
Adulto Responsable la aprueba; el adulto también puede reservar directamente para su menor. Antes de crear la Reserva se exige que el tutor tenga su cuenta de MercadoPago conectada por OAuth, porque el cobro se hace con su token y el dinero entra a su cuenta (ADR-M5-02); la
Transacción queda en retenido_escrow, que en este modelo es una ventana lógica en la que Tinku todavía puede reembolsar. El diagrama distingue el cierre manual (botón Finalizar) del corte automático, que es el único que aplica el umbral del 50 % de duración efectiva para separar una sesión finalizada de una interrumpida con reembolso total.
El resumen corre solo si se contrató el adicional, que existe únicamente entre adultos.

<!-- Figura: Diagrama de actividad: ciclo de una clase -->

## Diagrama de casos de uso

La figura~[§fig:uml-casos-uso] muestra los actores humanos y los sistemas externos (MercadoPago, LiveKit Cloud y OpenAI). Estudiante adulto, Adulto Responsable, Estudiante menor y tutor especializan a
Usuario registrado; el Visitante solo puede registrarse, porque la búsqueda y los perfiles requieren una sesión iniciada. El menor busca, solicita sesiones y participa en el aula, pero no paga, no autoriza tutores ni denuncia. Los administradores no son un tipo de usuario: se modelan como dos actores, uno por rol (Moderación y Seguridad, Soporte
Financiero), como se describe en la sección~[§sec:modelo-datos]. El kill-switch no lo acciona una persona: es una detección automática del clasificador que corre en el navegador y extiende la participación en el aula; entre adultos, la contraparte confirma o descarta la detección.

<!-- Figura: Diagrama de casos de uso de Tinku

La figura~[§fig:uml-estados-reserva] modela ‘EstadoReserva‘. Una
Reserva nace en pendiente_pago y pasa a ‘confirmada‘ cuando el pago se aprueba por cualquiera de sus vías (aviso de MercadoPago, vuelta del navegador, conciliación periódica o modo *bypass*). El cambio de horario no la saca de ‘confirmada‘ y nunca la cancela; la cancelación la decide el pagador, el tutor o el propio sistema (sanción, baja del menor o CAP vencido). Termina en ‘finalizada‘,
‘cancelada‘ o en alguno de los tres estados de no-show. Mientras la clase transcurre, la Reserva sigue en ‘confirmada‘: el estado en vivo lo lleva la Sesión de Aprendizaje, y el valor en_curso del enumerado queda reservado.

La figura~[§fig:uml-estados-sesion] completa el modelo con los estados de la Sesión de Aprendizaje y de la Transacción. La sesión pasa a en_curso con el primer ingreso; el no-show y el corte automático con el par roto antes del fin agendado la dejan en finalizada_anticipada. En la Transacción, una denuncia pausa el escrow y su resolución lo destraba según el resultado (infundada: vuelve a contar las 24 horas; fundada: se libera al tutor; escalada: se reembolsa); el kill-switch lo aparta en pausado_alerta, que prevalece sobre la denuncia y termina en reembolso total al resolverse la Alerta.

<!-- Figura: Diagrama de máquina de estados de la Reserva -->

<!-- Figura: Diagrama de máquina de estados de la Sesión de Aprendizaje y de la Transacción -->

## Diagrama de secuencia

La figura~[§fig:uml-secuencia] detalla la reserva directa y el pago. El frontend crea la Reserva y pide la preferencia de MercadoPago, que el backend genera con el token OAuth del tutor y con la comisión de
Tinku como ‘marketplace_fee‘. El aviso firmado llega a
‘MercadoPagoWebhookController‘, que verifica la firma y resuelve el token del tutor; ‘EscrowService‘ vuelve a consultar el pago con un cliente HTTP propio (sin SDK), bloquea la fila de la Reserva y, si el monto coincide con el precio congelado, crea la Transacción en retenido_escrow y confirma la Reserva. Con esa confirmación se publica el evento ‘ReservaConfirmadaEvent‘, a partir del cual el módulo de aula crea la Sesión y agenda sus trabajos. Si no llegan ni el aviso ni la vuelta del navegador, la conciliación periódica sigue el mismo camino.

<!-- Figura: Diagrama de secuencia: reserva directa y pago -->

## Diagrama de comunicación

La figura~[§fig:uml-comunicacion] muestra, con mensajes numerados, los objetos que colaboran en el aula virtual: la emisión del token de LiveKit
(que, con un menor, exige que el clasificador del navegador esté listo), los *webhooks* de ingreso y salida, la cancelación del trabajo de no-show, el disparo del kill-switch (mensajes K1 a K4, que cierran la sala) y el corte automático, junto con los eventos que reciben los módulos de pagos y de resumen.

<!-- Figura: Diagrama de comunicación: aula virtual -->

## Diagrama de tiempos

La figura~[§fig:uml-tiempos] ubica en una línea de tiempo los plazos de una clase de 60 minutos: pago dentro de los 15 minutos, creación de la sala en T$-$5, decisión de no-show en T$+$10 y corte automático 5 minutos después del fin agendado. La sesión pasa a en_curso con el primer ingreso, y al cierre se fija ‘liberarAt‘ 24 horas después del fin efectivo de la clase.

<!-- Figura: Diagrama de tiempos de una sesión -->

## Diagrama de visión general de interacciones

La figura~[§fig:uml-vision-general] encadena las interacciones del sistema como fragmentos ‘ref‘: búsqueda, solicitud o reserva directa, pago, ingreso al aula, no-show o kill-switch, cierre y, en paralelo, el cierre de la ventana de escrow (que verifica en
MercadoPago que el pago siga aprobado), el resumen automático y la calificación.

<!-- Figura: Diagrama de visión general de interacciones -->

## Diagrama de clases

La figura~[§fig:uml-clases] presenta las entidades del dominio agrupadas por módulo, con sus atributos principales, sus enumeraciones de estado y sus multiplicidades; es la vista detallada del modelo que resume la sección~[§sec:modelo-datos]. ‘Usuario‘ concentra las identidades: una Reserva lo referencia tres veces (pagador, beneficiario y tutor), un menor se vincula con su Adulto Responsable por una autorreferencia y ‘Admin‘ es una entidad aparte, vinculada a un usuario, con uno de dos roles. Un ‘Paquete‘ agrupa cuatro Reservas, y la cuenta de MercadoPago conectada del tutor (‘CuentaMpTutor‘) guarda su token cifrado.

<!-- Figura: Diagrama de clases del modelo de dominio -->

## Diagrama de componentes

La figura~[§fig:uml-componentes] detalla la vista de la figura~[§fig:arquitectura]: el monolito modular Spring Boot con sus nueve módulos y el planificador Quartz, el frontend Next.js con el clasificador del kill-switch, el motor de matching en Python (el único proceso propio separado), PostgreSQL con pgvector, el respaldo cifrado hacia Cloudflare R2 y los servicios externos. Las flechas punteadas entre módulos son eventos de dominio en memoria; el único ingreso desde internet es el túnel de Cloudflare.

<!-- Figura: Diagrama de componentes de Tinku{ -->

# Anexos

# Repositorios de código fuente

El trabajo se reparte en dos repositorios de GitHub, ambos activos. Las referencias a un ADR (por ejemplo, ADR-000-07), a una especificación funcional (por ejemplo, Spec M5) o a la Constitución del proyecto que aparecen en los capítulos remiten a los documentos del repositorio del sistema.

## Sistema Tinku (‘usal-tinku‘)

smercadocarbone/usal-tinku

Código del sistema y su documentación de diseño. La rama
‘main‘ es la que está en producción.

- backend/: monolito modular en Java 21 y Spring Boot, con las migraciones de Flyway en backend/src/main/resources/db/migration.
- frontend/: aplicación web en Next.js, con las pruebas de Playwright en frontend/tests.
- matching-service/: el motor de matching, escrito en Python con FastAPI y la biblioteca sentence-transformers.
- deploy/: definición de producción para Coolify
          (docker-compose.coolify.yml); .github/workflows/: los flujos de CI/CD.
- docs/Constitucion_Tinku.md: principios que gobiernan las decisiones del proyecto y su historial de enmiendas.
- docs/Tabla_Tiempos_Tinku.md: Tabla de Tiempos, única fuente de todos los plazos del sistema.
- docs/specs/: especificaciones funcionales de los nueve módulos (Spec_M1 a Spec_M9).
- docs/adr/: registros de decisión de arquitectura
          (ADR-000-01 en adelante), con el contexto, las alternativas descartadas y los riesgos aceptados de cada decisión.
- docs/operacion/RUNBOOK_produccion.md: manual de operación de producción (despliegue, vuelta atrás, copia y restauración de la base).
- AGENTS.md: reglas de trabajo para el desarrollo, incluido el uso de asistentes de IA.

Cómo ejecutarlo y probarlo: ver el README.md del repositorio y el apéndice~[§apx:tecnicos].

## Tesis (‘usal-tinku-docs‘)

smercadocarbone/usal-tinku-docs

Fuente en de este documento (capítulos, apéndices, anexos, figuras y bibliografía), armada sobre la plantilla de Proyecto Final de
Ingeniería Informática de la USAL. Incluye el relevamiento de precios de
Superprof (apendices/superprof-precios.csv) y un archivo
‘LICENSE‘ (CC0~1.0).

# Modelo financiero

Este anexo documenta el modelo con el que se calcularon los indicadores del capítulo~[§cap:economica], de modo que cualquier lector pueda reproducirlos a partir de los parámetros declarados. El modelo es determinístico: no tiene supuestos ocultos fuera de los que se listan a continuación, y todos los montos están expresados en dólares estadounidenses.

## Parámetros de entrada

**Tabla:** Parámetros del modelo financiero y su origen

| **Parámetro** | **Valor** | **Origen** |
| --- | --- | --- |
| Precio horario promedio | $13.392,43 | Relevamiento de 414 avisos de Superprof (apéndice~[§apx:precio]) |
| Duración media de la sesión | 51 min | Ecuación~[§eq:duracion] |
| Tipo de cambio | $1.535 por USD | BNA, 09/09/2026; el mismo que usa el sistema para el piso de tarifa |
| Ticket promedio | USD~7,42 | Ecuación~[§eq:ticket] |
| Comisión de la plataforma | 27 % | Regla BR-PAG-01 (ADR-M5-05) |
| Comisión de MercadoPago | 6,04 % | A cargo del tutor en el modelo de cobro A (ADR-M5-02); no es costo de la plataforma |
| Margen de la plataforma por sesión | USD~2,0034 | Ticket $$ comisión |
| Inversión inicial (Año 0) | USD~25.730 | Tabla~[§tab:inversion] |
| Costos fijos anuales (Años 1 a 5) | USD~3.555 a USD~4.395 | Tabla~[§tab:costos-fijos] |
| Sesiones anuales por escenario | tabla~[§tab:demanda] | Alumnos activos $$ 3 clases por mes $$ 12 |
| Tasa de descuento | 15 % anual en USD | Sección de tasa de descuento del capítulo~[§cap:economica] |

El adicional de resumen y el paquete mensual no entran en el flujo base: el primero se cobra a costo más un 50 % y su aporte es marginal
(sección~[§sec:adicional-resumen]); el segundo no tiene datos de adopción y se evalúa como sensibilidad del ticket
(sección~[§sec:sensibilidad]).

## Cadena de cálculo

Para cada escenario y cada año $t$ de 1 a 5:

- ingreso neto$_t$ = sesiones anuales$_t$ $$ margen de la plataforma por sesión;
- flujo neto$_t$ = ingreso neto$_t$ $-$ costos fijos anuales$_t$; el flujo del Año 0 es la inversión inicial con signo negativo;
- el VAN, la TIR y los períodos de repago simple y descontado se obtienen de la serie de flujos netos con las ecuaciones de la sección~[§sec:indicadores-formulas].

Los análisis de sensibilidad del capítulo~[§cap:economica] se obtienen variando un parámetro por vez sobre esta misma cadena y buscando, cuando corresponde, el valor que anula el VAN del escenario base (por ejemplo, la comisión de aproximadamente 18,2 % o el ticket de USD~4,99 por sesión).

## Flujos por escenario

La tabla~[§tab:flujos-escenarios] presenta los flujos netos de los tres escenarios; el desglose del escenario base se encuentra en la tabla~[§tab:flujo-caja].

**Tabla:** Flujos netos por escenario (en USD)

| **Escenario** | **Año 0** | **Año 1** | **Año 2** | **Año 3** | **Año 4** | **Año 5** |
| --- | --- | --- | --- | --- | --- | --- |
| Pesimista | $-25.730$ | 5.821 | 4.258 | 7.625 | 5.942 | 9.308 |
| Base | $-25.730$ | 10.869 | 15.077 | 11.231 | 16.760 | 13.636 |
| Optimista | $-25.730$ | 16.639 | 26.616 | 20.607 | 30.464 | 24.454 |

**Tabla:** Indicadores resultantes por escenario

| **Escenario** | **VAN (USD)** | **TIR** | **Repago simple** | **Repago descontado** |
| --- | --- | --- | --- | --- |
| Pesimista | $-4.410$ | 8,09 % | 4,22 años | no se alcanza |
| Base | 18.869 | 41,57 % | 1,99 años | 2,66 años |
| Optimista | 51.990 | 78,24 % | 1,34 años | 1,56 años |

## Versiones anteriores del modelo

Las primeras versiones del modelo se construyeron en una planilla de cálculo que usaba un ticket derivado de la disposición a pagar de la encuesta, restaba la comisión de MercadoPago como costo de la plataforma e incluía una partida fija de procesamiento de LLM. Esa planilla no se incluye en este trabajo porque sus cifras contradicen el modelo vigente: el ticket se recalculó con el relevamiento de Superprof
(apéndice~[§apx:precio]), con el modelo de cobro A la comisión de
MercadoPago la paga el tutor, y el único uso de LLM es el adicional de resumen, que se cobra aparte. El efecto de los dos últimos cambios sobre los indicadores se presenta en la tabla~[§tab:puente].

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
* `[rpgu]` *Ministerio de Capital Humano. Dirección Nacional de Gestión Universitaria. Registro Público de Graduados Universitarios (2026). https://registrograduados.siu.edu.ar/*
* `[refe]` *Ministerio de Capital Humano. Dirección de Validez Nacional de Títulos y Estudios. Registro Federal de Egreso (ReFE) (2026). https://www.argentina.gob.ar/educacion/direccion-de-validez-nacional-de-titulos-y-estudios/registro-federal-de-egreso-refe*
* `[mpmarketplace]` *Mercado Pago. Integrar checkout en marketplace (2026). https://www.mercadopago.com.br/developers/en/docs/checkout-pro/how-tos/integrate-marketplace*
* `[openaitranscribe2026]` *OpenAI. GPT-4o Mini Transcribe -- modelo y tarifa (s. f.). https://developers.openai.com/api/docs/models/gpt-4o-mini-transcribe*
* `[openaipricing2026]` *OpenAI. Precios de la API de OpenAI (s. f.). https://openai.com/api/pricing/*
* `[bna2026]` *El Cronista. Dólar oficial: cómo cerró su cotización hoy miércoles 9 de septiembre (s. f.). https://www.cronista.com/finanzas-mercados/dolar-oficial-como-cerro-su-cotizacion-hoy-miercoles-9-de-septiembre/*

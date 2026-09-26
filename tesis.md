# Tinku: una plataforma digital de marketplace educativo para conectar estudiantes y tutores académicos a escala nacional

> Autor: Santiago Mercado Carbone
> Año académico: 2026
> Palabras clave: marketplace educativo, tutorías particulares, inteligencia artificial, matching semántico, educación personalizada

## Agradecimientos

*Texto de los agradecimientos.*

## Declaración sobre el uso de IA

**Ejemplo.**
Se reconoce el uso de *herramienta y versión* para
*tareas: revisión de redacción, generación de código de prueba, resumen de papers, etc.*. Todas las salidas fueron revisadas, verificadas y adaptadas por el autor, que asume la responsabilidad total sobre el contenido de este documento.

> **Instrucción IA:** Reescribí este párrafo en registro académico impersonal sin cambiar su contenido.
> **Respuesta IA:** (texto devuelto por la herramienta, luego editado)

*Declaración propia: herramientas utilizadas, tareas asistidas y cómo se verificaron los resultados.*

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
          (sentence-transformers + FAISS) para la sugerencia de tutores compatibles, implementando un factor de ponderación o multiplicador de puntaje (*boost*) para aquellos perfiles que hayan validado voluntariamente su CAP.
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
          API públicas. Esta restricción impide automatizar dicho proceso en el MVP. En consecuencia, la plataforma centrará sus esfuerzos obligatorios de seguridad y confianza en la rigurosa verificación de los antecedentes académicos.
          Adicionalmente, para mitigar la barrera de verificación de antecedentes penales, se habilitará su carga manual de forma optativa, incentivando a los tutores mediante una mejora algorítmica en su visibilidad. El proceso de registro básico exigirá únicamente la demostración empírica de los conocimientos del tutor mediante la presentación de historial académico, títulos de grado o certificaciones pertinentes. Esta estrategia no solo sortea el impedimento técnico estatal, sino que alinea el sistema de admisión directamente con el objetivo central de la plataforma: asegurar la excelencia académica del apoyo escolar.
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

A nivel funcional, la plataforma integrará un microservicio de matching impulsado por IA y un módulo de aula virtual soportado por la tecnología de LiveKit (WebRTC). El flujo económico estará cubierto mediante la integración con MercadoPago para la gestión de pagos bajo la modalidad de escrow. Para potenciar la experiencia educativa, se implementará un módulo de resumen automático de sesiones utilizando un LLM (como GPT-4o o Gemini 2.0 Flash) que procesa audio nativamente. Adicionalmente, el MVP contará con un sistema de calificaciones y reputación bidireccional, junto con un panel de administración básico para la gestión interna de la plataforma. La plataforma incluye, además, un portal de denuncias con verificación de veracidad, que ante cada denuncia preserva de forma automática la evidencia de la sesión correspondiente y deriva la resolución final a revisión manual.

Por último, es importante delimitar que este proyecto no incluye ciertas características en su fase inicial. Quedan excluidos de este alcance: el desarrollo de aplicaciones móviles nativas; la integración automatizada mediante API con sistemas estatales (requiriéndose en su lugar la carga y verificación manual del CAP); el desarrollo de un módulo de accesibilidad completo; la implementación de un modelo de suscripción premium; la posibilidad de extender la duración de una sesión de videollamada en curso mediante un cobro adicional; y la incorporación de tutores menores de edad. Todas estas iniciativas y funcionalidades no incluidas quedarán debidamente documentadas como propuestas para el trabajo a futuro.

## Limitaciones

- **Límite de validación:** la validación de la hipótesis se realizará con un grupo piloto acotado. Los resultados son indicativos de la validez funcional del sistema, no estadísticamente representativos del mercado total.
- **Límite de verificación de tutores:** en el MVP, la verificación combina un chequeo automático de mayoría de edad mediante reconocimiento óptico (OCR) sobre la fecha de nacimiento del DNI cargado, y una revisión manual final de la autenticidad del documento y la correspondencia de los certificados académicos declarados. La verificación automatizada de antecedentes vía API queda fuera de alcance, reemplazándose por la exigencia y revisión manual obligatoria del CAP tramitado por el tutor vía Mi
          Argentina, con actualización anual; no debe confundirse con la verificación de edad, que también se realiza.
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
| Infraestructura cloud | Vercel (plan Hobby) para el frontend, Supabase (plan gratuito) para la base de datos Postgres, Upstash (plan gratuito) para Redis, y backend alojado inicialmente en infraestructura propia mediante Coolify y Cloudflare Tunnel, con migración planificada a un VPS de entre 10 y 25 USD mensuales antes del piloto. Estimación de costo: USD 0 en fase de desarrollo, hasta  25 USD/mes en la fase de piloto. |
| APIs externas | Para el motor de matching semántico: sentence-transformers junto con FAISS, con procesamiento local y sin costo de API por request. Para la transcripción y el resumen de sesión, y para el asistente conceptual: un LLM a confirmar entre GPT-4o y Gemini 2.0 Flash para la transcripción y resumen directo de audio, según relación costo-calidad al momento de la implementación (capítulos [§cap:marco-tecnologico] y [§cap:economica]). MercadoPago: sin costo fijo, comisión por transacción, con SDK oficial en Java. LiveKit Cloud: plan gratuito Build de 5.000 minutos de participante por mes. |
| Herramientas de desarrollo | OpenCode + Neovim (editor principal), GitHub (control de versiones), Figma (diseño UX), Postman (testing API), Jest (testing unitario). Todas en planes gratuitos o estudiantiles. |
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

El motor de matching de Tinku se apoya conceptualmente en dos cuerpos teóricos: los sistemas de recomendación (*recommender systems*), que buscan predecir la afinidad entre dos entidades a partir de sus atributos; y el procesamiento de lenguaje natural (NLP) aplicado a la representación semántica de texto mediante embeddings semánticos. Un embeddings semánticos es una representación vectorial de un texto en un espacio de alta dimensionalidad. Modelos como los sentence-transformers generan vectores a partir de oraciones completas, superando las búsquedas por palabras clave. Sobre este espacio, estructuras como FAISS (Facebook AI Similarity Search) permiten búsquedas de similitud eficientes.

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
| Servicios de IA | matching semántico, transcripción y resumen de sesión, asistente conceptual, kill-switch de seguridad | sentence-transformers + FAISS, LLM GPT-4o (resumen) y gpt-4o-mini-transcribe (transcripción), clasificador on-device |
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
| Tecnología | Next.js 16 + React 19 (App Router), elegido por el posicionamiento en buscadores de los perfiles públicos de tutores |
| Por qué se eligió | Conocimiento previo del desarrollador (capítulo~[§cap:introduccion], sección~[§sec:recursos]), ecosistema maduro, gran disponibilidad de componentes para formularios, calendarios y videollamada embebida |
| Alternativas evaluadas | Vue.js – descartado por menor familiaridad del desarrollador, lo que hubiera consumido tiempo de aprendizaje no disponible en el cronograma de seis meses |
| Formato de despliegue | PWA, consistente con la exclusión de app móvil nativa del alcance (capítulo~[§cap:introduccion], sección~[§sec:alcance]) |

### Backend

**Tabla:** Backend: decisión tecnológica

| **Ítem** | **Detalle** |
| --- | --- |
| Tecnología | Java 21 + Spring Boot 4.1.1 (la rama 3.5 dejó de recibir parches gratuitos el 30/06/2026) |
| Por qué se eligió | Framework “batteries-included” (seguridad, ORM, validación, manejo de excepciones ya resueltos) que reduce el riesgo de un desarrollador único investigando y ensamblando librerías sueltas bajo un cronograma fijo; alta disponibilidad de documentación y comunidad en español, relevante para un desarrollador sin experiencia previa profunda en ninguno de los lenguajes candidatos |
| Alternativas evaluadas | Go – descartado pese a tener ventajas reales de footprint de memoria y simplicidad del lenguaje, porque su ecosistema requiere ensamblar manualmente router, ORM y librerías de autenticación, lo cual consume tiempo de decisión de arquitectura que un proyecto de 6 meses en solitario no puede permitirse. Node.js – descartado como backend principal por preferirse la robustez de tipado y el ecosistema de seguridad de Spring frente a un desarrollador que tampoco tenía experiencia consolidada previa en ninguno de los dos |
| Autenticación | Spring Security + JWT emitido y validado por el propio backend (no se delega la autenticación a Supabase Auth, dado que el modelo de roles de Tinku –adulto responsable, menor con permisos por acción, tutor, administrador– requiere lógica de autorización granular propia que conviene mantener dentro del mismo framework que ya gestiona el resto de las reglas de negocio) |

### Datos

**Tabla:** Capa de datos: decisión tecnológica

| **Ítem** | **Detalle** |
| --- | --- |
| Motor relacional | PostgreSQL, gestionado por Supabase. Postgres es un motor relacional maduro con buen soporte de extensiones (por ejemplo, búsqueda por similitud vectorial vía pgvector, relevante para el motor de matching); Supabase ofrece un plan gratuito suficiente para el MVP y evita la administración manual de backups y actualizaciones del motor de base de datos |
| Detalle de conexión | El backend Spring Boot se conecta a través del pooler de Supabase (Supavisor) en modo sesión (puerto 5432), que se comporta como una conexión directa y es compatible con prepared statements de Hibernate sin configuración adicional. Se documenta como decisión explícita porque el modo transacción (puerto 6543) del mismo pooler no es compatible por defecto con el cacheo de prepared statements que usa Hibernate, y migrar a ese modo en el futuro requeriría desactivar esa característica en el driver JDBC |
| Caché / tiempo real | Redis, gestionado por Upstash (plan gratuito serverless por volumen de uso) – usado para estado de chat en tiempo real y rate limiting, no para el estado interno de las salas de videollamada, que en el MVP delega en LiveKit Cloud |
| Respaldo y migraciones | Backups automáticos de Supabase en su plan gestionado; migraciones de esquema versionadas con Flyway o Liquibase integradas al ciclo de despliegue de Spring Boot |

## Infraestructura y hosting

La tabla~[§tab:infra] resume dónde se aloja cada componente.

**Tabla:** Infraestructura y hosting de cada componente

| **Componente** | **Dónde se aloja** | **Notas** |
| --- | --- | --- |
| Frontend (PWA) | Vercel | Plan gratuito (Hobby) durante el desarrollo; CDN global sin configuración adicional |
| Backend (Spring Boot) | Fase de desarrollo: computadora propia del desarrollador, gestionada con Coolify (PaaS autoalojado) y expuesta a internet mediante Cloudflare Tunnel, sin necesidad de IP pública ni apertura de puertos. Fase de piloto (Sprint 11, capítulo~[§cap:metodologia]): migración a un VPS económico (por ejemplo, Hetzner, 10–25 USD/mes), reutilizando la misma configuración de Coolify | La migración de computadora propia a VPS no requiere reescribir la configuración de despliegue, dado que Coolify orquesta el mismo conjunto de contenedores Docker en ambos casos |
| Base de datos y Redis | Supabase y Upstash respectivamente | Servicios gestionados en la nube, independientes de dónde corra el backend |
| Aula virtual | LiveKit Cloud | Plan gratuito (Build): 5.000 minutos de participante por mes sin necesidad de tarjeta de crédito, equivalente a más de 40 horas de clases de 1 a 1 mensuales – cobertura suficiente para el piloto. Se descartó el auto-hospedaje de LiveKit porque requiere una IP pública alcanzable por UDP para el protocolo WebRTC, algo que ni la computadora de desarrollo ni un VPS económico garantizan sin trabajo adicional de configuración de NAT/TURN |

En cuanto a la escalabilidad: para el rango de tráfico esperado durante el MVP y el piloto (capítulo~[§cap:metodologia]), un único
VPS vertical (backend + base de datos si se optara por auto-alojarla) es suficiente. La estrategia de escalado horizontal
–balanceador de carga con múltiples instancias, o eventualmente
Kubernetes– queda fuera del alcance de esta entrega y se documenta como trabajo futuro, condicionada a que el volumen de uso real lo justifique.

Los costos por componente y por etapa (desarrollo, piloto, eventual escalado) se presentan en el capítulo~[§cap:economica], consistente con el techo de 0–100 USD mensuales declarado en el capítulo~[§cap:metodologia].

## Modelo de datos

El modelo se organiza alrededor de nueve entidades, cuyo detalle completo de atributos se documenta en el diccionario de datos que se incluye como apéndice técnico. **Usuario** es la entidad base y define un rol (ADULTO, MENOR, TUTOR, ADMIN); un usuario con rol ADULTO puede, además de gestionar sus propios datos, tener uno o más perfiles de MENOR
asociados como responsable. **PerfilMenor** está vinculado a un Usuario con rol ADULTO y hereda una sesión propia, pero con permisos restringidos a nivel de endpoint: no puede iniciar pagos, aceptar acuerdos ni reservar con un tutor no autorizado previamente. **PerfilTutor** concentra las credenciales académicas, la documentación de verificación (DNI, certificados), las materias, la disponibilidad y el precio de referencia, mientras que **Certificado** representa cada documento cargado por el tutor –DNI, título, analítico, y opcionalmente el CAP– con un estado de revisión (pendiente, aprobado manual, rechazado, y
‘en_revision_legal‘ exclusivo para el CAP). A nivel de integridad, la ausencia de un certificado de tipo CAP no bloqueará la activación del PerfilTutor ni la generación de una Reserva.

**Reserva** es el bloque horario entre un PerfilMenor/Usuario ADULTO y un PerfilTutor, con estados que recorren ‘pendiente_pago‘,
‘confirmada‘, ‘en_curso‘, ‘finalizada‘,
‘cancelada‘ o ‘no_show‘. **Sesión** es la instancia de videollamada asociada a una Reserva, con referencia a la grabación cuando corresponde y al resumen generado por IA; **Pago** referencia la transacción de MercadoPago asociada a esa Reserva, con su estado de escrow. Por último, **Calificación** es bidireccional y se asocia a una Sesión finalizada, y **Denuncia** se asocia a una Sesión o a un
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

El onboarding de Términos y Condiciones reemplaza el documento de scroll continuo por un paso propio del registro, “Cómo funciona Tinku”, con los puntos clave de los términos –incluido el funcionamiento de la plataforma– presentados como tarjetas: cada una tiene un título corto y grande, un párrafo breve y una ilustración al costado que representa el concepto. Los puntos cubren que Tinku conecta pero no dicta las clases, la verificación de identidad, que las recomendaciones son una ayuda y no una garantía, el pago retenido hasta después de la clase, la protección de los menores, que las clases no se graban salvo el audio del resumen contratado, y la minimización de datos. El tutor ve un conjunto propio, escrito desde su lado: que es independiente y fija su precio, la verificación de su identidad y de su formación contra registros oficiales, la foto obligatoria, cómo y cuándo cobra, los requisitos para dar clases a menores, la grabación del audio solo si habilita el resumen, y cómo se construye su reputación. Los plazos que se citan salen de la Tabla de Tiempos, nunca escritos a mano. Al final, un checkbox de aceptación explícita, desactivado por defecto, habilita el paso siguiente. La foto de perfil del tutor es obligatoria: sin ella no aparece en búsquedas ni recomendaciones, porque alumnos y familias tienen que ver con quién toman clase. La interfaz se diferencia según el rol: la de un PerfilMenor no muestra ni expone controles de las acciones reservadas al adulto –pago, gestión de acuerdos, contacto con tutores no autorizados–, y esa restricción opera tanto en el diseño de interfaz como en los permisos de la API, no solo a nivel visual. El sistema contempla una degradación de la videollamada a chat de texto exclusivamente durante una sesión activa en caso de conectividad deficiente.

En accesibilidad, el MVP no incluye un módulo completo
(capítulo~[§cap:introduccion], sección~[§sec:alcance]), pero aplica buenas prácticas básicas: contraste adecuado, tamaños de fuente legibles y navegación con foco visible. La validación del diseño con usuarios se apoya en las entrevistas y encuestas ya definidas en el capítulo~[§cap:metodologia], y en UAT con el grupo piloto
(OE8).

<!-- Figura: Mockups de pantallas principales -->

## Decisiones incorporadas durante la implementación

Durante la construcción del MVP se tomaron decisiones que precisan o corrigen lo planteado en las secciones anteriores. Cada una quedó registrada como decisión de arquitectura (ADR) en el repositorio del sistema (anexo~[§anx:repositorios]).

**Tabla:** Decisiones incorporadas durante la implementación

| **Tema** | **Decisión y motivo** |
| --- | --- |
| Proveedor de LLM | GPT-4o para el resumen, en lugar de la alternativa Gemini 2.0 Flash; solo recibe el texto ya anonimizado. La transcripción usa gpt-4o-mini-transcribe por costo (ADR-M6-03) |
| Resumen automático | Pasa a ser un adicional pago que se contrata al reservar. Si el resumen no se puede generar, se reembolsa solo el adicional |
| Grabación | Única excepción a no grabar (enmienda de la Constitución del proyecto, v2.4): solo audio, solo con el adicional, nunca con menores, con consentimiento de ambas partes y borrado al transcribir (24 horas como máximo). La graba el navegador del tutor porque la grabación del lado del servidor de LiveKit (Egress) incluye solo 60 minutos gratuitos por mes (ADR-M3-04) |
| Especialidades del tutor | El tutor declara de una a tres especialidades (materia y nivel máximo) además de sus temas; cada una se muestra como *verificada* (respaldada por una credencial aprobada contra un registro oficial) o *declarada*. Los tutores con especialidades solo declaradas aparecen en las búsquedas, marcados como tales (ADR-M1-06) |
| Recomendaciones | Las puntuaciones funcionan como un sistema de recomendación, no como un aval: ordenan los resultados combinando la similitud semántica con lo buscado y las calificaciones de otros usuarios, y un tutor nuevo arranca sin calificaciones. La decisión de con quién aprender es siempre del alumno o de su adulto responsable |
| Verificación de credenciales | Triaje automático que descarta lo inválido y prepara la consulta, más la decisión del rol ADMIN contra el registro oficial; la máquina decide lo que *no* es un título válido, pero lo que sí lo es solo lo prueba el registro (ADR-M1-06) |
| Foto de perfil del tutor | Obligatoria: sin foto el tutor no aparece en búsquedas ni recomendaciones |
| Catálogo de contenidos | El catálogo de temas sigue siendo cerrado y curado (el tutor solo elige temas de ahí), pero es *vivo*: se actualiza de forma continua con lo que se busca y todavía no está. Para eso se cuentan, de forma agregada, los temas buscados sin un tutor que los dé: un contador por tema, sin datos de quién buscó, sin las búsquedas de menores y con un máximo de 500 temas. El rol ADMIN solo ve los temas pedidos varias veces, agrupados por área, y los incorpora al catálogo (ADR-M2-04) |
| Búsqueda sin coincidencia exacta | Si nadie enseña exactamente lo que se buscó, el sistema reconoce el área del tema (materia y nivel del tema del catálogo más parecido) y recomienda tutores de esa área, aclarando que es una recomendación y no una coincidencia exacta (ADR-M2-04) |
| Orden de los resultados | La similitud semántica se calcula contra cada tema del tutor, no contra todos juntos, para que quien enseña muchos temas no quede relegado (ADR-M2-03). La reputación solo desempata entre tutores de relevancia parecida, y los resultados por debajo de un mínimo de relevancia no se muestran (ADR-M2-02) |
| Términos y Condiciones | Paso propio del registro con los puntos clave en tarjetas (título, párrafo breve e ilustración) y aceptación explícita |
| CAP | Obligatorio y vigente solo para dar clases a menores; un tutor que enseña solo a adultos no lo necesita. Al vencer, se cancelan sus clases futuras con menores con reembolso total |
| Versiones | Spring Boot 4.1.1 y Next.js 16.3.6, para mantener parches de seguridad durante el piloto |

Queda abierta una decisión con impacto en el cobro: el reparto automático de la comisión de MercadoPago (*split* de marketplace) exige que cada cobro se genere con las credenciales del propio tutor, obtenidas por OAuth
[mpmarketplace]. Hasta implementarlo, el dinero ingresa a la cuenta de la plataforma y la liquidación al tutor debe resolverse por separado.

## Seguridad, calidad y despliegue

### Seguridad

La autenticación se resuelve con JWT emitido por el propio backend a través de Spring Security, con contraseñas almacenadas mediante hash bcrypt; no se utiliza Supabase Auth, por el motivo ya explicado en la sección~[§sec:stack-backend]. El control de accesos se basa en autorización por rol (ADULTO, MENOR, TUTOR, ADMIN) aplicada a nivel de cada endpoint del backend: el modelo de permisos por acción del rol MENOR
(sección~[§sec:modelo-datos]) se implementa como reglas de autorización explícitas, no como una restricción de interfaz que pudiera sortearse llamando directamente a la API. Toda la comunicación viaja cifrada mediante TLS entre el cliente y el backend y entre el backend y los servicios externos, con el cifrado en reposo de la base de datos delegado a Supabase.

La verificación de tutores combina la carga de DNI y certificados académicos con la extracción automática de la fecha de nacimiento mediante OCR (implementado con Tesseract vía Tess4J, ejecutado in-process en el propio backend para garantizar que las imágenes de los documentos nunca se envíen a servicios de terceros), que rechaza automáticamente el registro de cualquier tutor menor de 18 años. La credencial académica no se da por buena por el archivo –un PDF se falsifica en minutos–, sino por el registro oficial que la respalda: el
Registro Público de Graduados Universitarios para títulos universitarios desde 2012 [rpgu], el Registro Federal de Egreso (ReFE) con el código QR de Mi Argentina para títulos secundarios y superiores digitales desde noviembre de 2023 [refe], el validador de SIU-Guaraní para certificados de alumno regular y los buscadores de cada colegio para las matrículas. Como ninguno de esos registros ofrece una API pública, la verificación combina un triaje automático –rechazo inmediato de lo que claramente no es un título, lectura por OCR del nombre para compararlo con el del DNI, y control de que el enlace de verificación pertenezca a un dominio oficial– con la decisión final del rol ADMIN, que consulta el registro y registra cómo verificó y qué especialidades del tutor cubre esa credencial (sección~[§sec:decisiones-implementacion]).
Incluye además la verificación manual del CAP vigente para quienes dan clases a menores.

El kill-switch de seguridad, presentado como SafeVchat en la sección~[§sec:estado-del-arte] –donde se desarrolla el mecanismo técnico completo, incluida esta misma verificación de edad del tutor vía
OCR y DNI–, se apoya en un clasificador de contenido que corre localmente en el dispositivo (*edge computing*, por ejemplo con
TensorFlow.js) durante la videollamada; ante una detección positiva ejecuta dos acciones diferenciadas: si hay un menor presente, corta la transmisión y suspende preventivamente la cuenta de forma inmediata; si ambos participantes son adultos, el video del detectado se bloquea con un filtro de desenfoque y el sistema solicita confirmación a la contraparte antes de proceder al corte. El portal de denuncias sigue una lógica equivalente: como las clases no se graban, la evidencia es el fragmento de treinta segundos del buffer local del kill-switch, que se sube solo ante un disparo y se conserva hasta la resolución; al registrarse una denuncia, el sistema suspende preventivamente al usuario denunciado y deriva la resolución final a revisión humana del rol ADMIN, con acceso a la evidencia preservada.

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

Todos los cálculos se apoyan en un modelo financiero parametrizado construido en planilla de cálculo, en el cual los indicadores están formulados con las funciones nativas ‘NPV‘ e ‘IRR‘. Esto permite que al modificar cualquier supuesto de entrada —el ticket promedio, la comisión, las horas de desarrollo o el volumen de sesiones— los tres escenarios, el VAN y la TIR se recalculen de forma inmediata. El modelo se incluye como anexo del presente trabajo.

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

El ingreso de Tinku proviene de una única fuente: una
**comisión de plataforma del 27 % sobre el precio de cada sesión**, descontada exclusivamente del pago que recibe el tutor. El ticket promedio de mercado se proyecta en **USD 7 por sesión**. El estudiante abona el precio final fijado por el docente, sin cargos de servicio adicionales visibles. Se excluyen explícitamente vías de ingreso como la publicidad, la venta de datos o las suscripciones premium durante la etapa de MVP.

Durante el diseño del modelo de negocio se evaluaron y descartaron dos metodologías alternativas de intermediación:

- **Suscripción mensual al estudiante (modelo Superprof):** se descartó porque la imposición de una barrera de entrada fija contradice el objetivo principal de reducir la fricción económica para familias de bajo poder adquisitivo.
          Adicionalmente, no genera un ingreso proporcional al valor efectivo entregado en cada sesión.
- **Comisión de alta retención en el extremo superior del mercado (33 %):** se descartó replicar las bandas tarifarias máximas de Preply. Una comisión percibida como excesiva incentiva la desintermediación —acuerdos de pago por fuera de la plataforma tras el primer contacto— lo cual erosiona los ingresos y vulnera el modelo de confianza diseñado.

### Calibración de la comisión

La comisión del 27 % no es un supuesto arbitrario sino el resultado de un análisis de punto de equilibrio. Una primera formulación del modelo adoptó una comisión del 15 %, valor que posiciona a la plataforma por debajo de toda la banda de Preply
(18 % a 33 %). Sin embargo, al incorporar al modelo los costos financieros de la pasarela de pago y proyectar un volumen de demanda realista para un MVP, esa comisión arrojaba un VAN negativo en los tres escenarios: el margen resultante no alcanzaba a cubrir los costos fijos de operación.

La comisión se recalibró entonces al 27 %, valor que continúa dentro de la banda de mercado vigente (18 % a 33 %) y por debajo de su extremo superior, pero que constituye el mínimo necesario para que el escenario base alcance un VAN no negativo dentro del horizonte de cinco años. Se trata de una restricción del modelo que se declara explícitamente: por debajo del 27 %, y manteniendo el resto de los supuestos constantes, el proyecto no se justifica económicamente.

### Unidad de cobro y duración de las sesiones

La plataforma admite sesiones de duración variable, con un mínimo facturable de 30 minutos y una duración estándar de 60 minutos. Esta distinción es económicamente relevante porque los costos variables de procesamiento de IA (transcripción y resumen automatizado) escalan con la duración real del audio procesado, no con la cantidad de sesiones.
Imputar un costo fijo por sesión sobrestimaría el costo de las clases cortas.

Por tal motivo, el modelo calibra el costo de procesamiento por hora de audio y luego lo pondera según la mezcla esperada de duraciones. Asumiendo que un 30 % de las sesiones utiliza el mínimo de 30 minutos, la duración promedio ponderada resulta:

    d = 60 (1 - 0{,}30) + 30 0{,}30 = 51  minutos.

El costo variable de IA por sesión se obtiene entonces como el costo por hora multiplicado por $d/60$, resultando en
USD~0{,0255} por sesión en lugar de los USD~0{,03} que correspondería a una hora completa. El ticket promedio de USD 7, por su parte, se interpreta como el promedio ya ponderado sobre esa misma mezcla de duraciones y precios horarios.

## Estructura de costos

### Inversión inicial

La inversión inicial corresponde a las erogaciones necesarias para llevar el MVP a producción, concentradas en el semestre de desarrollo
(Año 0). Se compone del costo del equipo de desarrollo valorizado a tarifas de mercado según el perfil, los costos administrativos de puesta en marcha y una reserva de contingencia. La tabla~[§tab:inversion] presenta el desglose.

**Tabla:** Inversión inicial desglosada por rol y concepto (en USD)

| **Categoría** | **Concepto** | **Cant.** | **Valor unit.** | **Total** |
| --- | --- | --- | --- | --- |
| Personal | Senior — arquitectura, IA y WebRTC | 192 hs | 50 | 9.600 |
| Personal | Mid — backend y pasarela de pagos | 250 hs | 30 | 7.500 |
| Personal | Junior — frontend PWA e interfaz | 250 hs | 15 | 3.750 |
| Personal | Junior — UAT y pruebas | 120 hs | 15 | 1.800 |
| Infraestructura | Cloud de desarrollo (Supabase, Vercel, LiveKit) | 6 meses | 0 | 0 |
| Administrativo | Registro de dominio | 1 año | 15 | 15 |
| Legal | Asesoría en privacidad de datos y TyC | único | 800 | 800 |
| Riesgo | Contingencia por imprevistos (10 % del desarrollo) | único | 2.265 | 2.265 |
| **Total inversión inicial** | **25.730** |  |  |  |

Las tarifas horarias por perfil (USD 50 para el rol senior, USD 30 para el semi-senior y USD 15 para los roles junior) se adoptan como estimación propia basada en valores de mercado para desarrollo remoto en la región, y se declaran como tal. Las horas asignadas a los perfiles mid y junior se dimensionaron considerando que el uso de servicios gestionados
(Supabase como backend) y de bibliotecas de componentes reduce sustancialmente el trabajo de construcción desde cero.

La reserva de contingencia del 10 % sobre el costo de desarrollo se incorpora para absorber retrabajo, subestimación de horas y corrección tardía de defectos. Su inclusión responde a un criterio conservador: un presupuesto de desarrollo sin margen de imprevistos presenta un riesgo de desvío elevado.

La infraestructura durante el desarrollo se aprovisiona íntegramente sobre las capas gratuitas de los proveedores seleccionados, por lo que no genera erogación en el Año 0. Como referencia del costo alternativo, un VPS de recursos medios de un proveedor local (8 vCore/16~GB) cuesta USD~158,7 mensuales y los planes de entrada arrancan en
USD~7,71 mensuales [lightnode2026]; la arquitectura elegida evita esa erogación durante la etapa de construcción.

### Costos recurrentes post-lanzamiento

Los costos operativos se proyectan mensualmente y se anualizan para el flujo de fondos. La tabla~[§tab:costos-fijos] muestra su evolución a lo largo del horizonte de evaluación.

**Tabla:** Costos fijos mensuales post-lanzamiento (en USD)

| **Categoría** | **Concepto** | **Año 1** | **Año 2** | **Año 3** | **Año 4** | **Año 5** |
| --- | --- | --- | --- | --- | --- | --- |
| Infraestructura | Servidores y base de datos | 45 | 45 | 50 | 55 | 60 |
| Infraestructura | Transmisión de video (LiveKit) | 60 | 60 | 65 | 70 | 75 |
| Infraestructura | Procesamiento LLM (base) | 55 | 55 | 60 | 65 | 70 |
| Administrativo | Honorarios contables | 150 | 150 | 150 | 150 | 150 |
| Administrativo | Renovación de dominio | 1,25 | 1,25 | 1,25 | 1,25 | 1,25 |
| Comercial | Adquisición de usuarios | 40 | 50 | 60 | 70 | 80 |
| **Total mensual** | **351,25** | **361,25** | **386,25** | **411,25** | **436,25** |  |
| **Total anual** | **4.215** | **4.335** | **4.635** | **4.935** | **5.235** |  |

Dos decisiones de este cuadro merecen justificación explícita:

- **Ausencia de equipo de soporte rentado.** El modelo no incorpora personal técnico contratado dentro de los costos fijos durante los cinco años proyectados. Un análisis de sensibilidad sobre esta variable mostró que, con el volumen de sesiones proyectado, sostener un equipo de soporte
          —aun escalonando su incorporación— vuelve el proyecto inviable en los tres escenarios. El mantenimiento correctivo y evolutivo queda a cargo del equipo fundador. La incorporación de soporte pago se difiere hasta que el volumen efectivo de sesiones lo justifique, lo cual constituye una restricción operativa declarada del modelo y no un supuesto de costo cero.
- **Presupuesto de adquisición de usuarios.** Se incorpora una partida de marketing, modesta pero creciente, dado que la proyección de demanda no se sostiene por sí sola: un modelo que proyecta captación de usuarios sin asignar presupuesto de adquisición incurre en una inconsistencia interna.

### Costos variables por transacción

Además de los costos fijos, cada sesión concretada genera costos variables que se deducen del ingreso bruto. La tabla~[§tab:unit-economics] presenta la economía unitaria completa de una sesión promedio.

**Tabla:** Economía unitaria por sesión (en USD)

| **Concepto** | **Cálculo** | **Valor** |
| --- | --- | --- |
| Ticket promedio de la sesión | Precio fijado por el tutor | 7,0000 |
| Comisión bruta de plataforma | Ticket $$ 27 % | 1,8900 |
| Costo variable de IA | Costo/hora $$ ($d/60$) | $-0{,}0255$ |
| Costo de pasarela de pago | Ticket $$ 6,04 % | $-0{,}4228$ |
| **Margen neto por sesión** |  | **1,4417** |

El costo de la pasarela de pago corresponde a la comisión de procesamiento de MercadoPago con dinero disponible de forma inmediata, incrementada por el IVA que grava dicha comisión. Es un costo real de cobranza y resulta conceptualmente distinto de la comisión de plataforma, que constituye el ingreso del proyecto. Su omisión en una formulación preliminar del modelo sobrestimaba el margen neto en aproximadamente un 40 %.

Se reconoce además la existencia de fricción financiera adicional
—retenciones de ingresos brutos, percepciones impositivas y contracargos— cuya magnitud depende de la jurisdicción y del comportamiento efectivo de los usuarios. No se cuantifica en el modelo base y se trata como una sensibilidad adicional sobre el margen, lo cual se declara como una restricción del análisis.

## Beneficios del proyecto

El análisis costo-beneficio contempla tanto los beneficios directamente monetizables como aquellos que, sin traducirse en flujo de caja, inciden sobre la viabilidad del proyecto. La tabla~[§tab:beneficios] los sistematiza.

**Tabla:** Beneficios tangibles e intangibles del proyecto

| **Tipo** | **Beneficio** | **Cuantificación** |
| --- | --- | --- |
| Tangible | Ingreso por comisión sobre sesiones concretadas | USD~1,4417 de margen neto por sesión; es la única fuente de ingreso del flujo |
| Tangible | Ahorro en infraestructura por arquitectura serverless | Evita USD~7,71 a USD~158,7 mensuales de un VPS dedicado [lightnode2026] |
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

La tasa de descuento resume el costo de inmovilizar capital en este proyecto en lugar de destinarlo a su mejor alternativa de riesgo comparable. Incorpora tres componentes: el rendimiento de una colocación alternativa, la cobertura frente a la pérdida de poder adquisitivo y una prima por el riesgo de que los flujos proyectados no se materialicen.

Se adopta una **tasa de descuento del 15 % anual en dólares**.
Dado que la totalidad del modelo está expresada en dólares estadounidenses, la tasa debe interpretarse como una tasa real en esa moneda y no incorpora la inflación en pesos. El valor refleja el costo de oportunidad de un desarrollo tecnológico temprano, sin ingresos históricos ni base de usuarios consolidada, categoría que exige primas de riesgo sensiblemente superiores a las de un activo financiero tradicional.

El factor de descuento aplicado a cada año $t$ es $1/(1+0{,}15)^t$. La sensibilidad de los resultados frente a esta elección se examina en la sección~[§sec:sensibilidad].

## Flujo de fondos proyectado

El flujo de fondos cruza los ingresos derivados del volumen de sesiones contra los costos fijos anuales, imputando la inversión inicial íntegramente en el Año 0. Los ingresos netos de cada año se obtienen multiplicando las sesiones anuales por el margen neto unitario de
USD~1,4417. La tabla~[§tab:flujo-caja] presenta el flujo del escenario base.

**Tabla:** Flujo de fondos proyectado — escenario base (en USD)

| **Concepto** | **Año 0** | **Año 1** | **Año 2** | **Año 3** | **Año 4** | **Año 5** |
| --- | --- | --- | --- | --- | --- | --- |
| Sesiones anuales | 0 | 7.200 | 9.360 | 7.560 | 10.440 | 9.000 |
| Ingreso neto | 0 | 10.380 | 13.494 | 10.899 | 15.051 | 12.975 |
| Costos fijos anuales | 0 | $-4.215$ | $-4.335$ | $-4.635$ | $-4.935$ | $-5.235$ |
| Inversión inicial | $-25.730$ | 0 | 0 | 0 | 0 | 0 |
| **Flujo neto** | **$-25.730$** | **6.165** | **9.159** | **6.264** | **10.116** | **7.740** |
| **Flujo acumulado** | **$-25.730$** | **$-19.565$** | **$-10.405$** | **$-4.141$** | **5.975** | **13.715** |
| **Flujo descontado** | **$-25.730$** | **5.361** | **6.926** | **4.119** | **5.784** | **3.848** |
| **Acum. descontado** | **$-25.730$** | **$-20.369$** | **$-13.443$** | **$-9.324$** | **$-3.540$** | **308** |

La comparación entre las dos últimas filas ilustra el efecto del descuento: mientras el flujo acumulado nominal cambia de signo durante el Año 4, el acumulado descontado recién lo hace sobre el cierre del Año 5. Esa distancia es, precisamente, el precio del tiempo.

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
| Pesimista | $-16.444$ | $-14{,}98$ % | No recupera en 5 años | No recupera en 5 años |
| Base | 308 | 15{,}48 % | 3,41 años | 4,92 años |
| Optimista | 24.143 | 47{,}01 % | 1,88 años | 2,42 años |

La lectura de cada indicador es la siguiente:

- **VAN del escenario base:** USD~308. Es positivo, por lo que el proyecto crea valor por encima de la tasa exigida del 15 % y se acepta. Ahora bien, el margen es mínimo sobre una inversión de USD~25.730: el proyecto apenas cubre su costo de capital, sin excedente relevante.
- **TIR del escenario base:** 15,48 %. Supera a la tasa de corte del 15 % por apenas 0,48 puntos porcentuales.
          Ese diferencial es el margen de seguridad disponible: bastaría que la tasa exigida subiera medio punto para que el proyecto dejara de convenir.
- **Período de repago:** 3,41 años en el escenario base. La inversión nominal se recupera durante el Año 4, dentro del horizonte de evaluación.
- **Repago descontado:** 4,92 años. Medido en dinero de hoy, el recupero se alcanza recién sobre el cierre del Año 5, es decir, en el límite mismo del horizonte proyectado.

En el escenario pesimista los cuatro indicadores son concluyentes: con un
VAN de USD~-16.444 y una TIR negativa, los flujos ni siquiera alcanzan a devolver el capital nominal invertido. El escenario optimista, en cambio, presenta holgura en las cuatro métricas.

## Análisis de sensibilidad

Los resultados de la sección anterior muestran que la viabilidad del proyecto no es robusta: depende críticamente de tres variables. El análisis de sensibilidad realizado sobre el modelo permite identificarlas y cuantificar su incidencia.

- **Volumen de sesiones.** Es la variable de mayor impacto.
          El punto de equilibrio operativo se obtiene dividiendo los costos fijos anuales por el margen neto unitario: en el Año 1
          se requieren $4.215 / 1{,}4417 2.924$ sesiones anuales para cubrir los costos fijos, y en el Año 5 aproximadamente
          3.631. Por debajo de ese umbral la operación genera pérdidas antes de considerar la recuperación de la inversión.
- **Comisión de plataforma.** Manteniendo el resto de los supuestos, una comisión del 26 % arroja un VAN de aproximadamente USD~-1.834 en el escenario base, y una del
          23 % lo lleva a USD~-7.872. El 27 % adoptado es, en consecuencia, el valor mínimo compatible con la aceptación del proyecto.
- **Estructura de costos fijos.** La incorporación de un equipo de soporte rentado —evaluada en una formulación previa del modelo con perfiles junior, mid y senior incorporados de forma escalonada— torna negativo el VAN en los tres escenarios. La operación con equipo fundador no es una preferencia sino una condición de viabilidad en esta etapa.

Cabe señalar que la tasa de descuento afecta al VAN y al repago descontado, pero no a la TIR, que depende exclusivamente del perfil de los flujos.

## Política de reembolsos y su costo real

Todo reembolso al estudiante se ejecuta de manera total a través de la
API de MercadoPago, nunca de forma parcial. Esta política tiene un costo real de cero para Tinku, ya que la pasarela reintegra su propia comisión de procesamiento junto con los fondos, evitando saldos negativos. Además, previene riesgos legales de retención indebida frente a la Ley de Defensa del Consumidor y reduce significativamente la exposición de la plataforma a contracargos.

## Conclusión de la evaluación económica

El proyecto se justifica económicamente, pero bajo condiciones estrictas que corresponde explicitar.

En el escenario base, los cuatro indicadores apuntan en la misma dirección: el VAN es positivo (USD~308), la TIR supera la tasa de corte (15,48 % frente a 15 %) y tanto el repago simple como el descontado se producen dentro del horizonte de cinco años. Conforme al criterio de decisión estándar, el proyecto se acepta. El escenario optimista confirma esa conclusión con holgura.

Sin embargo, los márgenes del escenario base son estrechos y el escenario pesimista resulta claramente no viable. De ello se desprenden tres condiciones de viabilidad:

- **Sostener un volumen mínimo de aproximadamente 3.000
          sesiones anuales**, umbral por debajo del cual la operación no cubre siquiera sus costos fijos.
- **Mantener la comisión en el 27 %**, dado que valores inferiores tornan negativo el VAN con la estructura de costos proyectada.
- **Operar sin equipo de soporte rentado** durante el horizonte evaluado, difiriendo esa incorporación hasta que el volumen efectivo la justifique.

Que el escenario pesimista no resulte viable no invalida el proyecto, sino que delimita con precisión el terreno en que debe moverse. Ante una tracción inferior a la proyectada, las alternativas disponibles no pasan por reducir costos —el margen de recorte ya está agotado— sino por revisar el modelo de negocio: segmentar la oferta por niveles de precio, incorporar modalidades de clase grupal que eleven el ingreso por hora de tutor, o explorar acuerdos institucionales que aporten volumen agregado.
El análisis de riesgos del capítulo siguiente retoma estas contingencias.

# Capítulo 6: Análisis de riesgos

*Desarrollo del capítulo.*

## *Nombre de la sección*

*Texto.*

**Tabla:** Matriz de exposición: probabilidad $$ impacto (escala de la cátedra)

|  | **1 Insignif.** | **2 Menor** | **3 Moderado** | **4 Importante** | **5 Severo** |
| --- | --- | --- | --- | --- | --- |
| **5 Muy probable** | 5 | 10 | 15 | 20 | 25 |
| **4 Probable** | 4 | 8 | 12 | 16 | 20 |
| **3 Posible** | 3 | 6 | 9 | 12 | 15 |
| **2 Poco probable** | 2 | 4 | 6 | 8 | 10 |
| **1 Muy improbable** | 1 | 2 | 3 | 4 | 5 |

**Ejemplo.** [Ejemplo de la cátedra: así no / así sí]
**Así no:** “Puede fallar el servidor.” No hay causa, no hay consecuencia y no se puede hacer nada con esa frase.

**Así sí:** “Debido a que el prototipo corre en una única VM sin réplica, podría caerse durante la demo, lo que impediría mostrar el resultado al jurado.”

Cuatro respuestas posibles: **evitar** (sacar la causa: cambiar el alcance), **mitigar** (bajar probabilidad o impacto: repositorio con backup, ambiente de respaldo), **transferir** (que lo asuma un tercero: hosting administrado, librería probada) y **aceptar**
(convivir con él, documentado, con responsable y contingencia).

| **ID** | **Descripción (causa, evento, efecto)** | **Naturaleza** | **Etapa** | **P** | **I** | **E** | **Respuesta** | **Resp.** | **Contingencia** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-01 | Debido a que los requerimientos se relevan con un solo usuario, podría ocurrir que aparezcan funciones nuevas en cada revisión, lo que provocaría que el alcance no cierre antes de la entrega final. | Alcance | Durante | 4 | 5 | 20 | Mitigar: congelar el alcance del MVP en el hito H4 | Autor | Recortar a los RF de prioridad alta |
| R-02 | Debido a que el prototipo corre en una única VM sin réplica, podría caerse durante la demo, lo que impediría mostrar el resultado al jurado. | Técnico | Pasaje a producción | 3 | 5 | 15 | Mitigar: ambiente de respaldo y video de la demo | Autor | Mostrar el video y el ambiente local |
| R-03 | Debido a que la fuente de datos es una API de terceros sin acuerdo de servicio, podría ocurrir que cambie o se cierre, lo que provocaría la pérdida del insumo del modelo. | Datos / terceros (externo) | Operación | 3 | 5 | 15 | Mitigar: descarga periódica y respaldo local | Autor | Reentrenar con el último respaldo |
| R-04 | Debido a que el hosting se cotiza en dólares y el presupuesto en pesos, podría ocurrir que el costo supere lo previsto, lo que provocaría la suspensión del entorno de producción. | Recursos (externo) | Operación | 3 | 3 | 9 | Transferir: hosting administrado con plan gratuito de respaldo | Autor | Migrar a entorno gratuito degradado |
| R-05 | Debido a que el equipo es de una persona, podría ocurrir una enfermedad o sobrecarga laboral, lo que provocaría atrasos en las entregas. | Recursos | Durante | 2 | 4 | 8 | Aceptar: no hay reemplazo posible; se documenta el avance semanalmente | Autor | Solicitar prórroga a la cátedra con evidencia |
| R-06 | *...* | *...* | *...* | ** | ** | ** | *...* | *...* | *...* |

# Capítulo 7: Presentación de resultados

*Desarrollo del capítulo.*

## *Nombre de la sección*

*Texto.*

**Tabla:** Requerimientos funcionales (ejemplo de estructura)

| **ID** | **Nombre** | **Descripción** | **Prioridad** | **Criterio de aceptación** |
| --- | --- | --- | --- | --- |
| RF-01 | Autenticación | El sistema permite registrarse e iniciar sesión con credenciales propias | Alta | Un usuario nuevo completa el registro y accede en menos de 2 minutos |
| RF-02 | *...* | *...* | *...* | *...* |

**Tabla:** Requerimientos no funcionales (ejemplo de estructura)

| **ID** | **Atributo** | **Descripción** | **Prioridad** | **Umbral medible** |
| --- | --- | --- | --- | --- |
| RNF-01 | Rendimiento | Tiempo de respuesta de las consultas principales | Alta | Latencia p95 menor a 5 s (indicador I-02) |
| RNF-02 | Calidad del modelo | Capacidad predictiva sobre datos no vistos | Alta | $F_1 0{,}70$ (indicador I-01) |
| RNF-03 | *...* | *...* | *...* | *...* |

## *Nombre de la sección*

*Texto.*

<!-- Figura: Captura del sistema en funcionamiento (ejemplo de figura) -->

**Tabla:** Resultados sobre el conjunto de prueba (ejemplo de estructura)

| **Modelo** | **Precisión** | **Exhaustividad** | **$F_1$** | **Tiempo (s)** |
| --- | --- | --- | --- | --- |
| Línea de base | *...* | *...* | *...* | *...* |
| Modelo propuesto | *...* | *...* | *...* | *...* |

**Tabla:** Traducción de la retroalimentación en decisiones de diseño (ejemplo de estructura)

| **Fuente** | **Hallazgo** | **Decisión** | **Estado** |
| --- | --- | --- | --- |
| Encuesta (n=*..*) | *El 60 % no encontró la función X* | *Mover X al menú principal* | Implementado |
| Experto 1 | *...* | *...* | Planificado |

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

*Objetivo de la encuesta y qué se quería validar.*

## Metodología

*Diseño del cuestionario, población, canal de distribución, período de aplicación y cantidad de respuestas.*

## Presentación de la encuesta

*Texto introductorio que vieron las personas participantes
(propósito, anonimato, duración estimada).*

## Cuestionario

- *Pregunta 1 (tipo: opción única).*
- *Pregunta 2 (tipo: escala 1–5).*
- *Pregunta 3 (tipo: abierta).*

# Entrevistas a especialistas

Como se detalla en el capítulo~[§cap:marco-teorico]
(sección~[§sec:entrevistas]), se definieron dos perfiles de especialista complementarios: un docente o gestor/a institucional y un/a profesional del campo psicopedagógico o del vínculo y la seguridad con menores. En cada caso se documenta el contexto, la ficha de la persona entrevistada y la transcripción por ejes temáticos.

**Estado: [PENDIENTE]** – el cronograma del capítulo~[§cap:metodologia] prevé su realización durante el Sprint 3.
Hasta entonces los guiones aquí transcritos constituyen la evidencia del diseño metodológico; los *completar* marcan los datos que se completarán con la realización efectiva de cada entrevista.

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

- **Trazabilidad**: cada entrada indica la herramienta y versión utilizada y la fecha aproximada.
- **Verificación**: toda cifra, cita o referencia sugerida por la herramienta se confirmó en la fuente original antes de incorporarla (regla 3 de la declaración de IA).
- **Autoría**: las salidas se transcriben solo como evidencia; el texto final del documento puede diferir por la revisión y adaptación del autor.

## Asistencia en el marco teórico y estado del arte

> **Instrucción IA:** Resumí los argumentos principales de este paper sobre evaluación de tutores y ranking de compatibilidad en plataformas de tutoría en línea, en tres párrafos en español.
> **Respuesta IA:** (resumen devuelto por la herramienta, verificado contra el texto original)

> **Instrucción IA:** Compará los modelos de negocio, comisiones y esquemas de pago de Superprof, Preply, Wyzant y Tus Clases de manera tabular.
> **Respuesta IA:** (tabla devuelta, contrastada con las tarifas públicas de cada plataforma antes de usarse en [§tab:comparativa)]

## Asistencia en la justificación económica

> **Instrucción IA:** Calculá el VAN a tasa 15 % y la TIR del flujo de caja
[Año 0 ... Año 5] de esta tabla de volúmenes y costos.
> **Respuesta IA:** (cálculos devueltos; se replicaron de forma independiente en hoja de cálculo antes de incluirlos en [§tab:flujo-caja y en la sección de indicadores)]

## Asistencia en redacción y código

> **Instrucción IA:** Reescribí este párrafo en registro académico impersonal sin cambiar su contenido.
> **Respuesta IA:** (texto devuelto por la herramienta, luego editado)

> **Instrucción IA:** Generá el scaffolding de una clase Java de Spring Boot para el endpoint de reserva de una sesión, con validación de permisos por rol.
> **Respuesta IA:** (código devuelto, revisado y adaptado por el autor; las pruebas se escribieron a mano)

# Anexos

# Repositorios de código fuente

*Repositorios.*

## *Nombre del repositorio*

usuario/repositorio

*Descripción: qué contiene, tecnología, cómo ejecutarlo, licencia.*

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

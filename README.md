# Tinku — Proyecto Final de Ingeniería Informática (USAL)

Documento de Proyecto Final de **Santiago Mercado Carbone** (Facultad de
Ingeniería, Universidad del Salvador): *Tinku, una plataforma digital de
marketplace educativo para conectar estudiantes y tutores académicos a
escala nacional*. Sigue la estructura de ocho capítulos de la cátedra, uno
por entrega, sobre el template LaTeX de la cátedra
([Noorman999/usal-proyecto-final-template](https://github.com/Noorman999/usal-proyecto-final-template)).

El sistema que describe está en
[smercadocarbone/usal-tinku](https://github.com/smercadocarbone/usal-tinku).
Ese repositorio es la **fuente de verdad** de las decisiones técnicas (ADR en
`docs/adr/`, Constitución del proyecto, specs por módulo y Tabla de Tiempos):
cuando el texto de la tesis y el sistema difieren, se corrige la tesis y el
cambio se justifica en la sección «Decisiones incorporadas durante la
implementación» del capítulo 4.

## Compilar

Compilador: **pdfLaTeX** (LuaLaTeX también funciona, y es obligatorio con
`pdfa=true`). La bibliografía usa `biber` y el glosario `makeglossaries`;
`latexmk` corre todo solo.

```bash
git clone https://github.com/smercadocarbone/usal-tinku-docs.git
cd usal-tinku-docs
latexmk main.tex
```

**En Overleaf**: subir la carpeta como `.zip` y elegir pdfLaTeX en el menú
(Menu → Compiler). El plan gratuito corta la compilación a los 20 segundos;
la primera vez puede quedarse corta, pero deja archivos en caché: apretar
*Recompile* de nuevo y termina. Las siguientes compilaciones tardan unos
segundos. Si se corta seguido, compilar localmente (TeX Live + VS Code con
LaTeX Workshop) no tiene límite.

## Estructura

| Archivo | Contenido |
|---|---|
| `main.tex` | Datos del trabajo y orden de los capítulos |
| `preliminares/` | Resumen, abstract, agradecimientos, declaración de IA, y las entradas del glosario, siglas y símbolos (se imprimen al final del documento) |
| `capitulos/01` a `08` | Introducción · Metodología y procedimientos · Síntesis de la literatura consultada · Marco tecnológico · Justificación económica · Análisis de riesgos · Presentación de resultados · Implicancias, conclusiones y recomendaciones |
| `refs.bib` | Bibliografía (estilo APA) |
| `apendices/` | A encuesta de validación · B entrevista · C detalles técnicos · D prompts de IA · E defensa del precio (con `superprof-precios.csv`, el relevamiento de 414 avisos) |
| `anexos/` | Repositorios de código |
| `figuras/` | Imágenes del trabajo (el diagrama de arquitectura se edita en `.svg` y se exporta a `.pdf`) |
| `presentacion/` | La presentación de la defensa en PDF (`Tinku-presentacion.pdf`), exportada de la versión web (`/presentacion` del sistema): una página por diapositiva, con el diagnóstico y los riesgos antes y después de dar vuelta las tarjetas |
| `main.pdf` | PDF compilado. **No se regenera solo**: compilar y commitear después de cambiar los `.tex` |
| `tesis.md`, `tesis_a_markdown.py` | Versión Markdown de la tesis para trabajar con asistentes de IA. **Se genera** con `python3 tesis_a_markdown.py`; no editar a mano, y regenerarla después de cambiar los `.tex` |

## Cajas de guía y marcadores

```latex
\begin{guia} ... \end{guia}          % qué evalúa la cátedra
\begin{ejemplo} ... \end{ejemplo}    % ejemplo de estructura
\completar{texto}                    % marcador a reemplazar
```

Para la entrega final se ocultan todas las cajas con:

```latex
\documentclass[guias=false]{usal-proyecto-final}
```

Las cajas `nota`, `advertencia` y `resumenbox` son para el cuerpo del
trabajo y quedan en el documento final.

## Citas, glosario y siglas

```latex
\citep{clave}   % (Autor, año)
\citet{clave}   % Autor (año)
\gls{clave}     % término del glosario o sigla, con enlace
```

Las siglas se expanden completas la primera vez y luego se abrevian. Solo
se imprimen las entradas usadas en el texto.

## Portada

```latex
\coverlogo{template/usal}            % logo superior
\coverwatermark{template/archivo}    % marca de agua (vacío = sin marca)
```

El color principal del documento es `mainColor`, en la sección 3 de
`usal-proyecto-final.cls`.

## PDF/A

Con la opción de clase `pdfa=true` (y LuaLaTeX) el PDF sale en formato
PDF/A-2b. Compila más lento; activarlo solo si lo piden. Se puede validar
en <https://www.pdfforge.org/online/en/validate-pdfa>.

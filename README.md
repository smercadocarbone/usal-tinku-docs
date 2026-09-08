# Template LaTeX — Proyecto Final de Ingeniería Informática (USAL)

Template para el documento de Proyecto Final de la carrera de Ingeniería
Informática de la Universidad del Salvador, cátedra del prof. Esteban
Tissera (ciclo 2026). Sigue la estructura de ocho capítulos de la cátedra,
uno por entrega, y trae en cada capítulo **cajas de guía** con lo que la
cátedra evalúa y **ejemplos de estructura** para tablas, cronogramas y
matrices, calibrados con una tesis que obtuvo la nota máxima.

## Estructura del documento

| Parte | Archivo | Entrega | Peso |
|---|---|---|---|
| Portada, declaración de originalidad | `main.tex`, `preliminares/segunda-pagina.tex` | — | — |
| Agradecimientos | `preliminares/agradecimientos.tex` | — | — |
| Resumen y Abstract | `preliminares/resumen.tex`, `preliminares/abstract.tex` | 0 | 10 % |
| Declaración de uso de IA | `preliminares/declaracion-ia.tex` | — | — |
| Índices, glosario, siglas y símbolos | automático (`preliminares/glosario.tex`, `siglas.tex`, `simbolos.tex`) | — | — |
| Cap. 1 Introducción | `capitulos/01-introduccion.tex` | 1 (9/6) | 5 % |
| Cap. 2 Metodología y procedimientos | `capitulos/02-metodologia.tex` | 2 (5/5) | 5 % |
| Cap. 3 Síntesis de la literatura consultada | `capitulos/03-marco-teorico.tex` | 3 (28/7) | 10 % |
| Cap. 4 Marco tecnológico | `capitulos/04-marco-tecnologico.tex` | 4 (25/8) | 10 % |
| Cap. 5 Justificación económica | `capitulos/05-justificacion-economica.tex` | 5 (15/9) | 15 % |
| Cap. 6 Análisis de riesgos | `capitulos/06-riesgos.tex` | 6 (29/9) | 5 % |
| Cap. 7 Presentación de resultados | `capitulos/07-resultados.tex` | 7 (13/10) | 5 % |
| Cap. 8 Implicancias, conclusiones y recomendaciones | `capitulos/08-conclusiones.tex` | 8 (20/10) | 5 % |
| Bibliografía | `refs.bib` (estilo APA, biblatex + biber) | — | — |
| Apéndices (material propio): encuesta, entrevista, detalles técnicos | `apendices/*.tex` | — | — |
| Anexos (material de terceros): repositorios | `anexos/*.tex` | — | — |
| **Entrega final**: documento + proyecto funcional + presentación | todo | 9 (17/11) | 30 % |

Las fechas son las del calendario 2026 de la cátedra.

## Cómo compilar

**Compilador: LuaLaTeX** (necesario para la fuente por defecto y el PDF/A).
La bibliografía usa `biber` y el glosario usa `makeglossaries`; ambos corren
solos con `latexmk`.

### Overleaf (recomendado)

1. Subir la carpeta completa como `.zip` (Nuevo proyecto → Subir proyecto).
2. Menú → *Compiler* → **LuaLaTeX**. Overleaf lee `.latexmkrc` y ejecuta
   biber y makeglossaries automáticamente.
3. Recompilar. Listo.

### Local (TeX Live 2024 o superior)

```bash
git clone https://github.com/Noorman999/usal-proyecto-final-template.git mi-tesis
cd mi-tesis
latexmk main.tex
```

`latexmk` toma la configuración de `.latexmkrc` (LuaLaTeX, biber,
makeglossaries). Para limpiar los archivos auxiliares: `latexmk -C`.

## Cómo usar el template

### Datos del trabajo

Todo se completa al principio de `main.tex`: título, autor, correo,
autoridades de la portada (decano, director, profesor y, si hay, tutor),
ciclo lectivo y palabras clave. La dedicatoria es opcional.
Los metadatos del PDF/A están en `main.xmpdata`.

### Cajas de guía y marcadores

Dentro de cada capítulo hay tres tipos de caja:

```latex
\begin{guia}      ... \end{guia}       % qué evalúa la cátedra en esa sección
\begin{ejemplo}   ... \end{ejemplo}    % cómo se escribe (ejemplo de estructura)
\begin{pendiente} ... \end{pendiente}  % recordatorio para el autor
\completar{texto}                      % marcador en línea, siempre visible
```

Se escribe **sobre** el template: se reemplazan los `\completar{...}` y se
borran o dejan las cajas de guía. Para la entrega final se ocultan todas de
una vez con la opción de clase:

```latex
\documentclass[guias=false]{usal-proyecto-final}
```

Los `\completar{...}` que queden aparecen en naranja para que no se escape
ninguno.

Las cajas `nota`, `advertencia` y `resumenbox` son para el cuerpo del
trabajo y sí quedan en el documento final.

### Bibliografía

`refs.bib` trae entradas de ejemplo de cada tipo (artículo, actas, libro,
tesis, recurso en línea) con los campos que la cátedra exige. Citas:

```latex
\citep{breiman2001}   % (Breiman, 2001)
\citet{breiman2001}   % Breiman (2001)
```

Toda cita se verifica en la fuente original. Una referencia inventada por
una IA es una falta grave.

### Glosario, siglas y símbolos

Se definen en `preliminares/glosario.tex`, `siglas.tex` y `simbolos.tex` y
se usan con `\gls{clave}`. Solo se imprimen las entradas usadas en el texto.
Las siglas se expanden completas la primera vez y luego se abrevian.

### Figuras, tablas, código y cronograma

* Figuras en `figuras/`. Mientras no existan, `example-image-a` sirve de
  marcador.
* Tablas con `booktabs` y `tabularx` (columnas `L`, `C`, `R` de ancho
  automático). Tablas largas o anchas: `xltabular` dentro de `landscape`
  (ver la matriz de riesgos del capítulo 6).
* Código con `lstlisting` (no requiere Python ni `shell-escape`).
* Cronograma con `pgfgantt` (ver capítulo 2).

### Portada, logos y marca de agua

Desde `main.tex`:

```latex
\coverlogo{template/archivo}        % logo superior (PDF o PNG, sin extensión)
\coverwatermark{template/archivo}   % marca de agua de fondo; vacío = sin marca
```

El diseño de la portada está en la sección 7 de `usal-proyecto-final.cls`
(`\maketitle` y `\makecover`). El color principal del documento es
`mainColor`, al inicio de la sección 3 de la clase.

Para imprimir solo la tapa con letra grande, descomentar el bloque
`\makecover` en `main.tex`.

## PDF/A

La clase genera PDF/A-2b con el paquete `pdfx`. Se puede validar en
<https://www.pdfforge.org/online/en/validate-pdfa>. Transparencias en
figuras o paquetes nuevos pueden romper la conformidad.

## Créditos y licencia

Adaptado por Norman Funes para la cátedra de Proyecto Final (USAL, 2026)
a partir del template *unipd-thesis-modern* v1.3.1 de Francesco Barone
(<https://github.com/baronefr/unipd-thesis-modern>, licencia CC0), que a su
vez adapta la portada del template de Luca Martinelli para la Universidad
de Padua. Se distribuye bajo la misma licencia CC0 (ver `LICENSE`).

#!/usr/bin/env python3
r"""tesis_a_markdown.py — Convierte la tesis (LaTeX) a un único archivo Markdown.

Uso:
    python3 tesis_a_markdown.py [directorio] [-o salida.md] [--no-bib] [--keep-guias]

El script deduce el orden del documento leyendo main.tex (y el template cls),
convierte cada archivo .tex a Markdown legible (quita comandos, expande
\gls/\acr con glosario/siglas, convierte tablas y listas) y al final adjunta
la bibliografía desde refs.bib. Pensado para pasar el contenido a una IA.
"""

import argparse
import os
import re
import sys


# ---------------------------------------------------------------
# utilidades de parseo
# ---------------------------------------------------------------

def find_matching(s, open_idx):
    """Dado un índice que apunta a '{', devuelve la posición del '}' que cierra."""
    depth = 0
    for i in range(open_idx, len(s)):
        c = s[i]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return i
    return len(s) - 1


def take_braced(s, i):
    """Si s[i] == '{', devuelve (contenido, índice_tras_cerrar). Si no, (None, i)."""
    if i < len(s) and s[i] == '{':
        j = find_matching(s, i)
        return s[i + 1:j], j + 1
    return None, i


def take_opt_and_braced(s, i):
    """Toma un argumento opcional [..] y uno obligatorio {..}; devuelve (opcional, obligatorio, i_final)."""
    opt = None
    if i < len(s) and s[i] == '[':
        j = s.find(']', i)
        if j != -1:
            opt, i = s[i + 1:j], j + 1
    arg, i = take_braced(s, i)
    return opt, arg, i


# ---------------------------------------------------------------
# staging 1: limpiar comentarios
# ---------------------------------------------------------------

def strip_comments(text):
    out = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c == '\\' and i + 1 < n:
            out.append(c)
            out.append(text[i + 1])
            i += 2
            continue
        if c == '%':
            # comentario hasta fin de línea
            while i < n and text[i] != '\n':
                i += 1
            continue
        out.append(c)
        i += 1
    return ''.join(out)


# ---------------------------------------------------------------
# staging 2: quitar cajas de guía de la cátedra (no son texto de la tesis)
# ---------------------------------------------------------------

GUIA_BLOCK_RE = re.compile(r'\\begin\{guia\}(\[[^\]]*\])?.*?\\end\{guia\}', re.S)
FIGURE_BLOCK_RE = re.compile(r'\\begin\{figure\*?\}(\[[^\]]*\])?.*?\\end\{figure\*?\}', re.S)


def drop_figures(text):
    def repl(m):
        blk = m.group(0)
        cap = re.search(r'\\caption(?:\[[^\]]*\])?\{([^}]*)\}', blk)
        return '\n\n<!-- Figura: %s -->\n\n' % cap.group(1) if cap else ''

    return FIGURE_BLOCK_RE.sub(repl, text)


def drop_guidance_blocks(text, keep_guias):
    if not keep_guias:
        text = GUIA_BLOCK_RE.sub('', text)
    text = drop_figures(text)
    return text


# ---------------------------------------------------------------
# glosario / siglas -> lookup
# ---------------------------------------------------------------

def load_lookup(root):
    lookup = {}  # key -> texto a insertar
    for fname in ('preliminares/siglas.tex', 'preliminares/glosario.tex',
                  'preliminares/simbolos.tex'):
        path = os.path.join(root, fname)
        if not os.path.exists(path):
            continue
        with open(path, encoding='utf-8') as f:
            content = strip_comments(f.read())
        # \newacronym{key}{SIGLA}{expansión}
        for m in re.finditer(r'\\newacronym\{([^}]*)\}\{([^}]*)\}\{', content):
            lookup[m.group(1)] = m.group(2)
        # \newglossaryentry{key}{name={...}, description={...}, ...}
        for m in re.finditer(r'\\newglossaryentry\{([^}]*)\}\{(.*?)\n\}', content, re.S):
            key, body = m.group(1), m.group(2)
            nm = re.search(r'name\s*=\s*\{', body)
            if nm:
                start = nm.end() - 1
                end = find_matching(body, start)
                name = body[start + 1:end]
                name = re.sub(r'\\ensuremath\{([^}]*)\}', r'\1', name)
                lookup[key] = name
    return lookup


# ---------------------------------------------------------------
# macros propias (custom-symbols.tex)
# ---------------------------------------------------------------

def load_macros(root):
    macros = {}  # comando -> (n_args, cuerpo)
    path = os.path.join(root, 'custom-symbols.tex')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            content = strip_comments(f.read())
        for m in re.finditer(
                r'\\(?:re)?newcommand\{\\([A-Za-z]+)\}(?:\[(\d+)\])?\{', content):
            name, nargs = m.group(1), m.group(2)
            body_start = m.end() - 1
            body_end = find_matching(content, body_start)
            body = content[body_start + 1:body_end]
            macros[name] = (int(nargs) if nargs else 0, body)
    return macros


# ---------------------------------------------------------------
# conversión de texto LaTeX -> markdown
# ---------------------------------------------------------------

def convert_chunk(text, lookup, macros, in_header=False):
    text = convert_math_delims(text)
    text = expand_glossary(text, lookup)
    text = expand_macros(text, macros)
    # instrucciones/respuestas de IA (con número opcional entre corchetes)
    text = re.sub(
        r'\\(instruccionIA|respuestaIA)\*?(?:\[[^\]]*\])?\{([^}]*)\}',
        lambda m: (('> **Instrucción IA:** ' if m.group(1) == 'instruccionIA'
                    else '> **Respuesta IA:** ') + m.group(2)),
        text)
    text = convert_citations(text)
    text = convert_headers(text)
    text = convert_lists(text)
    text = cleanup(text)
    return text


MATH = [(r'\\\(', '$'), (r'\\\)', '$'), (r'\\\[', '$$'), (r'\\\]', '$$')]


def convert_math_delims(text):
    for a, b in MATH:
        text = text.replace(a, b)
    text = re.sub(r'\\ensuremath\{([^}]*)\}', r'$\1$', text)
    return text


GLOSS_RE = re.compile(r'\\(Glspl|Gls|glspl|gls|acrshort|acrlong|acrfull|glslink|glsentryshort|glsentrylong)\*?\{([^}]*)\}(?:\s*\{[^}]*\})?')


def expand_glossary(text, lookup):
    def repl(m):
        cmd, key = m.group(1), m.group(2)
        val = lookup.get(key)
        if val is None:
            return key
        first = cmd[:1].isupper()
        return val[0].upper() + val[1:] if first else val
    return GLOSS_RE.sub(repl, text)


def expand_macros(text, macros):
    # primero los macros propios con sustitución real, con argumentos
    for name, (nargs, body) in macros.items():
        pat = r'\\%s\s*(?:\{[^}]*\}){0,%d}' % (name, max(nargs, 1))
        def mk(args):
            s = body
            for i, a in enumerate(reversed(args), start=nargs):
                s = s.replace('#%d' % i, a)
            return s
        text = re.sub(pat, lambda m: mk(re.findall(r'\{([^}]*)\}', m.group(0))), text)
    # comandos de texto conocidos con braced content
    simple = {
        r'\textbf': '**%s**',
        r'\emph': '*%s*',
        r'\textit': '*%s*',
        r'\textsf': '%s',
        r'\textsc': '%s',
        r'\texttt': '`%s`',
        r'\textsuperscript': '^%s^',
        r'\textsubscript': '~%s~',
        r'\tb': '**%s**',
        r'\completar': '*%s*',
        r'\paragraph': '**%s.** ',
        r'\subparagraph': '_%s._ ',
    }
    for cmd, tmpl in simple.items():
        text = re.sub(re.escape(cmd) + r'\*?\{([^}]*)\}', lambda m: tmpl % m.group(1), text)
    # \sistema{} y otros sin argumento pero definidos -> ya cubiertos arriba con nargs=0
    # comandos sin argumentos: \%, \&, \$, \_, \{, \}, \#, \~, \textbackslash ...
    text = text.replace('\\%', '%')
    text = text.replace('\\&', '&')
    text = text.replace('\\$', '$')
    text = text.replace('\\_', '_')
    text = text.replace('\\{', '{')
    text = text.replace('\\}', '}')
    text = text.replace('\\#', '#')
    text = re.sub(r'\\textbackslash\s*', '\\\\', text)
    text = re.sub(r'\\,\s*', ' ', text)
    text = re.sub(r'\\;\s*', ' ', text)
    text = re.sub(r'\\quad\s*', '   ', text)
    text = re.sub(r'\\qquad\s*', '       ', text)
    text = re.sub(r'\\vspace\*?\{[^}]*\}', '', text)
    text = re.sub(r'\\hspace\*?\{[^}]*\}', '', text)
    text = re.sub(r'\\bigskip|\\medskip|\\smallskip', '', text)
    return text


CITE_RE = re.compile(r'\\(?:citep|citet|cite|parencite|textcite)\*?(?:\[[^\]]*\])?(?:\[[^\]]*\])?\{([^}]*)\}')


def convert_citations(text):
    return CITE_RE.sub(lambda m: '[%s]' % m.group(1).replace(' ', ', '), text)


HEADER_RE = re.compile(r'\\(chapter|section|subsection|subsubsection)\*?(\[[^\]]*\])?\{([^}]*)\}')


def convert_headers(text):
    levels = {'chapter': '#', 'section': '##', 'subsection': '###', 'subsubsection': '####'}
    def repl(m):
        lvl, _, title = m.group(1), m.group(2), m.group(3)
        return '\n\n%s %s\n\n' % (levels[lvl], title.strip())
    return HEADER_RE.sub(repl, text)


ENUM_RE = re.compile(r'\\begin\{(itemize|enumerate|description)\}|\\(?:end)\{(itemize|enumerate|description)\}|\\item\b(?:\[([^\]]*)\])?')


def convert_lists(text):
    stack = []
    out = []
    lines = text.split('\n')
    for line in lines:
        # detectar listas en línea, procesando \begin/\end/\item
        stripped = line.strip()
        depth = len(stack) + 1  # indentación relativa
        if re.search(r'\\begin\{(itemize|enumerate|description)\}', stripped):
            stack.append(re.search(r'\\begin\{(itemize|enumerate|description)\}', stripped).group(1))
            continue
        if re.search(r'\\end\{(itemize|enumerate|description)\}', stripped):
            if stack:
                stack.pop()
            continue
        m = re.match(r'\s*\\item(?:\[([^\]]*)\])?\s+(.*)$', line)
        if m:
            kind = stack[-1] if stack else 'itemize'
            content = m.group(2)
            if m.group(1):
                content = '**%s** — %s' % (m.group(1), content)
            prefix = '  ' * len(stack)
            marker = '1. ' if kind == 'enumerate' else '- '
            out.append('%s%s%s' % (prefix, marker, content))
            continue
        out.append(line)
    text = '\n'.join(out)
    text = re.sub(r'\\begin\{(itemize|enumerate|description)\}', '', text)
    text = re.sub(r'\\end\{(itemize|enumerate|description)\}', '', text)
    return text


SEP = '@@SEP@@'


def cleanup(text):
    # proteger los comentarios HTML de los reemplazos de guiones
    text = text.replace('<!--', '\x01O')
    text = text.replace('-->', '\x01C')
    # referencias cruzadas -> marcador
    text = re.sub(r'\\(?:autoref|eqref|cref|ref|pageref|vref)\*?\{([^}]*)\}', r'[§\1]', text)
    text = re.sub(r'\\label\{[^}]*\}', '', text)
    text = re.sub(r'\\(?:hline|toprule|midrule|bottomrule)', '\n', text)
    text = re.sub(r'\\noindent', '', text)
    text = re.sub(r'\\clearpage|\\newpage|\\pagebreak|\\vfill|\\mbox|\\onehalfspacing|\\small|\\centering|\\raggedright|\\raggedleft|\^\^', '\n\n', text)
    text = re.sub(r'\\frontmatter|\\mainmatter|\\backmatter|\\glsresetall\s*|\\appendix\s*', '\n\n', text)
    text = re.sub(r'\\rule\{[^}]*\}\{[^}]*\}', '\n---\n', text)
    text = text.replace('\\~', ' ')
    # comillas tipográficas
    text = text.replace('---', '—')
    text = text.replace('--', '–')
    text = text.replace('``', '“')
    text = text.replace("''", '”')
    text = text.replace('`', '‘')
    # espacios y saltos
    text = re.sub(r'\\,[ \t]*', ' ', text)
    text = re.sub(r'\\\~{}', '§TILDE§', text)
    text = text.replace('\\ ', ' ')
    # \comando  ->  nada; llaves vacías extra -> nada
    text = text.replace('{}', '')
    # saltos de línea LaTeX (\\ al final de línea) y líneas partidas
    text = re.sub(r'\\\s*\n[ \t]*', '\n', text)
    text = text.replace('\\\\', ' ')
    # cortes de línea innecesarios (unir párrafos continuos)
    text = re.sub(r'([a-záéíóúüñ,;:)\]»]) *(?:\n *)([a-záéíóúüñ])', r'\1 \2', text)
    # saltos de línea dobles razonables
    text = re.sub(r'[ \t]+\n', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.replace('§TILDE§', '~')
    text = text.replace('\x01O', '<!--').replace('\x01C', '-->')
    return text.strip()


# ---------------------------------------------------------------
# tablas -> markdown
# ---------------------------------------------------------------

BRACE = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'
TABLE_ENV_RE = re.compile(
    r'\\begin\{(tabular\*?|tabularx|xltabular|longtable)\}'
    r'(?:\[[^\]]*\])?'
    r'(?:\s*' + BRACE + r'){0,4}'
    r'[ \t]*\n(?P<body>.*?)'
    r'\\end\{\1\}', re.S)
TABLE_WRAP_RE = re.compile(r'\\begin\{table\*?\}(\[[^\]]*\])?.*?\\end\{table\*?\}', re.S)


def rows_of_tablebody(body):
    body = re.sub(r'\\label\{[^}]*\}', '', body)
    body = re.sub(r'\\caption(?:\[[^\]]*\])?\{.*?\}', '', body)
    body = re.sub(r'\\endfirsthead.*?\\endhead', '\n', body, flags=re.S)
    body = re.sub(r'\\(?:endfoot|endlastfoot|endfirsthead|endhead)\s*', '\n', body)
    body = re.sub(r'\\(?:toprule|bottomrule|hline)\s*', '\n', body)
    body = body.replace('\\midrule', '\n\\midrule\n')
    header = []
    body_rows = []
    parts = body.split('\\midrule')
    for idx, part in enumerate(parts):
        cells_rows = []
        for raw_row in part.split('\\\\'):
            raw_row = raw_row.strip()
            if not raw_row:
                continue
            if re.search(r'^\s*\\(?:rowcolor|rowstyle|cmidrule|cline|addlinespace|noalign|sffamily|itshape|bfseries)\b', raw_row):
                continue
            if re.match(r'^\s*\\[A-Za-z]+\s*$', raw_row):
                continue
            cells = split_row_cells(raw_row)
            if not any(c for c in cells):
                continue
            cells_rows.append(cells)
        if idx == 0 and parts[0].strip() and '\\midrule' in body.replace('\\midrule\n', '\\midrule'):
            header = cells_rows
        elif idx == 0 and not header:
            # sin \midrule: primera fila es encabezado
            if cells_rows:
                header = [cells_rows[0]]
                body_rows.extend(cells_rows[1:])
        else:
            body_rows.extend(cells_rows)
    if not header and body_rows:
        header = [body_rows[0]]
        body_rows = body_rows[1:]
    return header, body_rows


def split_row_cells(raw):
    cells, buf = [], []
    depth = 0
    for ch in raw:
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
        if ch == '&' and depth == 0:
            cells.append(''.join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    cells.append(''.join(buf).strip())
    cells = [re.sub(r'\\multicolumn\{\d+\}\{[^}]*\}\{([^}]*)\}', r'\1', c) for c in cells]
    cells = [re.sub(r'\\multirow\*?\{\d+\}\{.*?\}\{([^}]*)\}', r'\1', c) for c in cells]
    return cells


def convert_tables(text, lookup, macros):
    def cell_clean(c):
        c = expand_glossary(c, lookup)
        c = expand_macros(c, macros)
        c = re.sub(r'\\textbf\{([^}]*)\}', r'**\1**', c)
        c = re.sub(r'\\tb\{([^}]*)\}', r'**\1**', c)
        c = re.sub(r'\\emph\{([^}]*)\}|\\textit\{([^}]*)\}', r'*\1\2*', c)
        return c.strip()

    def table_to_md(body, caption):
        header, body_rows = rows_of_tablebody(body)
        rows = [r for r in (header + body_rows) if r]
        if not rows:
            return ''
        maxcols = max(len(r) for r in rows)
        rows = [[cell_clean(c) for c in r] + [''] * (maxcols - len(r)) for r in rows]
        md = [rows[0], [SEP] * maxcols] + rows[1:]
        lines = ['| ' + ' | '.join(r) + ' |' for r in md]
        block = '\n\n' + '\n'.join(lines) + '\n\n'
        if caption:
            block = '\n\n**Tabla:** %s\n%s' % (caption, block)
        return block

    def repl_tab(m):
        return table_to_md(m.group('body'), None)

    def repl_wrap(m):
        block = m.group(0)
        cap = None
        cm = re.search(r'\\caption(?:\[[^\]]*\])?\{([^}]*)\}', block)
        if cm:
            cap = cell_clean(cm.group(1))
        inner = TABLE_ENV_RE.sub(repl_tab, block)
        inner = re.sub(r'\\caption(?:\[[^\]]*\])?\{.*?\}|\\label\{[^}]*\}|\\centering|\\small|\\noindent', '', inner)
        if cap:
            return '\n\n**Tabla:** %s\n%s' % (cap, inner)
        return inner

    text = TABLE_WRAP_RE.sub(repl_wrap, text)
    return TABLE_ENV_RE.sub(repl_tab, text)


# ---------------------------------------------------------------
# entornos sobrantes (definicion, proposicion, teorema, ejemplo...)
# ---------------------------------------------------------------

ENV_LABEL = {'definicion': 'Definición', 'proposicion': 'Proposición',
             'teorema': 'Teorema', 'ejemplo': 'Ejemplo',
             'nota': 'Nota', 'observacion': 'Observación'}


def convert_environments(text):
    # \begin{env} / \end{env} para los entornos con nombre propio
    for env, label in ENV_LABEL.items():
        text = re.sub(r'\\begin\{%s\}\*?' % env, '\n\n**%s.** ' % label, text)
        text = re.sub(r'\\end\{%s\}' % env, '\n\n', text)
    # entornos que desaparecen: abstract/resumen se reetiquetan afuera
    text = re.sub(r'\\begin\{(resumen|abstract|agradecimientos)\}\s*', r'\n\n', text)
    text = re.sub(r'\\end\{(resumen|abstract|agradecimientos)\}\s*', r'\n\n', text)
    # cualquier env restante sin caso especial -> vaciar
    text = re.sub(r'\\begin\{[A-Za-z*]+\}(\[[^\]]*\])?', '\n', text)
    text = re.sub(r'\\end\{[A-Za-z*]+\}', '\n', text)
    return text


# ---------------------------------------------------------------
# comandos sueltos que quedan
# ---------------------------------------------------------------

def strip_leftover_commands(text):
    # \comando{X} -> X  (conservar el contenido)
    text = re.sub(r'\\[A-Za-z]+\*?\{([^}]*)\}', r'\1', text)
    # \comando(*) sin argumento -> nada
    text = re.sub(r'\\[A-Za-z]+\*?\s*', '', text)
    return text


# ---------------------------------------------------------------
# bibliografía desde refs.bib
# ---------------------------------------------------------------

def bib_field_clean(v):
    # \'e, \"e, \`a, \~n, \^^c...  (acentos LaTeX de BibTeX)
    acc = {'a': 'á', 'e': 'é', 'i': 'í', 'o': 'ó', 'u': 'ú',
           'n': 'ñ', 'A': 'Á', 'E': 'É', 'I': 'Í', 'O': 'Ó', 'U': 'Ú'}
    dia = {'a': 'ä', 'e': 'ë', 'i': 'ï', 'o': 'ö', 'u': 'ü',
           'A': 'Ä', 'E': 'Ë', 'O': 'Ö', 'U': 'Ü'}
    v = re.sub(r"\\'([A-Za-z])", lambda m: acc.get(m.group(1), m.group(1)), v)
    v = re.sub(r'\\"([A-Za-z])', lambda m: dia.get(m.group(1), m.group(1)), v)
    v = re.sub(r'\\`([A-Za-z])', lambda m: acc.get(m.group(1), m.group(1)), v)
    v = re.sub(r'\\\^([A-Za-z])', lambda m: m.group(1).replace('a', 'â').replace('o', 'ô'), v)
    v = v.replace('\\&', '&')
    v = re.sub(r'[{}]', '', v)
    v = re.sub(r'\s+', ' ', v).strip()
    return v


def load_bib(root):
    path = os.path.join(root, 'refs.bib')
    if not os.path.exists(path):
        return ''
    with open(path, encoding='utf-8') as f:
        content = strip_comments(f.read())
    entries = []
    for m in re.finditer(r'@(\w+)\{([^,]*),(.*?)\n\}', content, re.S):
        etype, key, body = m.group(1), m.group(2).strip(), m.group(3)
        fields = {}
        # pares campo = {valor}
        for fm in re.finditer(r'^[ \t]*(\w+)\s*=\s*\{(.*)\},?\s*$', body, re.M):
            fields[fm.group(1).lower()] = fm.group(2).strip()
        # pares numéricos o de una línea
        for fm in re.finditer(r'^\s*(year|volume|number|pages)\s*=\s*\{([^}]*)\},?\s*$', body, re.M):
            fields[fm.group(1)] = fm.group(2).strip()
        author = bib_field_clean(fields.get('author', ''))
        title = bib_field_clean(fields.get('title', '') or key)
        year = fields.get('year', 's. f.')
        year = re.sub(r'[^0-9]', '', year) or 's. f.'
        source = bib_field_clean(fields.get('journal') or fields.get('booktitle') or fields.get('what') \
            or fields.get('howpublished') or fields.get('publisher') or '')
        extra = []
        if fields.get('volume'):
            extra.append('vol. %s' % fields['volume'])
        if fields.get('pages'):
            extra.append('pp. %s' % fields['pages'])
        if fields.get('doi'):
            extra.append('DOI: %s' % fields['doi'])
        elif fields.get('url'):
            extra.append(fields['url'])
        entry = '*%s. %s (%s). %s%s*' % (
            author or etype.capitalize(), title, year,
            ('%s. ' % source) if source else '',
            (' '.join(extra)) if extra else '')
        entries.append('* `[%s]` %s' % (key, entry))
    if not entries:
        return ''
    return '\n\n# Bibliografía\n\n%s\n' % '\n'.join(entries)


# ---------------------------------------------------------------
# orden del documento desde main.tex
# ---------------------------------------------------------------

def document_order(root):
    with open(os.path.join(root, 'main.tex'), encoding='utf-8') as f:
        content = f.read()
    cuerpo, apend, anexos = [], [], []
    region = 'cuerpo'
    for line in content.splitlines():
        line = strip_comments(line)
        m = re.search(r'\\includegraphics|\\include\{', line)
        s = re.search(r'\\(?:input|include)\{([^}]*)\}', line)
        if re.search(r'\\begin\{appendices\}', line):
            region = 'apend'
            continue
        if re.search(r'\\end\{appendices\}', line):
            region = 'cuerpo'
            continue
        if re.search(r'\\begin\{anexos\}', line):
            region = 'anex'
            continue
        if re.search(r'\\end\{anexos\}', line):
            region = 'cuerpo'
            continue
        if s:
            fname = s.group(1)
            if fname in ('custom-symbols',) or fname.startswith('preliminares/glosario') \
                    or 'template/' in fname:
                continue
            if fname == 'preliminares/segunda-pagina':
                continue
            if 'preliminares/' in fname:
                (cuerpo if region == 'cuerpo' else {'apend': apend, 'anex': anexos}[region]).append(fname)
            else:
                {'cuerpo': cuerpo, 'apend': apend, 'anex': anexos}[region].append(fname)
    # preliminares que el template incluye solo
    for p in ('preliminares/agradecimientos', 'preliminares/declaracion-ia'):
        if os.path.exists(os.path.join(root, p + '.tex')):
            cuerpo.insert(0, p)
    for p in ('preliminares/abstract', 'preliminares/resumen'):
        if p not in cuerpo and os.path.exists(os.path.join(root, p + '.tex')):
            cuerpo.append(p)
    return cuerpo, apend, anexos


def title_from_main(root):
    with open(os.path.join(root, 'main.tex'), encoding='utf-8') as f:
        content = strip_comments(f.read())
    title = author = kws = ''

    def get(cmd):
        m = re.search(r'\\%s\{(.*?)\}\s*$' % cmd, content, re.M | re.S)
        return m.group(1).strip() if m else ''

    t = get('title')
    if t:
        t = re.sub(r'\\\s*\\\s*(?:\n[ \t]*)?', ' ', t)  # salto de línea LaTeX (\\)
        t = re.sub(r'\\newline|\\break', ' ', t)
        t = re.sub(r'\\\w+(\{[^}]*\})?',
                   lambda m: m.group(1)[1:-1] if m.group(1) else '', t)
        t = re.sub(r'\s+', ' ', t)
        title = t.strip()
    author = get('author')
    a = get('academicYear')
    k = get('palabrasclave')
    if k:
        kws = 'Palabras clave: %s' % k
    return title, author, a, kws


# ---------------------------------------------------------------
# conversión de un archivo .tex
# ---------------------------------------------------------------

def convert_file(path, lookup, macros, keep_guias):
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    text = strip_comments(raw)
    text = drop_guidance_blocks(text, keep_guias)
    text = convert_tables(text, lookup, macros)
    text = convert_environments(text)
    text = convert_chunk(text, lookup, macros)
    text = strip_leftover_commands(text)
    text = cleanup(text)
    text = text.replace(SEP, '---')
    return text.strip()


# ---------------------------------------------------------------
# main
# ---------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description='Convierte la tesis LaTeX a Markdown.')
    ap.add_argument('dir', nargs='?', default='.', help='Directorio raíz de la tesis')
    ap.add_argument('-o', '--output', default='tesis.md', help='Archivo de salida')
    ap.add_argument('--no-bib', action='store_true', help='No adjuntar bibliografía')
    ap.add_argument('--keep-guias', action='store_true',
                    help='Conservar las cajas de guía de la cátedra')
    args = ap.parse_args()

    root = os.path.abspath(args.dir)
    if not os.path.exists(os.path.join(root, 'main.tex')):
        sys.exit('No se encontró main.tex en %s' % root)

    lookup = load_lookup(root)
    macros = load_macros(root)
    cuerpo, apend, anexos = document_order(root)
    title, author, year, kws = title_from_main(root)

    parts = []
    if title:
        parts.append('# %s\n' % title)
        meta = []
        if author:
            meta.append('Autor: %s' % author)
        if year:
            meta.append('Año académico: %s' % year)
        if kws:
            meta.append(kws)
        if meta:
            parts.append('\n'.join('> %s' % x for x in meta))
        parts.append('\n')

    headers = {'preliminares/resumen': '## Resumen (español)',
               'preliminares/abstract': '## Abstract (English)',
               'preliminares/agradecimientos': '## Agradecimientos',
               'preliminares/declaracion-ia': '## Declaración sobre el uso de IA'}

    # el template .cls incluye estos preliminares por su cuenta
    front = ['preliminares/agradecimientos', 'preliminares/declaracion-ia',
             'preliminares/resumen', 'preliminares/abstract']
    order = [f for f in front if os.path.exists(os.path.join(root, f + '.tex'))]
    order += [f for f in cuerpo if f not in front]

    def render(fname):
        path = os.path.join(root, fname + '.tex')
        if not os.path.exists(path):
            return ''
        txt = convert_file(path, lookup, macros, args.keep_guias)
        if not txt:
            return ''
        cm = re.match(r'capitulos/0*(\d+)-', fname)
        if cm:
            txt = re.sub(r'^# ', '# Capítulo %s: ' % str(int(cm.group(1))), txt, count=1)
        if fname in headers:
            return '\n%s\n\n%s\n' % (headers[fname], txt)
        return txt

    for f in order:
        parts.append(render(f))

    if apend:
        parts.append('\n# Apéndices\n')
        for f in apend:
            parts.append(render(f))

    if anexos:
        parts.append('\n# Anexos\n')
        for f in anexos:
            parts.append(render(f))

    if not args.no_bib:
        parts.append(load_bib(root))

    out = '\n\n'.join(x for x in parts if x)
    out = re.sub(r'\n{3,}', '\n\n', out)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(out)
    print('Listo: %s (%d caracteres)' % (args.output, len(out)))


if __name__ == '__main__':
    main()
# Configuración de latexmk: LuaLaTeX + biber + makeglossaries.
# Compilar con:   latexmk main.tex
# Limpiar con:    latexmk -C
# Overleaf lee este archivo automáticamente.

$pdf_mode = 4;            # 4 = lualatex
$lualatex = 'lualatex -interaction=nonstopmode -file-line-error -synctex=1 %O %S';
$bibtex_use = 2;          # usa biber y borra .bbl al limpiar

# glosario, siglas y símbolos (paquete glossaries)
add_cus_dep('glo', 'gls', 0, 'makeglossaries');
add_cus_dep('acn', 'acr', 0, 'makeglossaries');
add_cus_dep('slo', 'sls', 0, 'makeglossaries');
sub makeglossaries {
    my ($base_name, $path) = fileparse($_[0]);
    pushd $path;
    my $return = system("makeglossaries", $base_name);
    popd;
    return $return;
}
push @generated_exts, 'glo', 'gls', 'glg', 'acn', 'acr', 'alg', 'slo', 'sls', 'slg', 'ist', 'xmpi', 'run.xml';

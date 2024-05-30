#Abrir interprete
1. 'swipl'
2. consult('prolog_autocode.pl').
3. example
generate_code(cpp, [assign(x, 10), loop(i, 0, 5, [assign(sum, 'sum + i')]), if_else('x > 0', [assign(y, 'x - 1')], [assign(y, 'x + 1')])], Code).

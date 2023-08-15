exp = input('Insira uma expressão: ')
print('Expressão \033[32mválida') if exp.count('(') == exp.count(')') else print('Expressão \033[31minválida')
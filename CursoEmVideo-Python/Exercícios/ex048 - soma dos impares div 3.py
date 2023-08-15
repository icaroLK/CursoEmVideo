soma = 0
cont = 0
for r in range(1, 501, 2):
    if r % 3 == 0:
        soma += r
#soma = soma + r
        cont += 1
#conta = cont + 1
print('A soma dos \033[32m{}\033[m números solicitados é igual a \033[32m{}\033[m'.format(cont, soma))

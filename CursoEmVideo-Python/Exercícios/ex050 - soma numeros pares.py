soma = 0
qtde = 0
for n in range(1, 7):
    x = int(input('Digite o {}° número: '.format(n)))




    if x % 2 == 0:
        qtde += 1
        soma += x
print('Você inseriu \033[34m{}\033[m números \033[34mPARES\033[m, e a soma entre eles é igual a \033[32m{}\033[m'.format(qtde, soma))

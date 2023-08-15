maior = 0
menor = 0


for ord in range(1, 5+1):
    p = float(input('Insira o peso da {}° pessoa: '.format(ord)))
    if ord == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p

        if p < menor:
            menor = p
print('O maior peso foi {}kg e o menor foi {}kg'.format(maior, menor))

maior = menor = qtd = s = 0
r = 'S'

while r not in 'N':
    n = int(input('\nInsira um número: '))
    r = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    qtd += 1
    if qtd == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        elif menor > n:
            menor = n
    s += n




m = s / qtd
print('\nMédia dos valores: {}\nMaior valor digitado: {}\nMenor valor digitado: {}'.format(m, maior, menor))

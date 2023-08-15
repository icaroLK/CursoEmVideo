m = cont = menor = maior = resp = 0

while resp != 'N':
    n = int(input('Insira um número: '))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[:1]
    m += n
    cont += 1
    if cont == 1:
        maior = menor = n

    if n > maior:
        maior = n

    elif n < menor:
        menor = n
m = m/cont
print('A média entre os {} números digitados é {:.2f}'.format(cont, m))
print('O maior número digitado foi {} e o menor {}'.format(maior, menor))

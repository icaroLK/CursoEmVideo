from random import randint
from time import sleep
numero = []

def sort(a):
    for c in range(a):
        numero.append(randint(rg1, rg2))
    print('Sua lista: ', end='')
    sleep(0.3)
    for c in range(len(numero)):
        print(numero[c], end=' ')
        sleep(0.3)

def somapar(a):
    som = 0
    for c in range(len(a)):
        if a[c] % 2 == 0:
            som += a[c]
    sleep(0.3)
    print('\nA soma dos valores pares da lista é {}'.format(som))



qtd = int(input('Quantidade de números a serem sorteados: '))
print('Escolha um intevalo para sortear os números')
rg1 = int(input('Início: '))
rg2 = int(input('Final: '))

sort(qtd)
somapar(numero)


#sem escolha de valores e intervalo
'''from random import randint
from time import sleep
numero = []

def sort(a):
    for c in range(a):
        numero.append(randint(1, 10))
    print('Sua lista: ', end='')
    sleep(0.3)
    for c in range(len(numero)):
        print(numero[c], end=' ')
        sleep(0.3)

def somapar(a):
    som = 0
    for c in range(len(a)):
        if a[c] % 2 == 0:
            som += a[c]
    sleep(0.3)
    print('\nA soma dos valores pares da lista é {}'.format(som))

sort(5)
somapar(numero)
'''

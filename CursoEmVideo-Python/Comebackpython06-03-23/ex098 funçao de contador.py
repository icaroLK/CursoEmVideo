from time import sleep


def contag(ini, fim, passo):

    print('\033[1m{}\033[m'.format('—')*36)
    print('Contagem de {0} até {1} de {2} em {2}:'.format(ini, fim, passo))
    sleep(0.25)
    if ini < fim:
        for c in range(ini, fim + 1, passo):
            print(c, end=', ')
            sleep(0.25)
    elif ini > fim and passo > 0:
        for c in range(ini, fim + 1, -passo):
            print(c, end=', ')
            sleep(0.25)
    elif ini > fim and passo < 0:
        for c in range(ini, fim + 1, passo):
            print(c, end=', ')
            sleep(0.25)


    print('FIM')
    print('\033[1m{}\033[m'.format('—')*36)
    sleep(0.8)

contag(1, 10, 1)
contag(10, 0, 2)

print('Agora é a sua vez!!!')
a1 = int(input('Início: '))
a2 = int(input('Fim: '))
a3 = int(input('Passo: '))

contag(a1, a2, a3)
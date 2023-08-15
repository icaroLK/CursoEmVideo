from random import randint
deu = ''
qtde = 0



while True:
    resp = str(input('\nVocê quer um número \033[34mpar\033[m ou \033[31mímpar\033[m? ')).strip().upper().replace('Í', 'I')[0]
    x = int(input('Insira um número: '))
    comp = randint(1, 10)
    if (x + comp) % 2 == 0:
        deu = 'P'
    elif (x + comp) % 2 != 0:
        deu = 'I'
    if resp == deu:
        print('\n\033[1;32mVOCÊ GANHOU!!!\033[m')
        print(f'\nVocê escolheu: {x} \nEu escolhi: {comp} \nA soma deu:  {x+comp}')
    if resp != deu:
        print('\n\033[1;31mVOCÊ PERDEU!!!\033[m')
        print(f'\nVocê escolheu: {x} \nEu escolhi: {comp} \nA soma deu:  {x+comp}')
        break
    qtde += 1
    print('\nVamos jogar novamente...')
print(f'\nVocê obteve \033[32m{qtde}\033[m vitórias consecutivas')




#outro jeito

'''from random import randint

comp = randint(1, 10)
deu = ''
qtde = 0

while True:
    resp = str(input('\nVocê quer um número \033[34mpar\033[m ou \033[31mímpar\033[m? ')).strip().upper()[0]
    x = int(input('Insira um número: '))

    if (x + comp) % 2 == 0:
        deu = 'P'
    elif (x + comp) % 2 != 0:
        deu = 'Í'

    if resp == deu:
        print('\n\033[1;32mVOCÊ GANHOU!!!\033[m')
        print(f'\nVocê escolheu: {x} \nEu escolhi: {comp} \nA soma deu:  {x+comp}')

    if resp != deu:
        print('\n\033[1;31mVOCÊ PERDEU!!!\033[m')
        print(f'\nVocê escolheu: {x} \nEu escolhi: {comp} \nA soma deu:  {x+comp}')
        break
    qtde += 1

print(f'\nVocê obteve \033[32m{qtde}\033[m vitórias consecutivas')'''




#jeito cu

'''from random import randint
from time import sleep

comp = randint(1, 10)

while True:
    resp = str(input('Você quer um número \033[34mpar\033[m ou \033[31mímpar\033[m? ')).strip().upper()[0]
    x = int(input('Insira um número: '))

    if resp in 'P':
        if (x+comp) % 2 == 0:
            print('Parabéns você ganhou!!!')
        elif (x+comp) % 2 != 0:
            print('PERDEU!!!')
            break

    if resp in 'ÍI':
        if (x+comp) % 2 == 0:
            print('PERDEU HAHAH!!!')
            break
        elif (x+comp) % 2 !=0:
            print('Boa garoto ganhou')

print(f'Você escolheu {resp} \nEu escolhi {comp} \nA soma deu um número ')'''
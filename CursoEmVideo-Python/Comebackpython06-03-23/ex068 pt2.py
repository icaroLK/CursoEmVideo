from random import randint
from time import sleep
print('\033[1;97m=\033[m'*26)
print("\033[1;97m=\033[m"*6, "\033[1;97mPAR OU ÍMPAR\033[m", "\033[1;97m=\033[m"*6)
print('\033[1;97m=\033[m'*26)

vit = 0
while True:
    pc = randint(1, 10)
    pi = input('\nEscolha: Par ou Ímpar?\nR: ').upper().strip()[0]
    n = int(input('Insira um número entre 1 e 10: '))

    print('\nPar')
    sleep(0.3)
    print('ou')
    sleep(0.3)
    print('Ímpar...')
    sleep(0.3)

    print('\nVocê escolheu {} e eu escolhi {}. A soma deu {}'.format(n, pc, pc+n))
    if pi in 'P':
        if (pc + n) % 2 == 0:
            print('\033[32mGANHOU\033[m')
            vit += 1
        if (pc + n) % 2 != 0:
            print('\033[31mPERDEU\033[m')
            break

    if pi in 'IÍ':
        if (pc + n) % 2 == 0:
            print('\033[31mPERDEU\033[m')
            break
        if (pc + n) % 2 != 0:
            print('\033[32mGANHOU\033[m')
            vit += 1

print('\nVitórias consecutivas: {}'.format(vit))
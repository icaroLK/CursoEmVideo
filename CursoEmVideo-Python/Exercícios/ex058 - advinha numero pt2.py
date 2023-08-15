from random import randint
lk = int(input('Diga um range para o jogo: '))
x = randint(1, lk)
tent = 0
print('\033[1;97m_\033[m'*33)
print('Vou pensar em um número de 1 a {}'.format(lk))
print('\033[1;97m_\033[m'*33)
u = int(input('\nQue número você acha que foi? '))
while u != x:
    if u > x:
        u = int(input('''
\033[31mERROU\033[m
DICA: Um pouco menos...
Digite outro: '''))
    elif u < x:
        u = int(input('''
\033[31mERROU\033[m
DICA: Um pouco mais...
Digite outro: '''))

    tent += 1

if tent == 0:
    print('\n\033[1;33mNA PRIMEIRA TENTATIVA!!!\033[m')
    print('\n\033[32mGANHOU!!!\033[m \nVocê \033[31merrou\033[m \033[1m{}\033[m vezes e'
          ' \033[32macertou\033[m na \033[1m{}°\033[m tentativa'.format(tent, tent + 1))
else:
    print('\n\033[32mGANHOU!!!\033[m \nVocê \033[31merrou\033[m \033[1m{}\033[m vezes e'
          ' \033[32macertou\033[m na \033[1m{}°\033[m tentativa'.format(tent, tent+1))

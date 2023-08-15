from random import randint
x = randint(0,5)
print('-=-'*11)
print('Vou pensar em um número de 0 a 5')
print('-=-'*11)
u = int(input('\nQue número você acha que foi? '))

if u == x:
    print('GANHOU! Eu pensei no número {} e você chutou {}'.format(x, u))
else:
    print('PERDEU! Eu pensei no número {} e você chutou {}'.format(x, u))

from random import randint

def funcao(x):
    y = 0.03 * x + 14
    return y

for c in range(0, 10):
    alt = randint(10, 1000)
    print('R${:.2f} ligando {} minutos por mês'.format(funcao(alt), alt))


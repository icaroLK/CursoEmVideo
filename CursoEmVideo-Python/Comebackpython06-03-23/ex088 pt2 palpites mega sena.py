from random import randint
from time import sleep
ns = []
print('\033[1;97m{}'.format('—')*40)
print('\033[1;97m{:^40}\033[m'.format("JOGO DA MEGA SENA"))
print('\033[1;97m{}\033[m'.format('—')*40)
qtd = int(input('Insira a quantidade de jogos a ser sorteada: '))
tot = 1
jogos = []
while tot <= qtd:
    while True:
        alt = randint(1, 60)
        if alt not in ns:
          ns.append(alt)
        if len(ns) == 6:
            break
    ns.sort()
    jogos.append(ns[:])
    ns.clear()
    tot += 1
print('\033[1;97m{}\033[m'.format('—')*38)
for i, v in enumerate(jogos):
    sleep(0.3)
    print('Jogo {}: {}'.format(i+1, v))
print('\033[1;97m{}\033[m'.format('—')*38)










# meu jeito
'''from random import randint
from time import sleep
ns = []
print('\033[1;97m{}'.format('—')*40)
print('\033[1;97m{:^40}\033[m'.format("JOGO DA MEGA SENA"))
print('\033[1;97m{}\033[m'.format('—')*40)

qtd = int(input('Insira a quantidade de jogos a ser sorteada: '))
while True:
    alt = randint(0, qtd*6)
    if alt not in ns:
      ns.append(alt)
    if len(ns) == qtd*6:
        break

print('\033[1;97m{}\033[m'.format('—')*38)
ini = 0
eta = 6
for c in range(qtd):
    sleep(0.3)
    print(f'Jogo {c+1}:', sorted(ns[ini:eta]))
    ini += 6
    eta += 6
print('\033[1;97m{}\033[m'.format('—')*38)
#print(ns)'''








#old one

'''#funcionando

from random import randint
from time import sleep
ns = []
print('\033[1;97m{}'.format('—')*40)
print('\033[1;97m{:^40}\033[m'.format("JOGO DA MEGA SENA"))
print('\033[1;97m{}\033[m'.format('—')*40)

qtd = int(input('Insira a quantidade de jogos a ser sorteada: '))
while True:
    alt = randint(0, 60)
    if alt not in ns:
      ns.append(alt)
    if len(ns) == 60:
        break

print('\033[1;97m{}\033[m'.format('—')*38)
ini = 0
eta = 7
for c in range(qtd):
    sleep(0.3)
    print(f'Jogo {c+1}:', ns[ini:eta])

    ini += 7
    eta += 7
print('\033[1;97m{}\033[m'.format('—')*38)'''
n = int(input('Insira a quantidade de termos: '))


cont = 1
qtde = n
t1 = 0
t2 = 1

print('{}, {}, '.format(t1, t2), end='')

while cont <= qtde-2:
    t3 = t1 + t2
    print('{}'.format(t3), end='')
    print(', ' if cont < qtde-2 else '', end='')
    cont += 1

    t1 = t2
    t2 = t3

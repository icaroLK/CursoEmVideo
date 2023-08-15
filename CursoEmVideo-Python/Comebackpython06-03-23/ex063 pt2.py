print('Insira a quantidade de termos da sequência de Fibonacci')
n = int(input('R: '))

t1 = 0
t2 = t3 = 1

print('{} -> {}'.format(t1, t2), end='')

while n > 2:
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    n -= 1

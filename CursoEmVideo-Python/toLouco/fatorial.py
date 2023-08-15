n = int(input('Insira um número: '))
f = 1

print('Calculando {}! = '.format(n), end='')
while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    f = f * n
    n -= 1

print('{}'.format(f))

#mais jeitos

'''n = int(input('Insira um número: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1

print('{}'.format(f))'''

#mais um jeito

'''z = int(input('Insira um número: '))
fac = 1

while z != 0:
    fac *= z
    z -= 1
print(fac)'''

#usando for
'''z = int(input('Insira um número: '))
f = 1
for c in range (0, z):
    f = f * z
    z -= 1

print('{}'.format(f))'''
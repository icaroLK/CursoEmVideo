som = x = 0
n = int(input('Insira um número (999 para parar): '))
while n != 999:
    som += n
    x += 1
    n = int(input('Insira um número (999 para parar): '))

print('A soma entre os {} valores digitados é {}'.format(x, som))






#jeito 2
'''n = int(input('Insira um número (999 para parar): '))
c = f = n
x = 1

while c != 999:
    n = int(input('Insira um número (999 para parar): '))
    c = n
    if n != 999:
        f += n
        x += 1

print('A soma entre os {} valores digitados é {}'.format(x, f))'''

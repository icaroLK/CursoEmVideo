from math import sqrt, pow
c1 = float(input('Insira o comprimento do primeiro cateto: '))
c2 = float(input('Insira o comprimento do segundo cateto: '))

h = sqrt((pow(c1, 2) + pow(c2, 2)))

print('A hipotenusa vale {:.2f} cm'.format(h))

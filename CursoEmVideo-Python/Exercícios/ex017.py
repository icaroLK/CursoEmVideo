'''co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))
print('A hipotenusa vale {}'.format((co**2 + ca**2)**(1/2)))'''

'''from math import pow, sqrt
co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))
print('A hipotenusa vale {:.2f}'.format(sqrt((pow(co,2) + pow(ca,2)))))'''

from math import hypot

co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))
print('A hipotenusa vale {:.2f}'.format(hypot(co, ca)))

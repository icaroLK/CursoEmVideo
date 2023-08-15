from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo qualquer: '))
a = radians(ang)
print('O seno do ângulo {0} vale {1:.2f} \nO cosseno do ângulo {0} vale {2:.2f}'.format(ang, sin(a), cos(a)), end=' ')
print('\nA tangente do ângulo {0} vale {1:.2f}'.format(ang, tan(a)))

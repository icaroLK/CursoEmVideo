from math import sin, cos, tan, radians
ang = float(input('Insira um ângulo: '))
f = radians(ang)

print('O ângulo de {}° possui um seno de {:.2f}°, um cosseno de {:.2f}° e uma tangent'
      'e de {:.2f}°'.format(ang, sin(f), cos(f), tan(f)))
#sin, cos, tan ta em radianos, não em graus
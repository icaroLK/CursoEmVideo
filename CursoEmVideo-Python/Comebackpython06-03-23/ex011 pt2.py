alt = float(input('Insira a altura da parede em metros: '))
lar = float(input('Insira a largura da parede em metros: '))
a = alt * lar
# 1 litro de tinta pinta 2m²
l = a/2

print('A parede possui um área de {:.2f}m² e será necessário {:.1f} litros de tinta.'.format(a, l))

h = float(input('Insira a altura da parede: '))
lar = float(input('Insira a largura da parede: '))
print('Sua parede tem uma área de aproximadamente {:.1f}m², e '.format(h*lar), end='')
print('serão necessários {:.1f} litros de tinta para pinta-la'.format((h*lar)/2))

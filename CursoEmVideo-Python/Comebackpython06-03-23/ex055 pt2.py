maior = 0
menor = 0

for c in range(1, 5+1):
    peso = float(input('Insira o peso da {}° pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    if c == 1:
        menor = peso
    if peso < menor:
        menor = peso
print('A baleia mais pesada tem {:.1f}kg'
      '\nO frango mais leve tem {:.1f}kg'.format(maior, menor))
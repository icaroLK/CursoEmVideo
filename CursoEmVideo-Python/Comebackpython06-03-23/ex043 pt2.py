peso = float(input('Insira seu peso (kg): '))
altura = float(input('Insira sua altura (m): '))

IMC = peso / (altura * altura)
print('\nSeu IMC é {:.1f}'.format(IMC))

if IMC < 18.5:
    print('Abaixo do peso')

if 18.5 < IMC < 25:
    print('Peso ideal')

if 25 < IMC < 30:
    print('Sobrepeso')

if 30 < IMC < 40:
    print('Obesidade')

if 40 < IMC:
    print('Obesidade mórbida)


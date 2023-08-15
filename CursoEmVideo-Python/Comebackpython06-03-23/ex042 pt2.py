r1 = float(input('Insira a distância da 1° reta: '))
r2 = float(input('Insira a distância da 2° reta: '))
r3 = float(input('Insira a distância da 3° reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    if r1 == r2 == r3:
        print('Triângulo Equilátero')
    if r1 == r2 or r2 == r3 or r1 == r3:
        print('Triângulo Isóceles')
    if r1 != r2 != r3:
        print('Triângulo Escaleno')



else:
    print('Esse triângulo não pode existir')

ano = int(input('Insira seu ano de nascimento: '))

idade = (2023 - ano)

if idade <= 9:
    print('MIRIM')

elif 9 < idade <= 14:
    print('INFANTIL')

elif 14 < idade <= 19:
    print('JUNIOR')

elif 19 < idade <= 20:
    print('SENIOR')

elif 20 < idade:
    print('MASTER')
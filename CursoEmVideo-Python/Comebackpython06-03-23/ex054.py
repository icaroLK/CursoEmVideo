maior = 0
menor = 0


for c in range(1, 7+1):
    n = int(input('Insira a data de nascimento da {}° pessoa: '.format(c)))
    if 2023 - n >= 18:
        maior += 1
    elif 2023 - n < 18:
        menor += 1

print('Tem {} pessoas maiores de idade\n'
      'Tem {} pessoas menores de idade'.format(maior, menor))

media = 0
velho = 0
maisvel = []
mulher = 0

for c in range(1,4+1):
    print('{} {}° pessoa {}'.format('-'*5, c, '-'*5))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    if c == 1:
        velho = idade
        maisvel = nome

    if sexo == 'M':
        if idade > velho:
            velho = idade
            maisvel = nome

    if sexo == 'F' and idade < 20:
        mulher += 1

    media += idade

print('\nA média de idade do grupo é de {:.2f} anos\n'
      'O homém mais velho tem {} anos e se chama {}\n'
      'Tem {} mulheres com menos de 20 anos'.format(media/4, velho, maisvel, mulher))
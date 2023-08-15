maior18 = hom = bigw = 0
sexo = resp = ' '

while True:
    print('NOVO CADASTRO')
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = input('Sexo: ').strip().title()[0]

    if idade >= 18:
        maior18 += 1
    if sexo in 'M':
        hom += 1
    if sexo in 'F' and idade >= 20:
        bigw += 1

    while resp not in 'sn':
        resp = input('Deseja continuar? [S/N]: ').strip().lower()[0]
    if resp in 'n':
        break

print('Há {} maiores de idade\n'
      'Há {} homens\n'
      'Há {} mulheres com mais de 20 anos'.format(maior18, hom, bigw))

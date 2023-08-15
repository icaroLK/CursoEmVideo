it = 0
idmaisv = 0
qtde = 0
nmaisv = ''


for ord in range(1, 4+1):
    print('{}° pessoa: '.format(ord))
    nome = str(input('\033[34mNome\033[m: '.format(ord))).title().strip()
    idade = int(input('\033[32mIdade\033[m: '.format(ord)))
    sexo = str(input('\033[31mSexo\033[m [M/F] : '.format(ord))).upper().strip()
    print('_'*10)
    it += idade
    if ord == 1 and sexo in 'M':
        idmaisv = idade
        nmaisv = nome
    elif sexo in 'M':
        if idade > idmaisv:
            nmaisv = nome

    if sexo == 'F' and idade < 20:
        qtde += 1



print('''\nA média de idade das pessoas são \033[34m{}\033[m anos.
\033[34m{}\033[m é o homem mais velho com {} anos.
Ao todo existem \033[34m{}\033[m mulheres mais novas do que 20 anos.
'''.format(it/4, nmaisv, idmaisv, qtde))




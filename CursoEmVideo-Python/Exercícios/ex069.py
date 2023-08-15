cont = 1
pss = qtdeM = qtdeF = 0
while True:
    print(f'\n{cont}° pessoa: ')
    nome = str(input('Nome: ')).strip().title()
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().title()[0]
    idade = int(input('Idade: '))
    cont += 1
    if idade >= 18:
        pss += 1
    if sexo in 'M':
        qtdeM += 1
    if sexo in 'F' and idade < 20:
        qtdeF += 1
    dsj = ' '
    while dsj not in 'SN':
        dsj = str(input('Continuar? ')).strip().title()[0]
    if dsj in 'N':
        break

print(f'''\na) tem {pss} pessoas maiores de idade
b) foram cadastrados {qtdeM} homens
c) tem {qtdeF} mulheres menores do que 20 anos''')
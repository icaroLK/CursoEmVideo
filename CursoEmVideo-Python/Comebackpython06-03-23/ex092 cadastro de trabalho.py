dados = {}
dados['Nome'] = input('Nome: ').strip().title()
ano = int(input('Ano de nascimento: '))
dados['Idade'] = 2023 - ano
dados['CTPS'] = int(input('Carteira de trabalho (Caso não tenha, digite "0"): '))
if dados['CTPS'] == 0:
    pass
else:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - 2023)

print('\033[1;97m{}\033[m'.format('—')*23)

for k, v in dados.items():
    if k == 'Salário':
        print('{:<14}R$ {:>6}'.format(k, v))
    else:
        print('{:<15}{:>8}'.format(k, v))

print('\033[1;97m{}\033[m'.format('—')*23)
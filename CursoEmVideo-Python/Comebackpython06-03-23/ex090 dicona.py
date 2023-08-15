dic = {}
dic['Nome'] = input('Insira seu nome: ').title()
n1 = float(input('Nota 1 de {}: '.format(dic['Nome'])))
n2 = float(input('Nota 2 de {}: '.format(dic['Nome'])))
dic['Média'] = (n1+n2)/2
if dic['Média'] >= 7:
    dic['Situação'] = '\033[32mAprovado\033[m'
elif 7 > dic['Média'] >= 5:
    dic['Situação'] = '\033[33mRecuperação\033[m'
else:
    dic['Situação'] = '\033[31mReprovado\033[m'

#print(dic)
print('\033[1m{}\033[m'.format('—')*30)
for k, v in dic.items():
    print('{}: {}'.format(k, v))

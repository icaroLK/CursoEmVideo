tupla = (int(input('Insira um número: ')),
         int(input('Insira um número: ')),
         int(input('Insira um número: ')),
         int(input('Insira um número: ')))



print('O número 9 apareceu {} vezes'.format(tupla.count(9)))
if 3 in tupla:
    print('O número 3 apareceu pela primeira vez na {}° posição'.format(tupla.index(3)+1))
else:
    print('O número 3 não apareceu nenhuma vez :(')
print('Números pares digitados: ', end='')

for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')

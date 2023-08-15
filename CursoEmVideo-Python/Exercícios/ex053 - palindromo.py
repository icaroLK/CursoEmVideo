f = str(input('Insira uma frase: ')).strip().lower().replace(' ','')
qtde = len(f)
inv = ''

for cont in range(qtde-1, -1, -1):
    inv = inv + f[cont]

if inv == f:
    print('\nA frase {} ao contrário fica {} \nTemos um palíndromo'.format(f, inv))

else:
    print('\nA frase {} ao contrário fica {} \n\033[31mNão\033[m é um palíndromo'.format(f, inv))

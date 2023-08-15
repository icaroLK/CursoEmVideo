def area(l, c):
    a = l * c
    print('A área de um terreno {} x {} é de {:.2f}m²'.format(l, c, a))
def title(text):
    print('\033[1;97m{}\033[m'.format('—')*40)
    print('\033[1;97m{:^40}\033[m'.format(text))
    print('\033[1;97m{}\033[m'.format('—')*40)


title('AREA DO TERRENO')

l = float(input('Largura do terreno [m]: '))
c = float(input('Comprimento do terreno [m]: '))
area(l, c)












'''def area(l, c):
    return l * c

def title(text):
    print('\033[1;97m{}\033[m'.format('—')*40)
    print('\033[1;97m{:^40}\033[m'.format(text))
    print('\033[1;97m{}\033[m'.format('—')*40)


title('AREA DO TERRENO')
l = float(input('Largura do terreno [m]: '))
c = float(input('Comprimento do terreno [m]: '))
print('A área de um terreno {} x {} é de {:.2f}m²'.format(l, c, area(l, c)))
'''



print('\033[1;97m{}'.format('—')*40)
print('\033[1;97m{:^40}\033[m'.format("LISTAGEM DE PREÇOS"))
print('\033[1;97m{}\033[m'.format('—')*40)

list = ("Lápis", 1.75,
        "Borracha", 2.00,
        "Caderno", 12.90,
        "Estojo", 25.00,
        "Transferidor", 4.20,
        "Compasso", 9.99,
        "Mochila", 120.99,
        "Canetas", 5.90,
        "Livro", 34.90)

for c in range(0, len(list)):
    if c % 2 == 0:
        print("\033[97m{:.<30}\033[m".format(list[c]), end='')
    else:
        print('R$\033[32m{:>7.2f}\033[m'.format(list[c]))
print('\033[1;97m{}\033[m'.format('—')*40, '\n')
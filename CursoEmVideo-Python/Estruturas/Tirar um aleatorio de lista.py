from random import randint
itens = ('\033[31mPedra\033[m', '\033[1;97mPapel\033[m', '\033[34mTesoura\033[m')
comp = randint(0, 2)
print('O computador escolheu {}'.format(itens[comp]))

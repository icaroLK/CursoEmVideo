def ficha(nome="/desconhecido/", gol=0):
    print('O jogador {} fez {} gol(s)'.format(nome, gol))


n = input('Nome do jogador: ').strip().title()
g = input('Gols: ').strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gol=g)
else:
    ficha(n, g)





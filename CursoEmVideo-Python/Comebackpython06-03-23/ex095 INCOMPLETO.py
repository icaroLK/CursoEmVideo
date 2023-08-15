dados = {}
time = []
while True:
    gols = []
    dados['Nome'] = input('Nome do jogador: ').title()
    dados['Partidas jogadas'] = int(input('Partidas jogadas por {}: '.format(dados['Nome'])))
    for c in range(dados['Partidas jogadas']):
        gols.append(int(input('Quantidade de gols na partida {}: '.format(c+1))))
    dados['Gols'] = gols.copy()
    dados['Total de gols'] = sum(gols)
    time.append(dados.copy())
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja cadastrar mais algúem? [S/N]: ').title().strip()[0]
        if resp in 'SN':
            break
        print('\033[31mERRO\033[m Tente novamente')
    if resp in 'N':
        break
print('\033[1;97m{}\033[m'.format('—')*40)
pos = 0
print('\033[1;97m{:<8}{:<12}{:>8}{:>12}\033[m'.format('Cod', 'Nome', 'Gols', 'Total'))
for dic in time:
    teste = []
    teste = dic['Gols'][:]
    gol = ' '.join(map(str, teste))
    print('{1}{0:<7}{2:<16}{3:<11}{4:>5}'.format(' ', pos, dic['Nome'], gol, dic['Total de gols']))
    pos += 1
print('\033[1;97m{}\033[m'.format('—')*40)



resp = ' '
while resp != 999:
    resp = int(input('Mostrar os dados de qual jogador? [999 para parar]: '))
    print('\nLevantamento do jogador {}'.format(time[resp]['Nome']))
    resp = 0
    pos = 0
    teste = []
    teste = time[resp]['Gols'][:]
    gol = ''.join(map(str, teste))
    for b in time[resp]:
        print('No jogo {} fez {} gols'.format(pos + 1, gol[pos]))
        pos += 1












print('\033[1;97m{}\033[m'.format('—')*35)
for k, v in dados.items():
    if k == 'Gols':
        teste = []
        teste = dados['Gols'][:]
        gol = ' '.join(map(str, teste))
        print('   {:<12}{:>17}'.format(k, gol))
#        print('{:<20}{}'.format(k, dados['Gols']))
#        print('{:<20}'.format(k), end='')
#        for item in dados['Gols']:
#            print(item, end=' ')
#        print()
    else:
       print('   {:<20}{:>9}'.format(k, v))
print('\033[1;97m{}\033[m'.format('—')*35)

print('O jogador {} jogou {} partidas'.format(dados['Nome'], dados['Partidas jogadas']))
for teta in range(dados['Partidas jogadas']):
    print(' - Na partida {} fez {} gols.'.format(teta+1, teste[teta]))

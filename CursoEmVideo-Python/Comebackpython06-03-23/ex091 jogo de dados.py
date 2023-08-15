from random import choice
opc = [1, 2, 3, 4, 5, 6]
rank = []
jogo = {}
print()
for c in range(4): #sorteia
    jogo["Jogador {}".format(c+1)] = choice(opc)


for k, v in jogo.items(): #mostra os valores sorteados
    print('    {} tirou {} no dado'.format(k, v))

#rankeia as parada em ordem certa n etnendi pq atualizou o python
rank = sorted(jogo.items(), key=lambda item: item[1], reverse=True)
#print(rank)
print('\033[1m{}\033[m'.format('—')*33)
for c in range(len(rank)):
    print('{}° lugar: {} com {} pontos'.format(c+1, rank[c][0], rank[c][1]))











# nao terminei oq fiz aqui em baixo
'''from random import choice
opc = [1, 2, 3, 4, 5, 6]
jogs = {}
rank = []
info = []
test = {}
final = []

for c in range(4):
    jogs['Jogador'] = c+1
    jogs['Resultado'] = choice(opc)
    print('Jogador {} tirou {} no dado'.format(jogs['Jogador'], jogs['Resultado']))
    info.append(jogs.copy())

#isso aqui rankeia so os valores do dado
    if c == 0:
        rank.append(jogs['Resultado'])
    else:
        if jogs['Resultado'] >= rank[-1]:
            rank.append(jogs['Resultado'])
        elif jogs['Resultado'] <= rank[0]:
            rank.insert(0, jogs['Resultado'])
        elif rank[0] < jogs['Resultado'] <= rank[1]:
            rank.insert(1, jogs['Resultado'])
        elif rank[1] < jogs['Resultado'] <= rank[2]:
            rank.insert(2, jogs['Resultado'])





print(rank)
print(jogs)
print('INFO:', info)


for c in range(4):
    if c == 0:
        final.append(info[0])

    elif info[c]['Resultado'] > final[-1]['Resultado']:
        final.append(info[c])


print('FINAL: ', final)





print('\033[1m{}\033[m'.format('—')*26)




for c in range(len(info)):
    print('Jogador {} tirou {} no dado'.format(info[c]['Jogador'], info[c]['Resultado']))



'''

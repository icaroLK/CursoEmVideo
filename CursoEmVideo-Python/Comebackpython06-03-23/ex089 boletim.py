temp = []
vez = 1

while True:
    print('\n{}° aluno'.format(vez))
    vez += 1
    nome = input('Nome: ').title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    temp.append([nome, [nota1, nota2], media])
    resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if resp in 'N':
        break


print('\033[1m{}\033[m'.format('—')*41)
print('\033[1;97m{: <6}{:<30}MÉDIA\033[m'.format('Pos.', 'NOME'))
for i, v in enumerate(temp):
    print('{:<6}{:.<30} {}'.format(i+1, v[0], v[2]))
print('\033[1m{}\033[m'.format('—')*41)


while True:
    more = int(input('\nMostrar notas de qual aluno? (para parar digite 999) \nR: '))
    if more == 999:
        break
    if more <= len(temp):
      print('\nNotas de {}\nNota 1: {}\nNota 2: {}'.format(temp[more-1][0], temp[more-1][1][0], temp[more-1][1][1]))
    else:
        print('Dados \033[31mINVÁLIDOS\033[m\nTente novamente')
print('\nCabo :)')















'''#pronto do meu jeito

comp = []
temp = []
vez = 1

while True:
    print('\n{}° aluno'.format(vez))
    vez += 1
    nome = input('Nome: ').title()
    temp.append(nome)
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    comp.append(temp[:])
    temp.clear()


    resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if resp in 'N':
        break




print('\033[1m{}\033[m'.format('—')*41)
print('\033[1;97m{: <6}{:<30}MÉDIA\033[m'.format('Pos.', 'NOME'))
pos = 1
for nome, n1, n2 in comp:
    print('{: <6}{:.<30} {}'.format(pos, nome, (n1+n2)/2))
    pos += 1
print('\033[1m{}\033[m'.format('—')*41)
#print(comp) #testando só





while True:
    more = int(input('\nMostrar notas de qual aluno? (para parar digite 999) \nR: '))
    if more == 999:
        break
#    elif more > len(comp):
#        print('Dados \033[31minválidos.\033[m Tente novamente')
    print('\nNotas de {}\nNota 1: {}\nNota 2: {}'.format(comp[more-1][0], comp[more-1][1], comp[more-1][2]))
print('\nCabo :)')
'''
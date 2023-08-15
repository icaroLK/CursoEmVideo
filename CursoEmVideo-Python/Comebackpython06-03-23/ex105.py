def ficha(nome, *notas, sit=False, tab=False):
    dic = {}
    nut = 0
    for c in range(len(notas)):  #dava pra so ter usado tipo max(notas), min(notas), sum(notas)/len(notas)
        nut += notas[c]
        if c == 0:
            maior = menor = notas[0]
        elif notas[c] >= maior:
            maior = notas[c]
        elif notas[c] < menor:
            menor = notas[c]
    m = round((nut / len(notas)), 1) # media pronta e arredondada para 1 casa decimal
    dic['Nome'] = nome
    dic['Total'] = len(notas)
    dic['Maior'] = maior
    dic['Menor'] = menor
    dic['Média'] = m
    if sit != False:
        if m >= 7:
            sit = '\033[32mAprovado\033[m'
        elif 5 < m < 7:
            sit = '\033[33mRecuperação\033[m'
        elif m < 5:
            sit = '\033[31mReprovado\033[m'
        dic['Situação'] = sit
    else:
        dic['Situação'] = ''

    if tab == False:
        return dic

    if tab != False:
        chaves = list(dic.keys())
        return '\033[1m{0}\033[m\n{1:<13}{2:<8}{3:<7}{4:<7}{5:<8}{6}\n\033[1m{0}\033[m\n{7:<13}{8:<8}{9:<7}{10:<7}{11:<8}{12}'\
            .format('—'*60, chaves[0], chaves[1], chaves[2], chaves[3], chaves[4], chaves[5], dic['Nome'], dic['Total'], dic['Maior'], dic['Menor'], dic['Média'], dic['Situação'] )





resp = ficha('Alexandre', 3.5, 2, 6.5, 2, 7, 10, sit=True, tab=True)
print(resp)






















#1 tentativa que ficou bom ate
'''def ficha(*notas, sit=False):
    dic = {}
    nut = 0
    for c in range(len(notas)):  #dava pra so ter usado tipo max(notas), min(notas), sum(notas)/len(notas)
        nut += notas[c]
        if c == 0:
            maior = menor = notas[0]
        elif notas[c] >= maior:
            maior = notas[c]
        elif notas[c] < menor:
            menor = notas[c]
    m = round((nut / len(notas)), 1) # media pronta e arredondada para 1 casa decimal
    dic['Total'] = len(notas)
    dic['Maior'] = maior
    dic['Menor'] = menor
    dic['Média'] = m
    if sit != False:
        if m >= 7:
            sit = 'Aprovado'
        elif 5 < m < 7:
            sit = 'Recuperação'
        elif m < 5:
            sit = 'Reprovado'
        dic['Situação'] = sit
    return dic


resp = ficha(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
'''

# inclompleto mas n tem nada de errado, so parei de fazer. ia melhorar o que deu certo ali em cima colocando
#pro usuário digitar o nom e as notas e mostrar em tabela ou não mas dai so parei pq tava "fácil" kkkkk
'''def ficha(nome, *notas, sit=False, tab=False):
    dic = {}
    nut = 0
    for c in range(len(notas)):  #dava pra so ter usado tipo max(notas), min(notas), sum(notas)/len(notas)
        nut += notas[c]
        if c == 0:
            maior = menor = notas[0]
        elif notas[c] >= maior:
            maior = notas[c]
        elif notas[c] < menor:
            menor = notas[c]
    m = round((nut / len(notas)), 1) # media pronta e arredondada para 1 casa decimal
    dic['Nome'] = nome
    dic['Total'] = len(notas)
    dic['Maior'] = maior
    dic['Menor'] = menor
    dic['Média'] = m
    if sit != False:
        if m >= 7:
            sit = '\033[32mAprovado\033[m'
        elif 5 < m < 7:
            sit = '\033[33mRecuperação\033[m'
        elif m < 5:
            sit = '\033[31mReprovado\033[m'
        dic['Situação'] = sit
    else:
        dic['Situação'] = ''

    if tab == False:
        return dic

    if tab != False:
        chaves = list(dic.keys())
        return '\033[1m{0}\033[m\n{1:<13}{2:<8}{3:<7}{4:<7}{5:<8}{6}\n\033[1m{0}\033[m\n{7:<13}{8:<8}{9:<7}{10:<7}{11:<8}{12}'\
            .format('—'*60, chaves[0], chaves[1], chaves[2], chaves[3], chaves[4], chaves[5], dic['Nome'], dic['Total'], dic['Maior'], dic['Menor'], dic['Média'], dic['Situação'] )




noxt = []
n2 = ' '
vez = 1
n1 = input('Nome: ').strip().title()
while n2 != 999:
    n2 = float(input('Nota {} (999 para parar): '.format(vez)))
    vez += 1
    noxt.append(n2)
n3 = input('Mostrar a situação? [S/N]: ').strip().title()[0]
if n3 == 'S':
    n3 = True
elif n3 == 'N':
    n3 = False

n4 = input('Mostrar em tabela? [S/N]: ').strip().title()[0]
if n4 == 'S':
    n4 = True
elif n4 == 'N':
    n4 = False

resp = ficha(n1, n2, sit=n3, tab=n4)

#resp = ficha('Alexandre', 3.5, 2, 6.5, 2, 7, 10, sit=True, tab=True)
print(resp)
'''
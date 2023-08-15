print('\033[1;97m_\033[m'*26)
print('     \033[97mTERMOS DE UMA PA\033[m')
print('\033[1;97m_\033[m'*26)

pri = int(input('Insira o primeiro termo: '))
raz = int(input('Insira a razão da PA: '))
cuz = int(input('Insira a quatidade de termos da PA: '))
cont = 1
term = pri
buceta = 0
mais = cuz
qtde = mais

print('\nCalculando uma PA de \033[34m{}\033[m termos, partindo '
      'do \033[34m{}\033[m com uma razão de \033[34m{}\033[m: \n'.format(cuz, pri, raz))

while mais != 0:
    buceta += mais
    while cont <= buceta:
        print('{}'.format(term), end='')
        print(' / ' if cont < buceta else '', end='')
        term += raz
        cont += 1
    mais = int(input('\n\nQuantos termos voce quer ver a mais? '))
    qtde += mais


ult = pri + (qtde - 1) * raz

print('\n\nA soma dos termos dessa PA é \033[34m{}\033[m'.format((pri + ult)*qtde/2))

print('\033[31mFIM\033[m')





#guanabara's

'''print('\033[1;97m_\033[m'*26)
print('     \033[97mTERMOS DE UMA PA\033[m')
print('\033[1;97m_\033[m'*26)

pri = int(input('Insira o primeiro termo: '))
raz = int(input('Insira a razão da PA: '))
cont = 1
term = pri
buceta = 0
mais = 10
qtde = mais

print('\nCalculando uma PA de \033[34m10\033[m termos, partindo '
      'do \033[34m{}\033[m com uma razão de \033[34m{}\033[m: \n'.format( pri, raz))

while mais != 0:
    buceta += mais
    while cont <= buceta:
        print('{}'.format(term), end='')
        print(' / ' if cont < buceta else '', end='')
        term += raz
        cont += 1
    mais = int(input('\n\nQuantos termos voce quer ver a mais? '))
    qtde += mais


ult = pri + (qtde - 1) * raz

print('\n\nA soma dos termos dessa PA é \033[34m{}\033[m'.format((pri + ult)*qtde/2))

print('\033[31mFIM\033[m')'''


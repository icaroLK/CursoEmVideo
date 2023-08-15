print('\033[1;97m_\033[m'*26)
print('     \033[97mTERMOS DE UMA PA\033[m')
print('\033[1;97m_\033[m'*26)

pri = int(input('Insira o primeiro termo: '))
raz = int(input('Insira a razão da PA: '))
qtde = int(input('Insira a quantidade de termos: '))
cont = 1
term = pri
ult = pri + (qtde - 1) * raz

print('\nCalculando uma PA de \033[34m{}\033[m termos, partindo '
      'do \033[34m{}\033[m com uma razão de \033[34m{}\033[m: \n'.format(qtde, pri, raz))


while cont <= qtde:
    print('{}'.format(term), end='')
    print(' / ' if cont < qtde else '', end='')
    term += raz
    cont += 1

print('\n\nA soma dos termos dessa PA é \033[34m{}\033[m'.format((pri + ult)*qtde/2))

print('\n\033[31mFIM\033[m')



#outro jeito

'''print('\033[1;97m_\033[m'*26)
print('     \033[97mTERMOS DE UMA PA\033[m')
print('\033[1;97m_\033[m'*26)

pri = int(input('Insira o primeiro termo: '))
raz = int(input('Insira a razão da PA: '))
qtde = int(input('Insira a quantidade de termos: '))
termo = pri
cont = 1

print('\nCalculando uma PA de \033[34m{}\033[m termos, partindo '
      'do \033[34m{}\033[m com uma razão de \033[34m{}\033[m: \n'.format(qtde, pri, raz))

while cont <= qtde:
    print('{} / '.format(termo), end='')
    #print(' / ' if pri + raz < ult else ' = ', end='')
    termo += raz
    cont += 1
print('\033[31mfim\033[m')'''
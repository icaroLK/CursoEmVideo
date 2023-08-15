'''for c in range(1, 10+1):
    print(c, end='/')'''


'''c = 1
while c < 10+1:
    print(c, end='/')
    c = c + 1'''

'''resp = str(input('Inserir código? [S/N]\n')).strip().title()
if resp in 'Sim':
    n = int(input('Senha: '))
    while n != 6969:
        n = int(input('Senha: '))
    if n == 6969:
        print('Parabéns, você descobriu o segredo.')

else:
    print('*Você segue em frente*')'''

tot = par = impar = 0
x = 1
while x != 0:
    x = int(input('Digite um número: '))
    tot += 1
    if x != 0:
        if x % 2 == 0:
            par += 1
        if x % 2 != 0:
            impar += 1
print('''
Você \033[31merrou\033[m {} vezes e \033[32macertou\033[m na {}° vez
\nTentativas com números \033[34mpares\033[m: {}
Tentarivas com números \033[31mímpares\033[m: {}'''.format(tot-1, tot, par, impar))

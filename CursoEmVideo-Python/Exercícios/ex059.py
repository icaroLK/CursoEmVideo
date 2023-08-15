from time import sleep
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
r = 0

print('\033[1;97m_\033[m'*22)
print('''[1] = somar
[2] = multiplicar
[3] = maior valor
[4] = novos números
[5] = sair do programa''')
print('\033[1;97m_\033[m'*22)
esc = int(input('Digite: '))

while esc != 5:

    if esc == 1:
        r = n1 + n2

    if esc == 2:
        r = n1 * n2
    if esc == 3:
        if n1 > n2:
            r = n1
        elif n2 > n1:
            r = n2
    if esc == 4:
        n1 = int(input('Insira um número: '))
        n2 = int(input('Insira outro número: '))
    else:
        print('\033[31mERROO\nopção inválida \nTente novamente.\033[m')

    print('\n\033[1;97mVALOR ATUAL = {}\033[m\n'.format(r))

    print('\033[1;97m_\033[m' * 22)
    print('''[1] = somar
[2] = multiplicar
[3] = maior valor
[4] = novos números
[5] = sair do programa''')
    print('\033[1;97m_\033[m' * 22)
    esc = int(input('Digite: '))


print('\nFinalizando o programa...')
sleep(0.7)
print('Obrigado, volte sempre :)')

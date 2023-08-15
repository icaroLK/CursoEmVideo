n1 = int(input('Insira um número: '))
n2 = int(input('Insira um número: '))
resp = []
while resp != '5':
    print('Escolha uma opção:\n'
                  '[1] Somar\n'
                  '[2] Multiplicar\n'
                  '[3] Maior\n'
                  '[4] Novos números\n'
                  '[5] Sair do programa\n')
    resp = str(input('R: '))
    if resp == '1':
        soma = n1 + n2
        print('A soma de {} com {} é igual a {}'.format(n1, n2, soma))
    elif resp == '2':
        mult = n1 * n2
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, mult))
    elif resp == '3':
        if n1 > n2:
            maior = n1
            print('O maior valor entre {} e {} é {}'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('O maior valor entre {} e {} é {}'.format(n1, n2, maior))
        elif n1 == n2:
            print('Não existe maior valor. Os dois números digitados são iguais.')
    elif resp == '4':
        n1 = int(input('Insira um novo número: '))
        n2 = int(input('Insira um novo número: '))
    elif resp == '5':
        break
    else:
        print('Dados inválidos. Tente novamente')

print('Obrigado, volte sempre!!')

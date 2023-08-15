resp = str(input('Inserir código? [S/N]\n')).strip().title()
if resp in 'Sim':
    n = int(input('Senha: '))
    while n != 6969:
        n = int(input('Senha: '))
    if n == 6969:
        print('Parabéns, você descobriu o segredo.')

else:
    print('*Você segue em frente*')
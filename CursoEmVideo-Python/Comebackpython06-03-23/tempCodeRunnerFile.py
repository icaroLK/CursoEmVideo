def titulo(msg):
    print('\033[1;37m—\033[m'*50)
    print('\033[37m{:^50}\033[m'.format(msg))
    print('\033[1;37m—\033[m'*50)


titulo('MENU PRINCIPAL')
print('\033[33m1\033[m — \033[34mVer pessoas cadastradas\033[m\n'
      '\033[33m2\033[m — \033[34mCadastrar uma nova pessoa\033[m\n'
      '\033[33m3\033[m — \033[34mSair do programa\033[m')
print('\033[1;37m—\033[m'*50)


while True:
    op = input('Sua opção: ').strip()
    if op in '1' or op in '2' or op in '3':
        break
    else:
        print('\033[31mERRO. Por favor, digite um número inteiro válido.\033[m')


if op in '1' or op in '2':
    titulo('Opção {}'.format(op))
else:
    titulo('Saindo do sistema... Até logo!')

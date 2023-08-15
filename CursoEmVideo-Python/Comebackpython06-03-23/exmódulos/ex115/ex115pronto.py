from lib.interface import interfacee
from lib.arquivo import arquivadas
from time import sleep


arq = 'cursoemvideo.txt'
encont = 'C:\Time Travel Stuff\CursoEmVideoPython\Comebackpython06-03-23\exmódulos\ex115\{}'.format(arq)


if arquivadas.arqExiste(encont) == True:
    pass #se deixar o print aqui em baixo, pode tirar esse 'pass'
#    print('Arquivo encontrado :)')
else:
#    print('Arquivo não encontrado :(')
    arquivadas.criararq(encont)


while True:
    respo = interfacee.menu('MENU PRINCIPAL', ['Ver pessoas cadastradas', 'Cadastrar uma pessoa', 'Sair do sistema'])
    if respo == 1:
        interfacee.titulo('Opção 1')
        #opçaõ de listar conteudo de um arquivo
        arquivadas.lerarq(encont)

    elif respo == 2:
        interfacee.titulo('Opção 2')
        interfacee.titulo('NOVO CADASTRO')
        nome = input('Nome: ').title().strip()
        idade = interfacee.leiaint(input('Idade: '))
        arquivadas.addarq(encont, nome, idade)

    elif respo == 3:
        interfacee.titulo('Saindo do sistema... Até logo.')
        break

    else:
        print('\033[31mERRO!!! Digite uma opção válida.\033[m')
    sleep(1)

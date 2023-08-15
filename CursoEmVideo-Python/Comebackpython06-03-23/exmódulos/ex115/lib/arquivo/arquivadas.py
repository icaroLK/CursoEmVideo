from lib.interface import interfacee


def arqExiste(nome):
    try:
        with open(nome, 'rt') as arquivo:
            return True
    except FileNotFoundError:
        return False


def criararq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print("Arquivo criado com \033[32msucesso\033[m")
    


def lerarq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!!!')
    else:
        interfacee.titulo('PESSOAS CADASTRADAS')
        print(a.read())
        print()
    finally:
        a.close()


def addarq(areq, n='Desconhecido', i=0):
    try:
        with open(areq, 'at') as oie:
            oie.write('\n{:<30}{:>15} anos'.format(n, i))
    except:
        print('Ocorreu um erro ao fazer o cadastro!!!')
    else:
        print('Cadastro de {} realizado com sucesso'.format(n))
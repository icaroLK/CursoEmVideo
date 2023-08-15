def leiaint(a):
    try:
        return int(a)

    except ValueError:
        a = leiaint(input(
            '\033[31mDados inválidos!!! Insira um número válido\033[m\nInsira um número inteiro: '))
        return int(a)


def linha(tam=50):
    return '\033[1;37m—\033[m'*50


def titulo(msg):
    print(linha())
    print('\033[37m{:^50}\033[m'.format(msg))
    print(linha())


def menu(tit, lista):
    titulo(tit)
    c = 1
    for opa in lista:
        print('\033[33m{}\033[m — \033[34m{}\033[m'.format(c, opa))
        c += 1
    print(linha())
    opc = leiaint(input('Sua opção: '))
    return opc
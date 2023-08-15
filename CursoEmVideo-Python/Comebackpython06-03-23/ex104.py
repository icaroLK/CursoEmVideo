def leiaint(n):
    if n.isnumeric():
        return int(n)
    else:
        n = leiaint(input('\033[31mDados inválidos!!!\033[m Insira um número inteiro válido\nInsira um número inteiro: '))
        return int(n)


n = leiaint(input('Insira um número inteiro: '))
print('Você digitou o número {}'.format(n))

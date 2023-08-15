def leiaint(a):
    try:
        return int(a)

    except ValueError:
        a = leiaint(input(
            '\033[31mDados inválidos!!!\033[m Insira um número inteiro válido\nInsira um número inteiro: '))
        return int(a)


def leiafloat(a):
    a = a.replace(',', '.')
    if a.replace('.', '').isnumeric():
        a = a.replace(',', '.')
        return float(a)
    else:
        a = leiafloat(input(
            '\033[31mDados inválidos!!!\033[m Insira um número real válido\nInsira um número real: '))
        return a


n = leiaint(input('Insira um número inteiro: '))
r = leiafloat(input('Insira um número real: '))

print('Número inteiro digitado: {}\n'
      'Número real digitado: {}'.format(n, r))

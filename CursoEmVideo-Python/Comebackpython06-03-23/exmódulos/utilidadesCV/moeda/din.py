def aument(a, t, p=False):
    r = (a * t / 100) + a
    if p != False:
        fort = '\033[32mR${:.2f}\033[m'.format(r)
        return fort
    return r


def reduz(a, t, p=False):
    r = a - (a * t / 100)
    if p != False:
        fort = '\033[32mR${:.2f}\033[m'.format(r)
        return fort
    return r


def dobro(a, p=False):
    r = a * 2
    if p != False:
        fort = '\033[32mR${:.2f}\033[m'.format(r)
        return fort
    return r


def metade(a, p=False):
    r = a/2
    if p != False:
        fort = '\033[32mR${:.2f}\033[m'.format(r)
        return fort
    return r


def moeda(a):
    return '\033[32mR${:.2f}\033[m'.format(a)


def resumo(a, b, c):
    print('\033[1;37m{}'.format('—'*32))
    print('{:^32}'.format('RESUMO DO VALOR'))
    print('—'*32, '\033[m')
    print('{:<21}\033[32mR$ {:>8.2f}\033[m'.format('Preço analisado:', a))
    print('{:<21}\033[32mR$ {:>8.2f}\033[m'.format('Dobro do preço:', dobro(a)))
    print('{:<21}\033[32mR$ {:>8.2f}\033[m'.format('Metade do preço:', metade(a)))
    print('{:02d}% {:<17}\033[32mR$ {:>8.2f}\033[m'.format(b, 'de aumento:', aument(a, b)))
    print('{:02d}% {:<17}\033[32mR$ {:>8.2f}\033[m'.format(c, 'de desconto:', reduz(a, c)))
    print('—'*32, '\033[m')
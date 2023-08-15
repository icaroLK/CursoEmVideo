from utilidadesCV.moeda import din


p = float(input('\033[mInsira o preço: \033[32mR$'))
print('\033[mA metade de {} é {}'.format(din.moeda(p), din.metade(p, p=True)))
print('O dobro de {} é {}'.format(din.moeda(p), din.dobro(p, p=True)))
print('Aumentando 10%, temos {}'.format(din.aument(p, 10, p=True)))
print('Reduzindo 15%, temos {}'.format(din.reduz(p, 15, p=True)))

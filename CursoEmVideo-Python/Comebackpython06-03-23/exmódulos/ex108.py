from utilidadesCV.moeda import din


p = float(input('\033[mInsira o preço: \033[32mR$'))
print('\033[mA metade de {} é {}'.format(din.moeda(p), din.moeda(din.metade(p))))
print('O dobro de {} é {}'.format(din.moeda(p), din.moeda(din.dobro(p))))
print('Aumentando 10%, temos {}'.format(din.moeda(din.aument(p, 10))))
print('Reduzindo 15%, temos {}'.format(din.moeda(din.reduz(p, 15))))

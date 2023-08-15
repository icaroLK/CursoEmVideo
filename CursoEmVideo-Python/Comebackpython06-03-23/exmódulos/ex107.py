from utilidadesCV.moeda import din


p = float(input('\033[mInsira o preço: \033[32mR$'))
print('\033[mA metade de R${:.2f} é \033[32mR${:.2f}\033[m'.format(p, din.metade(p)))
print('O dobro de R${:.2f} é \033[32mR${:.2f}\033[m'.format(p, din.dobro(p)))
print('Aumentando 10%, temos \033[32mR${:.2f}\033[m'.format(din.aument(p, 10)))
print('Reduzindo 15%, temos \033[32mR${:.2f}\033[m'.format(din.reduz(p, 15)))

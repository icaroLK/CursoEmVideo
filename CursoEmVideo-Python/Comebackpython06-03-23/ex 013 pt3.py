atual = float(input('Insira seu salário: R$'))
novo = atual + (atual *15/100)

print('O salário de R${:.2f} com 15% de aumento passa a valer R${:.2f}'.format(atual, novo))

p = float(input('Insira o valor do produto: R$'))
d = int(input('Insira o desconto: '))
f = p - (p * d/100)
print('O produto que custa R${:.2f} com {}% de desconto passa a custar R${:.2f}'.format(p, d, f))

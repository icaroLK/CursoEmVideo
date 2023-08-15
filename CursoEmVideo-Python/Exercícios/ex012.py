pt = float(input('Digite o preço do produto: R$'))
desc = int(input('Digite o desconto a ser aplicado: '))
print('O produto que custa R${} ficaria R${} com {}% de desconto'.format(pt, pt - (pt*desc/100), desc))

v = int(input('Qual a distância da viagem em km? '))
if v <= 200:
    print('O preço da sua passagem será de R${:.2f}'.format(v*0.5))
else:
    print('O preço da sua passagem será de R${:.2f}'.format(v*0.45))

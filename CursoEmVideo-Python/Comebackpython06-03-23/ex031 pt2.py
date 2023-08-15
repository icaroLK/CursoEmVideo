'''dist = int(input('Insira a distância da viagem em KM: '))
if dist <= 200:
    p = 0.5*dist
    print('O preço da sua passagem será R${:.2f}'.format(p))
else:
    p = 0.45 * dist
    print('O preço da sua passagem será R${:.2f}'.format(p))'''


dist = int(input('Insira a distância da viagem em KM: '))
p = dist * 0.5 if dist <=200 else dist * 0.45
print('O preço da sua passagem será R${:.2f}'.format(p))
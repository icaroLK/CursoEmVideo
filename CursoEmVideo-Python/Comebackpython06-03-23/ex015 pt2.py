dia = int(input('Insira a quantidade de dias alugados: '))
km = int(input('Insira a quantidade de KM percorridos: '))

p = (60 * dia) + (0.15 * km)

print('O preço do aluguel será de R${:.2f}'.format(p))

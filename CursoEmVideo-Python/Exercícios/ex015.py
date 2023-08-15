km = float(input('Insira quantos km você andou com o carro alugado: '))
d = int(input('Por quantos dias você alugou o carro? '))
print('Você deverá pagar R${:.2f} pelo aluguel do carro.'.format(60*d + 0.15*km))

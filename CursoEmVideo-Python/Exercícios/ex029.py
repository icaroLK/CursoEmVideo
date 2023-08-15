v = float(input('Quantos km/h estava o carro? '))
if v < 80:
    print('Você não será multado')
else:
    print('Você estava a {:.0f}km/h acima do limite e receberá uma multa de R${:.2f}'.format(v-80, (v-80)*7))
print('Dirija com segurança')

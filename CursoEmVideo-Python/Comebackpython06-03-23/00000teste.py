dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês: '))
ano = int(input('Insira o ano: '))
hora = int(input('Insira a hora (formato 24h): '))
min = int(input('Insira os minutos: '))
seg = int(input('Insira os segundos: '))



data = []
list = [seg, min, hora, dia, mes, ano]
for c in range(0, 5 + 1):
    data.append(int(list[c]))
print('data: ',data)
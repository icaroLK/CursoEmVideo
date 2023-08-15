dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês: '))
ano = int(input('Insira o ano: '))
hora = int(input('Insira a hora (formato 24h): '))
min = int(input('Insira os minutos: '))
seg = int(input('Insira os segundos: '))

data = []
list = [dia, mes, ano, hora, min, seg]

for c in range(0,14):
    data.append(dia[c])

add = 6
qtd = 181

list = [' ', 'dia', mes, ano, hora, min, seg]


print(list[1])

print(list[1].replace('dia', mes))



c = 1
while c < 7:
    if add == c:
        list[c] += qtd
    c += 1



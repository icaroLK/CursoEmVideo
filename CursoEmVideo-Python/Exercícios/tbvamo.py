dia = input('Insira o dia: ')
mes = input('Insira o mês: ')
ano = input('Insira o ano: ')
hora = input('Insira a hora (formato 24h): ')
min = input('Insira os minutos: ')
seg = input('Insira os segundos: ')

data = []
list = [dia, mes, ano, hora, min, seg]
for c in range(0, 5 + 1):
    data.append(int(list[c]))
print(data)
print('\nData atual: \n{:02d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}'.format(dia, mes, ano, hora, min, seg))





c = 1
while c < 7:
    if add == c:
        tempo += qtd
    c += 1


if seg >= 60:
    min += seg // 60
    seg = seg % 60
if min >= 60:
    hora += min // 60
    min = min % 60
if hora >= 24:
    dia += hora // 24
    hora = hora % 24


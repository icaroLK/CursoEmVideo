dia = '12'
mes = '05'
ano = '2000'
hora = '12'
min = '40'
seg = '40'


data = []
list = [seg, min, hora, dia, mes, ano]
for c in range(0, 5 + 1):
    data.append(int(list[c]))
print(data)
print('\nData atual: \n{:02d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}'.format(int(dia), int(mes), int(ano), int(hora), int(min), int(seg)))


add = int(input('''\nSelecione a unidade de tempo que deseja adicionar:
[1] Dia
[2] Mes
[3] Ano
[4] Horas
[5] Minutos
[6] Segundos
R: '''))
qtd = int(input('Insira a quantidade de tempo que será adicionada: '))


ord = [int(dia), int(mes), int(ano), int(hora), int(min), int(seg)]
data = ord

c = 1
while c < 7:
    if add == c:
        ord[c-1] += qtd
    c += 1
data = ord
print(data) #até aqui foi agr so falta add os limites tipo 60 seg vira 1 min
#print(data[::-1])

for c in range(0, 6):

    data.insert(c, ord[c])
print(data)
dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês: '))
ano = int(input('Insira o ano: '))
hora = int(input('Insira a hora (formato 24h): '))
min = int(input('Insira os minutos: '))
seg = int(input('Insira os segundos: '))

print('\nData atual: \n{}/{}/{} {}:{}:{}'.format(dia, mes, ano, hora, min, seg))

add = int(input('''\nSelecione a unidade de tempo que deseja adicionar:
[1] Dia
[2] Mes
[3] Ano
[4] Horas
[5] Minutos
[6] Segundos
R: '''))

qtd = int(input('Insira a quantiade de tempo aumentada: '))

if add == 6:
    seg += qtd
    if seg + qtd >= 60:
        min += 1
        seg = seg + qtd - 60
    if min >= 60:
        hora += 1
        min = '00'
    if hora >= 24:
        dia += 1
        hora = '00'
    if dia > 31:
        mes += 1
        dia = '00'
    if mes > 12:
        ano += 1
        mes = '00'
    print('Nova data:\n{}/{}/{} {}:{}:{}'.format(dia, mes, ano, hora, min, seg))


if add == 5:
    if min + qtd >= 60:
        hora += 1
        min = min + qtd - 60
    if hora >= 24:
        dia += 1
        hora = '00'
    if dia > 31:
        mes += 1
        dia = '00'
    if mes > 12:
        ano += 1
        mes = '00'
    print('Nova data:\n{}/{}/{} {}:{}:{}'.format(dia, mes, ano, hora, min, seg))


if add == 4:
    if hora + qtd >= 24:
        dia += 1
        hora = hora + qtd - 60
    if dia > 31:
        mes += 1
        dia = '00'
    if mes > 12:
        ano += 1
        mes = '00'
    print('Nova data:\n{}/{}/{} {}:{}:{}'.format(dia, mes, ano, hora, min, seg))
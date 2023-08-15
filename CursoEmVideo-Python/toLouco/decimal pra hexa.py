dec = int(input('Insira um número em decimal: '))

cu = dec
hexa = []
while True:
    if cu % 16 == 10:
        hexa.append('A')
    elif cu % 16 == 11:
        hexa.append('B')
    elif cu % 16 == 12:
        hexa.append('C')
    elif cu % 16 == 13:
        hexa.append('D')
    elif cu % 16 == 14:
        hexa.append('E')
    elif cu % 16 == 15:
        hexa.append('F')
    else:
        hexa.append(cu % 16)
    if cu // 16 == 0 and cu % 16 == 0 and cu == 0:
        break
    cu = cu // 16


hex = ((hexa[::-1])[1:])
qtd = len(hex)
vez = 0
print("O número decimal '\033[34m{}\033[m' em hexadecimal é \033[34m".format(dec), end='')
while vez != qtd:
    print(hex[vez], end='')
    vez += 1

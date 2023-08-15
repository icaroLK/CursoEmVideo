print("="*6, "\033[97mCALCULADORA DE DECIMAL PRA HEXA/BIN\033[m", "="*6)
resp = int(input('\033[97m[1]\033[m Decimal pra \033[34mBinário\033[m'
                 '\n\033[97m[2]\033[m Decimal pra \033[33mHexadecimal\033[m\nR: '))
if resp == 1:
    dec = int(input('\nInsira um número em decimal: '))
    cu = dec
    binar = []
    while True:
        binar.append(cu % 2)
        if cu // 2 == 0 and cu % 2 == 0 and cu == 0:
            break
        cu = cu // 2
    bin = ((binar[::-1])[1:])
    qtd = len(bin)
    vez = 0
    print("O número decimal '\033[97m{}\033[m' em binário é \033[34m".format(dec), end='')
    while vez != qtd:
        print(bin[vez], end='')
        vez += 1

elif resp == 2:
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
    print("O número decimal '\033[97m{}\033[m' em hexadecimal é \033[33m".format(dec), end='')
    while vez != qtd:
        print(hex[vez], end='')
        vez += 1

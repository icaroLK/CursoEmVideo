dec = int(input('\nInsira um número em decimal: '))
cu = dec
binar = []
while True:
    while True: #bin
        binar.append(cu % 2)
        if cu // 2 == 0 and cu % 2 == 0 and cu == 0:
            break
        cu = cu // 2
    print("O número decimal '\033[97m{}\033[m' em binário é \033[34m".format(dec), end='')

    while True: #pent
        binar.append(cu % 2)
        if cu // 2 == 0 and cu % 2 == 0 and cu == 0:
            break
        cu = cu // 2





    bin = ((binar[::-1])[1:])
    qtd = len(bin)
    vez = 0


    while vez != qtd:
        print(bin[vez], end='')
        vez += 1
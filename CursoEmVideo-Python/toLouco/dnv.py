dec = int(input('\nInsira um número em decimal: '))
print('DECIMAL = {}\n'.format(dec))

base = 2
cu = dec
binar = []
while True:
    while True:
        binar.append(cu % base)
        if cu // base == 0 and cu % base == 0 and cu == 0:
            break
        cu = cu // base
    bin = ((binar[::-1])[1:])
    qtd = len(bin)
    vez = 0
    print("\033[mBinário = \033[34m".format(dec), end='')
    base +=1
    while vez != qtd:
        print(bin[vez], end='')
        vez += 1


    break
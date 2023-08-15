dec = int(input('Insira um número em decimal: '))
print('\n\033[1;97mDECIMAL = {}\033[m\n'.format(dec))

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
print("\033[mBinário = \033[34m".format(dec), end='')
while vez != qtd:
    print(bin[vez], end='')
    vez += 1




cu = dec
binar = []
while True:
    binar.append(cu % 3)
    if cu // 3 == 0 and cu % 3 == 0 and cu == 0:
        break
    cu = cu // 3
bin = ((binar[::-1])[1:])
qtd = len(bin)
vez = 0
print("\n\033[mTernário = \033[34m".format(dec), end='')
while vez != qtd:
    print(bin[vez], end='')
    vez += 1


base = 4
cu = dec
binar = []
while True:
    binar.append(cu % base)
    if cu // base == 0 and cu % base == 0 and cu == 0:
        break
    cu = cu // base
bin = ((binar[::-1])[1:])
qtd = len(bin)
vez = 0
print("\n\033[mQuaternário = \033[34m".format(dec), end='')
while vez != qtd:
    print(bin[vez], end='')
    vez += 1



base = 5
cu = dec
binar = []
while True:
    binar.append(cu % base)
    if cu // base == 0 and cu % base == 0 and cu == 0:
        break
    cu = cu // base
bin = ((binar[::-1])[1:])
qtd = len(bin)
vez = 0
print("\n\033[mPental = \033[34m".format(dec), end='')
while vez != qtd:
    print(bin[vez], end='')
    vez += 1




base = 6
cu = dec
binar = []
while True:
    binar.append(cu % base)
    if cu // base == 0 and cu % base == 0 and cu == 0:
        break
    cu = cu // base
bin = ((binar[::-1])[1:])
qtd = len(bin)
vez = 0
print("\n\033[mSenário = \033[34m".format(dec), end='')
while vez != qtd:
    print(bin[vez], end='')
    vez += 1



base = 7
cu = dec
binar = []
while True:
    binar.append(cu % base)
    if cu // base == 0 and cu % base == 0 and cu == 0:
        break
    cu = cu // base
bin = ((binar[::-1])[1:])
qtd = len(bin)
vez = 0
print("\n\033[mSeptuário = \033[34m".format(dec), end='')
while vez != qtd:
    print(bin[vez], end='')
    vez += 1





base = 8
cu = dec
binar = []
while True:
    binar.append(cu % base)
    if cu // base == 0 and cu % base == 0 and cu == 0:
        break
    cu = cu // base
bin = ((binar[::-1])[1:])
qtd = len(bin)
vez = 0
print("\n\033[mOctal = \033[34m".format(dec), end='')
while vez != qtd:
    print(bin[vez], end='')
    vez += 1




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
print("\n\033[mHexadecimal = \033[34m".format(dec), end='')
while vez != qtd:
    print(hex[vez], end='')
    vez += 1
print('\n')
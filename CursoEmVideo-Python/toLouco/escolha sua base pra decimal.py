print('\033[1;97m_\033[m'*50)
print("\033[1;97m=\033[m"*6, "\033[1;34mCALCULADORA DE TRANSFORMAÇÕES DE BASES\033[m", "\033[1;97m=\033[m"*6)
print('\033[1;97m_\033[m'*50)


num = int(input('Insira um número na base decimal: '.format(base)))
dec = str(num)
tamanho = len(dec)-1
vez = 0
cu = []
pos = -1
resp = 0
while vez != tamanho+2:
    if dec[0] != '0':
        cu = base ** (tamanho - vez)
        pos += 1

        if pos == tamanho + 1:
            break

        if dec[pos] == '1':
            resp += cu

        if dec[pos] == '2':
            resp += (cu*2)

        if dec[pos] == '3':
            resp += (cu*3)

        if dec[pos] == '4':
            resp += (cu*4)

        if dec[pos] == '5':
            resp += (cu*5)

        if dec[pos] == '6':
            resp += (cu*6)

        if dec[pos] == '7':
            resp += (cu*7)

        if dec[pos] == '8':
            resp += (cu*8)

        if dec[pos] == '9':
            resp += (cu*9)

        if dec[pos] == '10':
            resp += (cu*10)
        vez += 1
print(''
      '\nBase {}: \033[36m{}\033[m'
      '\n  ='
      '\nBase decimal: \033[1;35m{}\033[m'.format(base, num, resp))
t = 0
s = 0
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
print(' ')
if n1 > n2:
    if n2 % 2 ==0:
        for rola in range(n2, n1+1, 2):
            t += 1
            s += rola
            print(rola, end='/')

    elif n2 % 2 !=0:
        for rola in range(n2+1, n1+1, 2):
            t += 1
            s += rola
            print(rola, end='/')

    print('\n\nA quantidade de números pares entre \033[32m{}\033[m e \033[32m{}\033[m é \033[31m{}\033[m'
          ' e a soma entre eles é \033[31m{}\033[m'.format(n2, n1, t, s))

if n2 > n1:
    if n1 % 2 == 0:
        for rola in range(n1, n2+1, 2):
            t += 1
            s += rola
            print(rola, end='/')
    elif n1 % 2 != 0:
        for rola in range(n1+1, n2+1, 2):
            t += 1
            s += rola
            print(rola, end='/')
    print('\n\nA quantidade de números pares entre \033[32m{}\033[m e \033[32m{}\033[m é \033[31m{}\033[m'
          ' e a soma entre eles é \033[31m{}\033[m'.format(n1, n2, t, s))


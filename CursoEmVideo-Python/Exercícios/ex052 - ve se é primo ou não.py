n = int(input('Insira um número: '))
t = 0

for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;34m', end='')
        t += 1

    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')

print('\n\n\033[mO número {} foi divisível \033[34m{}\033[m vezes'.format(n, t))

if t == 2:
    print('\033[32mÉ primo\033[m')
else:
    print('\033[31mNÃO é primo\033[m')

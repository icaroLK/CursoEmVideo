print('Vamos ver se o número é primo ou não!\n')
n = int(input('Insira um número: '))

list = []

for c in range(2, n):
    if n % c == 0:
        list.append(c)

if list == []:
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não é primo pq foi divisível por {}'.format(n, list))


'''print('Vamos ver se o número é primo ou não!\n')
n = int(input('Insira um número: '))
tot = 0

for c in range(1, n+1):
    if n % c == 0:
        print('\033[31m', end='')
        tot += 1
    else:
        print('\033[97m', end='')
    print(c, end=' ')

if tot != 2:
    print('\033[m\nO número {} foi divisível {} vezes, logo ele não é primo'.format(n, tot))
else:
    print('\033[m\nO número {} não foi divisível nenhuma vez, logo ele é primo'.format(n))
'''
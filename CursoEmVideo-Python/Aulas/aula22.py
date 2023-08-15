def fatorial(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


num = int(input('Insira um número: '))
fat = fatorial(num)
print('O fatorial de {} é {}'.format(num, fat))

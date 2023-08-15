while True:
    n = int(input('Insira um valor: '))
    print('=' * 15)
    if n <= 0:
        break
    for c in range(1, 10+1):
        print('{} x {} = {}'.format(c, n, c*n))
    print('=' * 15)
print('cabooo')
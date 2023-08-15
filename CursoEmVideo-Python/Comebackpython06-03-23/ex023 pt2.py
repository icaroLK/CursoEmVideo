n = int(input('Insira um número de 0 a 9999: '))


u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('\nO número escolhido foi {}\n'
          'Unidade: {}\n'
          'Dezenas: {}\n'
          'Centenas: {}\n'
          'Milhar: {}'.format(n, u, d, c, m))



'''n = str(input('Insira um número de 0 a 9999: ')).strip()

if len(n) == 4:
    u = n[0]
    d = n[1]
    c = n[2]
    m = n[3]
    print('\nO número escolhido foi {}\n'
          'Unidade: {}\n'
          'Dezenas: {}\n'
          'Centenas: {}\n'
          'Milhar: {}'.format(n, u, d, c, m))

if len(n) == 3:
    u = n[0]
    d = n[1]
    c = n[2]
    print('\nO número escolhido foi {}\n'
          'Unidade: {}\n'
          'Dezenas: {}\n'
          'Centenas: {}\n'
          'Milhar: {}'.format(n, u, d, c, '0'))

if len(n) == 2:
    u = n[0]
    d = n[1]
    print('\nO número escolhido foi {}\n'
          'Unidade: {}\n'
          'Dezenas: {}\n'
          'Centenas: {}\n'
          'Milhar: {}'.format(n, u, d, '0', '0'))

if len(n) == 1:
    u = n[0]
    print('\nO número escolhido foi {}\n'
          'Unidade: {}\n'
          'Dezenas: {}\n'
          'Centenas: {}\n'
          'Milhar: {}'.format(n, u, '0', '0', '0'))
'''
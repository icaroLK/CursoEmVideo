a1 = int(input('Insira um número: '))
a2 = int(input('Insira um número: '))

if a1 > a2:
    print('O {} é maior'.format(a1))
elif a1 < a2:
    print('O {} é maior'.format(a2))
elif a1 == a2:
    print('Os dois valores são iguais')
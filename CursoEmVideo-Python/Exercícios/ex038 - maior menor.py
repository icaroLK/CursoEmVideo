n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

if n1 > n2:
    print('O primeiro valor ({}) é \033[32mmaior\033[m que o segundo valor ({})'.format(n1, n2))

elif n1 < n2:
    print('O segundo valor ({}) é \033[32mmaior\033[m que o primeiro valor ({})'.format(n2, n1))

else:
    print('Os dois valores são iguais')

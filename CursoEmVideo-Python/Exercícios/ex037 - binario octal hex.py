n = int(input('Digite um número: '))
e = str(input('''Escolha uma conversão:
\n[1] para \033[34mbinário\033[m
[2] para \033[31moctal\033[m
[3] para \033[32mhexadecimal\033[m
\nSua opção: '''))


if e in '1':
      print('\nO número {} na forma binária é \033[34m{}\033[m'.format(n, bin(n)[2:]))

elif e in '2':
      print('\nO número {} na forma octal é \033[31m{}\033[m'.format(n, oct(n)[2:]))

elif e in '3':
      print('\nO número {} na forma hexadecimal é \033[32m{}\033[m'.format(n, hex(n)[2:]))
else:
      print('Comando \033[31minválido\033[m. Tente novamente')



#outra forma de tirar o 0b 0o 0x
'''if e in '1':
      print('\nO número {} na forma binária é \033[34m{}\033[m'.format(n, str(bin(n)).replace('0b','')))

elif e in '2':
      print('\nO número {} na forma octal é \033[31m{}\033[m'.format(n, str(oct(n)).replace('0o','')))

elif e in '3':
      print('\nO número {} na forma hexadecimal é \033[32m{}\033[m'.format(n, str(hex(n)).replace('0x','')))
else:
      print('Comando \033[31minválido\033[m. Tente novamente')'''

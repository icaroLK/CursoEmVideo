a = 5
b = 6
s = a+b
print('A soma de {} e {} é \033[32m{}\033[m'.format(a, b, s))


a = 5
b = 6
s = a+b
print('A soma de {0} e {1} é {3}{2}{4}\033[m'.format(a, b, s, '\033[32m', '\033[m'))


#print('\033[32mHello world\033[m')
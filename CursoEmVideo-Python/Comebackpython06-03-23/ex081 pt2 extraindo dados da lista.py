c = 0
list = []
while True:
    n = int(input('Insira um número (999 para parar): '))
    if n == 999:
        break
    list.append(n)
    c += 1
print('Foram digitados {} elementos'.format(c))

list.sort(reverse=True)
print('A lista na forma descrescente fica {}'.format(list))
if 5 in list:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não foi encontrado na lista')
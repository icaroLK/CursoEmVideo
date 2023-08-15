list = []
valor = 0
while True:
    valor = int(input('Insira um número (999 para parar): '))
    if valor == 999:
        break
    if valor in list:
        print('Valor duplicado. Tente novamente:')
    else:
        list.append(valor)

list.sort()
print('Você digitou os valores: \033[34m', end='')

for c in range(len(list)):
    print(list[c], end=' ')


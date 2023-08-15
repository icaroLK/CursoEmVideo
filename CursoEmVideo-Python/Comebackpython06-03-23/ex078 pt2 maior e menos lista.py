list = []
for c in range(5):
    num = int(input('Insira um número para a posição {}: '.format(c)))
    if c == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    list.append(num)
print('—'*40)
print('Você digitou os valores {}'.format(list))
print("O menor número foi o '{}' e está na posição ".format(menor), end='')
for c, v in enumerate(list):
    if v == menor:
        print("{}...".format(c), end='')
print("\nO maior número foi o '{}' e está na posição ".format(maior), end='')
for c, v in enumerate(list):
    if v == maior:
        print("{}...".format(c), end='')
print()
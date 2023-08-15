num = [[], []]
posp = 0
while True:
    n = int(input('Insira um número (999 para parar): '))
    if n == 999:
        break
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print('\nNúmeros pares digitados: {}'.format(sorted(num[0])))
print('Números ímpares digitados: {}'.format(sorted(num[1])))









'''num = []
posp = 0
while True:
    n = int(input('Insira um número (999 para parar): '))
    if n == 999:
        break
    if n % 2 == 0:
        num.insert(posp, n)
        posp += 1 #o valor do posp no final vai ser a quantiade de numeros pares
                # ou seja a posição que termina os pares
    if n % 2 != 0:
        num.insert(posp+1, n)
#   print(num) #teste pra ir vendo se ta add certo
print('\nNúmeros pares digitados: {}'.format(sorted(num[:posp])))
print('Números ímpares digitados: {}'.format(sorted(num[posp:])))
'''
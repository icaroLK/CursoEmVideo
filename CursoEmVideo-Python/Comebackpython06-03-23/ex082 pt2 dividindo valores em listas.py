list = []
par = []
impar = []
while True:
    n = int(input('Insira um número (999 para parar): '))
    if n == 999:
        break
    list.append(n)
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        impar.append(n)
print('Lista inteira: {}\n'
      'Lista de pares: {}\n'
      'Lista de ímpares: {}'.format(list, par, impar))
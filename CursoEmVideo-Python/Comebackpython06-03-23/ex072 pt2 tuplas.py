c = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    n = int(input('Insira um número de 0 a 10: '))
    if 0 <= n <= 10:
        break
    print('\033[31mINVÁLIDO\033[m', end=' ')

print('Você digitou o número',c[n])
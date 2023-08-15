resp = 'S'
n = 0
ex = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'catorze',
          'quinze', 'dezesseis', 'dezesete', 'dezoito',
          'dezenove', 'vinte')

while True:
    while resp == 'S':
        n = int(input('Insira um número de 0 a 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'\nVocê digitou o número {ex[n]}')
    resp = str(input('Deseja continuar? ')).strip().title()[0]
    if resp == 'N':
        break
print('\nObrigado.')


# while True:
#     n = int(input('Insira um número de 0 a 20: '))
#     if 0 <= n <= 20:
#         break
#     print('Tente novamente. ', end='')
# ex = ('zero', 'um', 'dois', 'três', 'quatro',
#       'cinco', 'seis', 'sete', 'oito', 'nove',
#       'dez', 'onze', 'doze', 'treze', 'catorze',
#       'quinze', 'dezesseis', 'dezesete', 'dezoito',
#       'dezenove', 'vinte')
# print(f'Você digitou o número {ex[n]}')



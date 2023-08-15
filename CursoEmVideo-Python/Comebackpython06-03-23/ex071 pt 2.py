print('\033[1;97m=\033[m'*25)
print("\033[1;97m=\033[m"*6, "\033[1;97mLIMA'S BANK\033[m", "\033[1;97m=\033[m"*6)
print('\033[1;97m=\033[m'*25)


print('Cédulas disponíveis: R$50, R$20, R$10, R$1')
n = float(input('Insira o valor a ser sacado: R$'))

cinq = vint = dez = um = 0
cu = n

while n != 0:
    if n // 50 != 0:
        cinq = (n // 50)
        n = n-(cinq*50)
    elif n // 20 != 0:
        vint = n // 20
        n = n-(vint*20)

    elif n // 10 != 0:
        dez = n // 10
        n = n - (dez * 10)

    elif n != 0:
        um = n
        break

print('{:.0f} notas de R$50\n'
      '{:.0f} notas de R$20\n'
      '{:.0f} notas de R$10\n'
      '{:.0f} notas de R$1'.format(cinq, vint, dez, um))
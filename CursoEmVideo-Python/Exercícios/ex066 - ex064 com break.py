qtde = s = 0
while True:
    n = int(input('Insira um número: '))
    if n == 999:
        break
    qtde += 1
    s += n
print(f'A soma entre os {qtde} valores é {s}')
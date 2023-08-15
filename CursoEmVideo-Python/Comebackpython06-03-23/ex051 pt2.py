pri = int(input('Insira o primeiro termo da PA: '))
raz = int(input('Insira a razão da PA: '))
qtd = int(input('Insira a quantidade de termos da PA: '))

dec = pri + (qtd-1) * raz

for c in range(pri, dec+1, raz):
    print(c, end=' / ')

print('\033[31mFIM\033[m')

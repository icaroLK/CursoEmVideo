n1 = float(input('Insira a nota da primeira prova: '))
n2 = float(input('Insira a nota da segunda prova: '))
n3 = float(input('Insira a nota da quarta prova: '))

m = (n1 + n2 + n3)/3

if m >= 7:
    print('\033[32mAPROVADO\033[m')
if 7 > m > 5:
    print('\033[33mRECUPERAÇÃO\033[m')
if m < 5:
    print('\033[31mREPROVADO SEU BOSTA\033[m')

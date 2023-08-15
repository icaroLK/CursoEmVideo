n1 = float(input('Insira a nota da prova 1: '))
n2 = float(input('Insira a nota da prova 2: '))

m = (n1 + n2)/2

print('A sua média ficou {:.1f}'.format(m))
if m >= 7:
    print('Você foi APROVADO')
elif m < 7:
    print('Você foi REPROVADO')


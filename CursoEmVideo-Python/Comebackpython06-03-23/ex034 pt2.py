sal = float(input('Insira seu salário: R$'))
if sal > 1250:
    new = sal + (sal*10/100)
    print('Seu salário receberá um aumento de 10% e passará a ser R${:.2f}'.format(new))
else:
    new = sal + (sal*15/100)
    print('Seu salário receberá um aumento de 15% e passará a ser R${:.2f}'.format(new))

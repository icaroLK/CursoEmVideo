v = float(input('Insira o valor da casa: R$'))
s = float(input('Insira seu salário: R$'))
h = int(input('Em quantos anos você quitará a dívida? '))

p = v / (h * 12) #valor da prestação
# p*100/s é a porcentagem da prestação em relação ao salário

if p > (s*30/100):
    print('\nA prestação ficará no valor de \033[33mR${:.2f}\033[m, equivalente a {:.1f}% do seu salário. '
          '\nEmprestimo \033[31mnegado\033[m'.format(p, (p*100/s)))
else:
    print('\nEmprestimo \033[32mconcedido\033[m')
    print('O valor da prestação será \033[33mR${:.2f}\033[m, o equivalente a {:.1f}% '
          'do seu salário'.format(p, (p*100/s)))

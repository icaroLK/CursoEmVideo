s = float(input('Insira seu salário: '))
if s >= 1250:
    print('Você receberá um \033[1maumento\033[m de 10% (\033[32mR${:.2f}\033[m) e'
          ' ganhará no total de R${:.2f}'.format(s*10/100, s+(s*10/100)))
else:
    print('Você receberá um \033[1maumento\033[m de 15% (\033[32mR${:.2f}\033[m) e ganhará '
          'um total de R${:.2F}'.format(s*15/100, s+(s*15/100)))

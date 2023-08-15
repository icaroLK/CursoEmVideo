n1 = float(input('Insira a nota da sua primeira prova: '))
n2 = float(input('Insira a nota da sua segunda prova: '))
m = (n1 + n2)/2


if m < 7:
    if m + 0.5 >= 7:
        print('''
Sua nota média ficou {:.1f} arredondada em {:.1f} pontos
\033[32mAPROVADO\033[m
\033[33mESTUDE MAIS\033[m'''.format(m, 7-m))

    else:
        print('''Sua média ficou {:.1f} 
Você ficou {:.1f} pontos \033[31mabaixo\033[m da média. 
\033[31mRECUPERAÇÃO\033[m'''.format(m, 7 - m))


elif m > 7:
    print('''
Sua média ficou {:.1f}
Você passou com {} pontos \033[32macima\033[m da média.
\033[32mAPROVADO\033[m'''.format(m, m-7))

elif m == 7:
    print('''
Sua médica ficou exatamente {}
Você passou sem pontos adicionais.
\033[33mEstude um pouco mais\033[m'''.format(m))

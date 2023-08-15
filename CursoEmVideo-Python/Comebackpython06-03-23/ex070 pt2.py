print('\033[1;97m=\033[m'*27)
print("\033[1;97m=\033[m"*6, "\033[1;97mKUCHA'S STORE\033[m", "\033[1;97m=\033[m"*6)
print('\033[1;97m=\033[m'*27)

tot = caro = pmb = qtd = 0
barato = ' '

while True:
    nome = input('Nome do produto: ').title().strip()
    p = float(input("Preço do item '{}': R$".format(nome)))
    tot += p
    qtd += 1
    if p > 75:
        caro += 1
    if qtd == 1 or p < pmb:
        pmb = p
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = input('Continuar? [S/N]:').strip().upper()[0]
    if resp == 'N':
        break

print('\n{:-^40}'.format('\033[1m FIM DO PROGRAMA \033[m'))
print('''A compra teve um total de {} produtos
O preço total foi de \033[32mR${:.2f}\033[m
Na compra existem {} produtos que custam mais de R$75
O produto mais barato foi a/o \033[34m{}\033[m que custa \033[32mR${:.2f}\033[m'''.format(qtd, tot, caro, barato, pmb))

prett = qtde1000 = barat = cont = 0
maisbar = ' '
while True:
    nome = str(input('\nNome do produto: ')).strip().title()
    preco = float(input('Preço do produto: R$'))
    prett += preco
    cont += 1
    if preco > 1000:
        qtde1000 += 1
    if cont == 1 or preco < barat:
        barat = preco
        maisbar = nome
    dsj = ' '
    while dsj not in 'SN':
        dsj = str(input('Continuar? ')).strip().title()[0]
    if dsj in 'N':
        break
print('\n{:-^40}'.format('\033[1m FIM DO PROGRAMA \033[m'))
print(f'''O preço total foi de \033[32mR${prett:.2f}\033[m
Na compra existem {qtde1000} produtos que custam mais de R$1000
O produto mais barato foi a/o \033[34m{maisbar}\033[m que custa \033[32mR${barat:.2f}\033[m''')

p = float(input('Insira o preço do produto: R$'))
forma = int(input('\nEscolha a forma de pagamento: '
                  '\n[1] À vista dinheiro (10% off) '
                  '\n[2] À vista cartão (5% off)'
                  '\n[3] Até 2x cartão'
                  '\n[4] 3x ou mais (20% juros)'
                  '\nR: '))

um = p - (p * 10 / 100)
dois = p - (p * 5 / 100)
quatro = p + (p * 20 / 100)

if forma == 1:
    print('O valor da sua compra ficou R${:.2f}'.format(um))

if forma == 2:
    print('O valor da sua compra ficou R${:.2f}'.format(dois))

if forma == 3:
    print('O valor da sua compra ficou R${:.2f}'.format(p))

if forma == 4:
    print('O valor da sua compra ficou R${:.2f}'.format(quatro))

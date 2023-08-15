p = float(input('Insira seu peso (kg): '))
h = float(input('Insira sua altura (m): '))
imc = p / (h**2)
print('\nSeu IMC é {:.1f}'.format(imc))

g = str(input('''
Escolha qual opção você se encaixa melhor:

[1] sou fortinho
[2] sou gordinho\n\n''')).strip()


if g == '2':
    if imc < 18.5:
        print('Você está abaixo do peso ideal.')
    elif 25 > imc > 18.5:
        print('Continue assim, seu peso está ideal.')
    elif 30 > imc > 25:
        print('Você tem sobrepeso.')
    elif 40 > imc > 30:
        print('Você é obeso.')
    elif imc > 40:
        print('Obesidade \033[31mmórbida\033[m! Procure ajuda imediatamente.')

elif g == '1':
    if imc < 18.5:
        print('Frango. VAI COMER')
    elif 25 > imc > 18.5:
        print('Shape de praia d bosta kkkkk meme ta pica')
    elif 30 > imc > 25:
        print('Começou a tomar bomba???')
    elif 40 > imc > 30:
        print('Gigantesco')
    elif imc > 40:
        print('HULK FILHA DA PUTA??? ABERRAÇÃO QQ É ISSO O CARA É UMA MONTANHA')
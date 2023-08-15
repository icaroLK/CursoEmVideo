from lib.interface import interfacee


op = []


nome = input('Insira o nome do seu menu: ').strip().upper()
qtd = int(input('Insira a quantidade de opções que o seu menu terá: '))

for c in range(qtd):
    alt = input('Digite a {}° opção do menu: '.format(c+1)).title().strip()
    op.append(alt)


while True:
    respo = interfacee.menu(nome, op)
    for a in range(qtd):
        if respo == a

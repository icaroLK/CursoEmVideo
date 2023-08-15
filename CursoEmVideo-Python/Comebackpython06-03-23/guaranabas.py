cem = cinq = vint = dez = cinc = dois = um = valor = 0

print('\033[1;97m{}'.format('=')*30)
print('{:^30}'.format("KUCHA's BANK"))
print('\033[1;97m{}\033[m'.format('=')*30)
while True:
    if valor == 0:
        print('\nCédulas disponíveis: \n\033[34mR$100 // R$50 // R$20 // R$10 // R$5 // R$2\033[m')
        print('\nMoedas disponíveis: \n\033[34mR$1\033[m')
        valor = int(input('\nInsira o valor a ser sacado: R$'))
    if valor >= 100:
        valor -= 100
        cem += 1
    if 100 > valor >= 50:
        valor -= 50
        cinq += 1
    if 50 > valor >= 20:
        valor -= 20
        vint += 1
    if 20 > valor >= 10:
        valor -= 10
        dez += 1
    if 10 > valor >= 5:
        valor -= 5
        cinc += 1
    if 5 > valor >= 2:
        valor -= 2
        dois += 1
    if 2 > valor >= 1:
        valor -= 1
        um += 1
    if valor == 0:
        break


list = [cem, cinq, vint, dez, cinc, dois, um]
listan = ['100', '50', '20', '10', '5', '2', '1']

for c in range(0, 6+1):
    print('{}{}{} cédulas de \033[32mR${}\033[m'.format('\033[33m' if list[c] != 0 else '', list[c], '\033[m', listan[c]))


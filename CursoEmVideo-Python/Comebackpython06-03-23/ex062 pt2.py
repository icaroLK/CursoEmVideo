pri = int(input('Insira o primeiro termo da PA: '))
raz = int(input('Insira a razão da PA: '))
termos = qtd = int(input('Insira a quantidade de termos da PA: '))

cu = 0
resp = []

while True:
    while cu < qtd:
        print(pri, end='')
        print(end=' / ') if cu < qtd-1 else print(end=' -> PAUSA')
        pri += raz
        cu += 1
    print("\nQuantos termos você quer mostrar a mais? (Insira 'Pare' para parar)")
    resp = input('R: ').lower()
    if resp in 'pare':
        break
    qtd = int(resp)
    cu = 0
    termos += qtd

print('\ncabooo')
print('PA finalizada com {} termos'. format(termos))
tupla = (int(input('Insira o 1° número: ')),
         int(input('Insira o 2° número: ')),
         int(input('Insira o 3° número: ')),
         int(input('Insira o 4° número: ')), )

print('\nVocê digitou os valores: ', end='')
for c in tupla:
    print('\033[34m', c, '\033[m', end='')



print(f'\nO número 9 apareceu {tupla.count(9)} vez{"" if tupla.count(9) == 1 else "es"}') #trampo aqui pra ficar
                                                                                        # bonitinho e arrumar o plural



if 3 in tupla:
    print(f'O número 3 apareceu na {(tupla.index(3))+1}° posição')
else:
    print(f'O número 3 não apareceu em nenhuma posição')



print('Os valores pares digitados foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')

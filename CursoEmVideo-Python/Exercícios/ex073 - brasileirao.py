bigbr = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense',
         'Corinthians', 'CAP', 'Atletico-MG', 'São Paulo', 'Fortaleza',
         'Botafogo', 'América-MG', 'Santos', 'Goias', 'Bragantino',
         'Coritiba', 'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')
print('\nSegue a lista dos 20° primeiros colocados do Brasileirão:\n')
for v in bigbr:
    print(v, '\n' if v == bigbr[5] or v == bigbr[10] or v == bigbr[15] else ' / ', end='')
print('\n')
for c in range(0, 5):
    print(f'O {c+1}° colocado é o {bigbr[c]}')
    if c == 4:
        print('')
for cu in range(16, 20):
    print(f'O {cu+1}° colocado é o {bigbr[cu]}')
    if cu == 19:
        print('')
print('Os times em órdem alfabética ficam: \n')
for v in sorted(bigbr):
    print(v, '\n' if v == sorted(bigbr)[5] or v == sorted(bigbr)[10] or v == sorted(bigbr)[15] else ' / ', end='')
print('\n')

print(f'O time do Atlético-PR está na {bigbr.index("CAP")+1}ª posição')
print('Obrigado')

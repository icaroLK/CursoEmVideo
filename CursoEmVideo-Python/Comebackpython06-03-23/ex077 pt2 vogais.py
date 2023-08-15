list = ('aprender', 'programar', 'linguaguem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for c in range(0, len(list)):
    print('\nA palavra {} tem as vogais: '.format(list[c]), end=' ')
    if 'a' in list[c]:
        print('a', end=' ')
    if 'e' in list[c]:
        print('e', end=' ')
    if 'i' in list[c]:
        print('i', end=' ')
    if 'o' in list[c]:
        print('o', end=' ')
    if 'u' in list[c]:
        print('u', end=' ')

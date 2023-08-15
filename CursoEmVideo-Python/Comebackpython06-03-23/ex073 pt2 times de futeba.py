times = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Santos',
         'Fluminense', 'Fortaleza', 'Palmeiras', 'Atlético-GO', 'Corinthians',
         'Grêmio', 'Sport Recife', 'Bahia', 'Ceará SC', 'Botafogo', 'Vasco da Gama',
         'Athletico-PR', 'Coritiba', 'Bragantino-SP', 'Goiás')


print('Os 5 primeiros colocados são: {}'.format(times[:5]))
print('Os 4 ultímos colocados são {}'.format(times[-4:]))
print('Os times em órdem alfabética ficam: {}'.format(sorted(times)))
print('O Corinthians está na {}° posição'.format(times.index('Corinthians')+1))

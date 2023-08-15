cid = str(input('Insira o nome da sua cidade: ')).title().strip()
separado = cid.split()

tem = ('Santo' in separado[0])
print('A cidade {} começa com a palavra "Santo"?\n{}'.format(cid, tem))

#if 'Santo' in separado[0]:
#   print('A sua cidade começa com a palavra "Santo"')
#else:
#    print('A sua cidade não começa com a palavra "Santo"')
n = str(input('Digite um número: ')).strip()
print('\nAnalisando o número {}'.format(n))

t4 = int(len(n[:3]))
print('Unidade: {}'.format(n.replace(n[:3], t4 * '_')))

z = int(n)
z2 = z // 10
z3 = str(z2)
t3 = int(len(n[:2]))
print('Dezena: {}'.format(z3.replace(n[:2], t3 * '_')         + int(len(str(int(n) % 10)))*'_'))

y = int(n)
y2 = y // 100
y3 = str(y2)

t2 = int(len(n[:1]))
print('Centena: {}'.format(y3.replace(n[:1], t2 * '_')         + int(len(str(int(n) % 100)))*'_'))

t1 = int(len(n[1:]))
print('Milhar: {}'.format(n.replace(n[1:], t1 * '_')))


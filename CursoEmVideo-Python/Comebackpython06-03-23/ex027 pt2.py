n = str(input('Insira seu nome: ')).strip().title()
print('Seu nome inteiro é {}'.format(n))

n = n.split()

n1 = n[0]
n2 = n[(len(n)-1)]
# ou n2 = n[-1]

print('Seu primeiro nome: {}\n'
      'Seu último nome: {}'.format(n1, n2))

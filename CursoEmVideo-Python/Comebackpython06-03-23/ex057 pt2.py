sex = input('Insira seu sexo: ').strip().upper()[0]
while sex not in 'MF':
    sex = input('Dados inválidos, insira novamente: ').strip().upper()[0]
print('foi')
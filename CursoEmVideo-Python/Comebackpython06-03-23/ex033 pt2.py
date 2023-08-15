a = int(input('Insira um número: '))
b = int(input('Insira um número: '))
c = int(input('Insira um número: '))

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('{} é o maior número'.format(maior))
print('{} é o menor número'.format(menor))

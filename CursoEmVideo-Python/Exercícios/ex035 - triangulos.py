print('-=-'*10)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-'*10)
a = float(input('\nDigite um lado do triângulo: '))
b = float(input('Digite outro lado do triângulo: '))
c = float(input('Digite o último lado do triângulo: '))

#lado tem que ser menor que a soma dos outros dois
if (b-c)<a<(b+c) and (a-c)<b<(a+c) and (a-b)<c<(a+b):
    print('\033[32mÉ\033[m possivel formar um triângulo')
else:
    print('\033[31mNão\033[m é possível formar um triângulo')

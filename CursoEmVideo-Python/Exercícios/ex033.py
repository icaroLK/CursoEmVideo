x = str(input('Digite três números: ')).split()
x1 = int(x[0])
x2 = int(x[1])
x3 = int(x[2])
if x1 > x2 and x1 > x3:
    print('\033[1m{}\033[m é o \033[32mmaior\033[m número'.format(x1))
if x2 > x1 and x2 > x3:
    print('\033[1m{}\033[m é o \033[32mmaior\033[m número'.format(x2))
if x3 > x1 and x3 > x2:
    print('\033[1m{}\033[m é o \033[32mmaior\033[m número'.format(x3))
#agr o menor numero
if x1<x2 and x1<x3:
    print('\033[1m{}\033[m é o \033[31mmenor\033[m número'.format(x1))
if x2<x1 and x2<x3:
    print('\033[1m{}\033[m é o \033[31mmenor\033[m número'.format(x2))
if x3<x1 and x3<x2:
    print('\033[1m{}\033[m é o \033[31mmenor\033[m número'.format(x3))


'''x1 = int(input('Digite um valor: '))
x2 = int(input('Digite outro valor: '))
x3 = int(input('Ultimo valor: '))'''
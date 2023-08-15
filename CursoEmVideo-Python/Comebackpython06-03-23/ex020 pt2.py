from random import shuffle
a1 = str(input('Nome do 1° aluno: '))
a2 = str(input('Nome do 2° aluno: '))
a3 = str(input('Nome do 3° aluno: '))
a4 = str(input('Nome do 4° aluno: '))
a = [a1, a2, a3, a4]
shuffle(a)

print('A ordem de apresentação será {}'.format(a))

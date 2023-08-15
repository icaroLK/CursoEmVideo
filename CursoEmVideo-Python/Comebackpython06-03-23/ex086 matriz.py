print('''\033[1;97m————————————————————————————————————————
    MONTANDO OS TERMOS DE UMA MATRIZ    
————————————————————————————————————————\033[m

A base da sua matriz será 3x3

[1,1][1,2][1,3]
[2,1][2,2][2,3]
[3,1][3,2][3,3]

''')
mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(1, 3+1):
    for c in range(1, 3+1):
        mat[l-1][c-1] = int(input('Insira um valor para a posição [{},{}]: '.format(l, c)))
for l in range(1, 3+1):
    for c in range(1, 3+1):
        print('[{}]'.format(mat[l-1][c-1]), end='')
    print()
#print("\n{}\n{}\n{}".format(mat[0], mat[1], mat[2])) #meu jeito pra printar










#meu jeito
'''print('\033[1;97m{}'.format('—')*40)
print('\033[1;97m{:^40}\033[m'.format("MONTANDO OS TERMOS DE UMA MATRIZ"))
print('\033[1;97m{}\033[m'.format('—')*40)
mat = ['[1,1]', '[1,2]', '[1,3]', '[2,1]', '[2,2]', '[2,3]', '[3,1]', '[3,2]', '[3,3]']

print('A base da sua matriz será 3x3\n\033[1m')
for c in mat:
    print('{}'.format(c), end='')
    if c == "[1,3]" or c == '[2,3]':
        print('')
#print("{}\n{}\n{}".format(mat[:3], mat[3:6], mat[6:9])) #tb funciona ao inves so for
list = []
print()
for c in range(9):
    valor = int(input('\033[mInsira um valor para a posição {}: '.format(mat[c])))
    list.append(valor)
print("\n{}\n{}\n{}".format(list[:3], list[3:6], list[6:9]))'''
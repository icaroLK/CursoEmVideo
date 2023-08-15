print('''\033[1;97m————————————————————————————————————————
    MONTANDO OS TERMOS DE UMA MATRIZ    
————————————————————————————————————————\033[m

A base da sua matriz será 3x3

[1,1][1,2][1,3]
[2,1][2,2][2,3]
[3,1][3,2][3,3]

''')
mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
col3 = 0
mai2 = []
for l in range(1, 3+1):
    for c in range(1, 3+1):
        mat[l-1][c-1] = int(input('Insira um valor para a posição [{},{}]: '.format(l, c)))
        if mat[l-1][c-1] % 2 == 0:
            par += mat[l-1][c-1]
        if c == 3:
            col3 += mat[l-1][c-1]
        if l == 2:
            mai2.append(mat[l-1][c-1])

for l in range(1, 3+1):
    for c in range(1, 3+1):
        print('[{}]'.format(mat[l-1][c-1]), end='')
    print()
print('A soma dos valores pares é {}'.format(par))
print('Soma dos valores da terceira coluna: {}'.format(col3))
mai2.sort()
print('O maior valor da segunda linha é o {}'.format(mai2[-1]))

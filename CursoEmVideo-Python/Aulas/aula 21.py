'''def soma(a=0, b=0, c=0):
    s = a + b + c
    return s

print(soma(1, 9))'''

def fat(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Insira um número: '))
print(f'O fatorial de {n} é {fat(n)}')
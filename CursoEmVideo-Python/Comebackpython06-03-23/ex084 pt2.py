info = []
glr = []
tot = maior = menor = 0
while True:
    if tot == 0:
        print("Para parar digite \033[31m'Stop'\033[m")
    n = input('\nNome: ').strip().title()
    if n == 'Stop':
        break
    P = input('Peso: ').strip().title()
    if P == 'Stop':
        break
    tot += 1
    p = float(P)
    info.append(n)
    info.append(p)
    if len(glr) == 0:
        maior = menor = p
    else:
        if p < menor:
            menor = p
        elif p > maior:
            maior = p
    glr.append(info[:])
    info.clear()
#print(glr)
print(f'Foram cadastradas {tot} pessoas\n')
print("O maior peso foi de {}Kg. Peso de ".format(maior),end='')
for p in glr:
    if p[1] == maior:
        print('[{}] '.format(p[0]), end='')
print("\nO menor peso foi de {}Kg. Peso de ".format(menor), end='')
for p in glr:
    if p[1] == menor:
        print('[{}] '.format(p[0]), end='')

def maior( * num):
    for p, v in enumerate(num):
        if p == 0:
            maior = v
        if v > maior:
            maior = v
    print('Analisando os valores: ',end='')
    for c in num:
        print(c, end=' ')
    print("\nO maior número da sua lista é o '{}'".format(maior))



maior(1,23,4,2,32,13,14,32,42,1,4,1)
maior(0,5)
#maior()
maior(4)






#ta inclompleto mas quase
'''from random import randint
from time import sleep

def maior( * num):
    for p, v in enumerate(num):
        if p == 0:
            maior = v
        if v > maior:
            maior = v
    print('O maior número da sua lista é {}'.format(maior))



list = []
qtd = int(input('Quantidade de números a serem sorteados: '))
print('Escolha um intevalo para sortear os números')
rg1 = int(input('Início: '))
rg2 = int(input('Final: '))
for c in range(qtd):
    list.append(randint(rg1, rg2))
print('\nGerando Lista...')
sleep(1)
print('Sua lista de números: {}'.format(list))


for c in range(len(list)):
    maior(list[c])'''
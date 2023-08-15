from random import randint
rd = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram:', end='')
for c in rd:
    print('\033[34m', c, '\033[m', end='')


print(f'\n\nO \033[32mmaior\033[m valor foi: \033[34m{sorted(rd)[-1]}\033[m')
print(f'O \033[31mmenor\033[m valor foi: \033[34m{sorted(rd)[0]}\033[m')
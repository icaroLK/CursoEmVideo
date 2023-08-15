from random import randint
n = randint(1, 4)
print('\033[97m=\033[m'*55)
print('\033[97mVOU PENSAR EM UM NÚMERO ENTRE 1 E 4. TENTE ADIVINHAR...\033[m')
print('\033[97m=\033[m'*55)
r = int(input('Que número foi esse?\nR: '))
if r == n:
    print('\033[32mParabéns você acertou!\033[m')
else:
    print('\033[31mVocê errou!\033[m Eu pensei no número {}'.format(n))


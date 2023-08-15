from random import randint

sort = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('Os valore sorteados foram: ', end='')
for c in sort:
    print(c, end=' ')

print('\nO maior número sorteado foi {}'.format(sorted(sort)[-1]))
print('O menor número sorteado foi {}'.format(sorted(sort)[0]))
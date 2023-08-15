n = int(input('Insira a um número. [999 para parar]: '))

s = count = 0

while n != 999:
    s += n
    count += 1
    n = int(input('Insira a um número. [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é {}'.format(count, s))

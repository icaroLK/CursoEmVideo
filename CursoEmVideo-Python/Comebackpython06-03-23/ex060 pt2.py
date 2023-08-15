print('Fatorial de números')
cu = num = n = int(input('Insira um número: '))
vez = 1

print('FATORIAL DE {}\n'.format(cu))


while True:
    if vez < n-1:
        num = num * (n-vez)
    if cu == 0:
        print(' = ', end='')
        break
    if cu == 1:
        print(cu, end='')
    else:
        print(cu, end=' x ')
    cu -= 1
    vez += 1


print('{}'.format(num))


'''print('Fatorial de números')
cu = n = int(input('Insira um número: '))
f = 1

print('FATORIAL DE {}\n'.format(cu))


while cu > 0:

    print(cu, end='')
    print(end=' x ') if cu > 1 else print(end=' = ')
    f *= cu
    cu -= 1

print('{}'.format(f))'''

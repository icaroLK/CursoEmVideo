list = []

for c in range(5):
    valor = int(input('\nInsira um valor: '))
    if c == 0 or valor > list[-1]:
        list.append(valor)
        print('O valor {} foi adicionado na ultima posição.'.format(valor))
    else:
        pos = 0
        while pos < len(list):
            if valor <= list[pos]:
                list.insert(pos, valor)
                print('O valor {} foi adicionado na {}° posição.'.format(valor, pos+1))
                break
            pos += 1
    print('Lista atual: {}'.format(list))















'''list = []

for c in range(5):
    valor = int(input('\nInsira um valor: '))
    if c == 0:
        list.append(valor)
        print('O valor {} foi adicionado na ultima posição.'.format(valor))
    elif valor >= list[-1]:
        list.append(valor)

        print('O valor {} foi adicionado na ultima posição.'.format(valor))
    elif valor <= list[0]:
        list.insert(0, valor)
        print('O valor {} foi adicionado na 1° posição.'.format(valor))
    elif list[0] < valor <= list[1]:
        list.insert(1, valor)
        print('O valor {} foi adicionado na 2° posição.'.format(valor))
    elif list[1] < valor <= list[2]:
        list.insert(2, valor)
        print('O valor {} foi adicionado na 3° posição.'.format(valor))
    print(list)'''
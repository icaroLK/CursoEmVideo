dec = int(input('Insira um número em decimal: '))
binar = []
while dec // 2 != -1:
    binar.append(dec % 2)
    if dec // 2 == 0 and dec % 2 == 0 and dec == 0:
        break
    dec = dec // 2
print((binar[::-1])[1:])

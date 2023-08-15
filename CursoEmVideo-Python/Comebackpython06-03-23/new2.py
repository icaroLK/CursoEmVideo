dec = int(input('Insira um número em decimal: '))


binar = []
while dec // 2 != -1:
    binar.append(dec % 2)
    if dec // 2 == 0 and dec % 2 == 0 and dec == 0:
        break
    dec = dec // 2
bin = ((binar[::-1])[1:])

qtd = len(bin)
vez = 0

print("O número decimal '{}' em binário é: \033[34m".format(dec), end='')
while vez != qtd:
    print(bin[vez], end='')
    vez += 1

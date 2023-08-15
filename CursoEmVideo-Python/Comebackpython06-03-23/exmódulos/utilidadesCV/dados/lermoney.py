
def leiaDinheiro(msg):
    while True:
        r = input(msg).replace(',','.')
        if r.replace('.','').replace(',','').isnumeric() == True:
            num = float(r)
            break
        else:
            print('\033[31mDADOS INVÁLIDOS.\033[m Tente novamente')
    return num
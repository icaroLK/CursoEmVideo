while True:
    x = int(input('Insira um número: '))

    if x < 0:
        break
    print('\033[1;97m_\033[m' * 12)
    for c in range(1, 10+1):
        print(f'{x} x {c} = {c*x}')
    print('\033[1;97m_\033[m' * 12)

print('\033[31m\nVocê digitou um valor negativo. \nPrograma encerrando...\033[m')

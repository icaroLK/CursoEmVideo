x = int(input('Insira um número: '))
print('\033[1;97m_\033[m'*12)

for m in range(1, 10+1):
    print('{} x {} = {}'.format(m, x, x*m))

print('\033[1;97m_\033[m'*12)

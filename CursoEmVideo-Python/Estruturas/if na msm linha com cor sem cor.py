cem = 4

print('{}{}{} cédulas de \033[32mR$100\033[m'.format('\033[33m' if cem != 0 else '', cem, '\033[m'))





'''if cem == 0:
    print('0 cédulas de \033[32mR$100\033[m')
else:
    print(f'\033[33m{cem}\033[m cédulas de \033[32mR$100\033[m')


print('{}{}{} cédulas de \033[32mR$100\033[m'.format('\033[33m' if cem != 0 else '', cem, '\033[m' if cem != 0 else ''))'''

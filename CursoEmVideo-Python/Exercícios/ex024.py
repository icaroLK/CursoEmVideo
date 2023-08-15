c = str(input('Digite o nome de uma cidade: ')).strip().title()
print('A cidade começa com a palavra "Santo?"? \n{}' .format(c[:5] == 'Santo'))


#outra forma de fazer


'''if 'Santo' in c:
    print('A cidade começa com a palavra "Santo" ')

else:
    print('Nome de bosta')'''

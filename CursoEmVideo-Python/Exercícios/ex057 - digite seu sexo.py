sex = str(input('Insira seu sexo [M/F]: '))

while sex not in 'MF':
    sex = str(input('Tente novamente. '))
    if sex == 'MF':
        sex = str(input('Para d várzea porra mlk digita certo \nTente novamente. '))

print('Sexo {} registrado com sucesso'.format(sex))




#sex = str(input('Insira seu sexo [M/F]: ')).title().strip()[:1]
'''while not sex in 'MF':
    print('Tente novamente.')
    sex = str(input('Insira seu sexo [M/F]: '))

print('Sexo {} registrado com sucesso')'''
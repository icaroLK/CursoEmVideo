from datetime import date
ano = date.today().year
tm = 0
tg = 0
for cu in range(1, 7+1):
    x = int(input('Insira a data de nascimento da {}° pessoa: '.format(cu)))
    if (ano - x) < 18:
        tm += 1

    elif (ano - x) >= 18:
        tg += 1

print('\nExistem {} pessoas com \033[31mmenos\033[m de 18 anos \nExistem {} pessoas com \033[32mmais\033[m de 18 anos'.format(tm, tg))

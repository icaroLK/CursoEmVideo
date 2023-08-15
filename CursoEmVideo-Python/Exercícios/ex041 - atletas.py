from datetime import date

anoatual = date.today().year
a = int(input('Ano de nascimento do atleta: '))
i = anoatual - a
if i <= 9:
    print('O atleta possui {} anos e entrará na classe \033[31mMIRIM\033[m'.format(i))

elif 14 >= i > 9:
    print('O atleta possui {} anos e entrará na classe \033[32mINFANTIL\033[m'.format(i))

elif 19 >= i > 14:
    print('O atleta possui {} anos e entrará na classe \033[33mJUNIOR\033[m'.format(i))

elif 20 >= i > 19:
    print('O atleta possui {} anos e entrará na classe \033[34mSÊNIOR\033[m'.format(i))

elif i > 20:
    print('O atleta possui {} anos e entrará na classe \033[35mMASTER\033[m'.format(i))

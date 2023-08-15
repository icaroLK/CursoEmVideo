ano = int(input('Insira seu ano de nascimento: '))
idade = (2023 - ano)



if idade < 18:
    print('Ainda falta {} anos para você se alistar'.format(18-idade))
if idade == 18:
    print('Você tem que se alistar esse ano.')
if idade > 18:
    print('Seu alistamento ja passou {} anos'.format(idade - 18))
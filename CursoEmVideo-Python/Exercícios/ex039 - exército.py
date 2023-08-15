from datetime import date
anoatual = date.today().year

a = int(input('Insira seu ano de nascimento: '))
idade = anoatual - a

if idade < 18:
    print('Você tem {} anos de idade. Faltam {} anos para você se alistar ao '
          'exército no ano de {}.'.format(idade, 18 - idade, anoatual + (18-idade)))

elif idade == 18:
    print('Você tem {} anos de idade. Chegou sua vez de servir ao exército.'.format(idade))

else:
    print('Você tem {} anos de idade. Já se passaram {} anos da data prevista para se '
          'alistar ao exército no ano de {}.'.format(idade, idade - 18, anoatual - (idade - 18)))

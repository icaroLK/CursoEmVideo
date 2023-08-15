frase = input('Insira uma frase: ').strip().lower().replace(' ','')
if frase == frase[::-1]:
    print('É um palindromo')
else:
    print('Não é um palíndromo')
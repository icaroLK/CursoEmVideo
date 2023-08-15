frase = str(input('Escreva qualquer bosta: ')).strip()

a = int((frase.lower()).count('a'))
prim = int((frase.lower()).find('a'))
ult = int((frase.lower()).rfind('a'))

print("Analizando a frase '{}'".format(frase))
print("A letra 'A' apareceu {} vezes\n"
      "A letra 'A' apareceu pela primeira vez na {}° posição\n"
      "A letra 'A' apareceu pela ultima vez na {}° posição".format(a, prim + 1, ult+1))
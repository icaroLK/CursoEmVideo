n1 = int(input('Digite um número: '))
n2 = int(input('Outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {} \nA multiplicação é {} \nA divisão é {:.3f} \nA divisão inteira ' .format(s, m, d), end=' ')
print('é {} \nA exponenciação é {}' .format(di, e))

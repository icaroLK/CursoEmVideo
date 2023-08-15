from utilidadesCV.moeda import din
from utilidadesCV.dados import lermoney


p = lermoney.leiaDinheiro('Insira o preço: R$')
au = int(input('Insira a % de juros: '))
dim = int(input('Insira a % de desconto: '))

din.resumo(p, au, dim)


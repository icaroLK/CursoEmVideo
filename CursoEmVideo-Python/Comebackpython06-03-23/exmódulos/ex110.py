from utilidadesCV.moeda import din


p = float(input('Insira o preço: R$'))
au = int(input('Insira a % de juros: '))
dim = int(input('Insira a % de desconto: '))

din.resumo(p, au, dim)


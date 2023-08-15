nome = str(input('Insira seu nome: ')).title().strip()

nmai = nome.upper()
nmin = nome.lower()
qtd = len(nome.replace(' ',''))
prim = (nome.split())[0]
qtde1 = nome.find(' ')


print('Segue algumas informações sobre o nome "{0}":\n\n'
      'O nome {0} com as letras maiúsculas fica "{1}"\n'
      'O nome {0} com as letras minúsculas fica "{2}"\n'
      'O nome {0} possui {3} letras sem considerar os espaços\n'
      'Seu primeiro nome ({4}) possui {5} letras'.format(nome, nmai, nmin, qtd, prim, qtde1))
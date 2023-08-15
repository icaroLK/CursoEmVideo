from urllib.request import urlopen

try:
    response = urlopen('http://pudim.com.br/')
    print('Consegui entrar no site do pudim :)')

except:
    print('Não consegui entrar no site do pudim :(')

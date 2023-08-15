def fato(a, show=False):
    """
CALCULADORA DE FATORIAL

    'a' = o número a ser calculado
    'show' = (opcional) mostrar ou não a conta
    'return' = retorna o valor do fatorial de 'a'
    """
    m = 1
    for c in range(a, 0, -1):
        m *= c
        if show == True:
            if c == 1:
                print(c, end=' = ')
            else:
                print(c, end=' x ')
    return m


print(fato(5, show=True))
#help(fato)
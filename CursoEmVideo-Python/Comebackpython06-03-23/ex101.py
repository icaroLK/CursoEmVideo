def title(text):
    print('\033[1m{}\033[m'.format('—')*40)
    print('\033[1m{:^40}\033[m'.format(text))
    print('\033[1m{}\033[m'.format('—')*40)
title('SITUAÇÃO DE VOTO')

def voto(ano):
    from datetime import date
    id = date.today().year - ano
    if id >= 18:
        return f'Com {id} anos: VOTO OBRIGATÓRIO'
    elif 16 <= id < 18 or id > 65:
        return f'Com {id} anos: VOTO OPCIONAL'
    else:
        return f'Com {id} anos: VOTO NEGADO'




resp = int(input('Insira seu ano de nascimento: '))
print(voto(resp))

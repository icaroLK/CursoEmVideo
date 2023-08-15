try:
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('\n\033[31m{}\n{}\033[m\nO erro encontrado foi \033[1;35m{}\033[m\n\033[31m{}\n{}\033[m\n'.format('ERRO '*8, 'ERRO '*8 , erro,'ERRO '*8, 'ERRO '*8 ))
else:
    print('O resultado é {:.1f}'.format(r))
finally:
    print('Thanks my boy')

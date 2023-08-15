from time import sleep

nome = str(input('Olá jovem. Prazer em te conhecer, eu me chamo Skar, sou um duende, daquela espécie que vive nas '
                 'montanhas hahahah você ja deve ter ouvido falar... Enfim, qual é o seu nome rapaz? ')).strip().title()

resp1 = str(input('Muito prazer {}. Bom, estou tentando oferecer esta linda maçã a algúem e você foi o primeiro que '
                  'cruzou meu caminho... Gostaria de receber esse belo presente? '.format(nome))).strip().title()
if 'Sim' in resp1:
    print('\nMuitíssimo obrigado garoto. Agora este fardo não está mais sobre minhas costas... HAHHAHHAHAHA')
    sleep(1.8)
    print('\033[1;97m*O duende sai correndo e se enfia em um buraco*\033[m')
    sleep(1.4)
    print('\033[1;97m*Você se sente meio enjoado mas melhora em seguida. Depois de alguns segundos você percebe que '
          'adiquiriu superpulo...\033[m')
    pulo = str(input('Você quer pular? ')).strip().title()
    if 'Sim' in pulo:
        print('\033[1;97m*Você pula tão alto que não consegue sobreviver a queda e \033[1;31mmorre\033[m \033[1;97mao tocar '
              'o chão*\033[m')
    elif pulo in 'Não Nao':
        print('\033[1;97m*Você decide nunca mais pular e simplesmente segue seu caminho...\033[m')

elif resp1 in 'Não Nao':
    print('Seu verme! Eu lhe ofereço um presente e é assim que você retribui? Isso não ficará barato')
    sleep(1.8)
    print('\033[1;97m*O duende tira uma faca do bolso e corre em sua direção*\033[m')
    d = str(input('Você decide correr ou lutar? ')).strip().title()
    if 'Lutar' in d:
        print('\033[1;97m*Apesar de seu tamanho, o duende possui uma força extraordinária e te mata com pouco '
              'esforço.*\033[m')
    elif 'Correr' in d:
        print('\033[1;97m*Você corre e consegue fugir do duende. Pouco tempo depois ele desiste e se enfia em um '
              'buraco na floresta*\033[m')

elif '' in resp1:
    print('\033[1;31mSeu bastardo inútil.\033[m')
    print('\033[1;97m*O duende grita e corre para dentro da floresta...*\033[m')




#print('\033[1;97m*')
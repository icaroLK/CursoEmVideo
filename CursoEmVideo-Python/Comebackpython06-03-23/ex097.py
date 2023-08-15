def title(msg):
    print('\033[1m{}\033[m'.format('—')*(len(msg)+4))
    print('\033[1m  {:.^}  \033[m'.format(msg))
    print('\033[1m{}\033[m'.format('—')*(len(msg)+4))


title('Bucetinha')
title('OI caralhgo')
title('rolinha dura e coisaradaaaaaaa')
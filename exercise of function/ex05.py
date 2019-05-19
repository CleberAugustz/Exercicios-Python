n = str(input('Digite seu nome:\n')).title()
f = str(input('Deseja digitar sua idade?:\n')).lower()
def dados(n,f):
    if f == 'sim':
        f = int(input('Qual sua idade?\n'))
        print('Olá {}, você tem {} anos, Seja Bem-Vindo'.format(n,f))
    else:
        print('Olá {}, Seja Bem-Vindo'.format(n))
dados(n,f)
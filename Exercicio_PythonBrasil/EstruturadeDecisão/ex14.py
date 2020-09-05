n1 = int(input('Digite sua primeira nota:\n'))
n2 = int(input('Digite sua segunda nota:\n'))
m = (n1+n2)/2
if m >= 6:
    print('Você foi aprovado')
    print('Suas notas são {} e {}, sua média é {}'.format(n1,n2,m))
    if m > 6 and m <= 7.5:
        print('E seu conceito é C')
    elif m > 7.5 and m <= 9:
        print('Seu Conceito é B')
    elif m > 9 and m <= 10:
        print('Seu Conceito é A')
elif m >= 4 and m < 6:
    print('Você foi reprovado')
    print('Suas notas são {} e {}, sua média é {}'.format(n1,n2,m))
    if m > 4 and m <= 6:
        print('E seu conceito é D')
    elif m > 0 and m <= 4:
        print('Seu Conceito é E')
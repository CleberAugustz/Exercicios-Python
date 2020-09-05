d = input('Digite o dia:\n')
m = input('Digite o mês:\n')
a = input('Digite o ano:\n')
s = m > '12'
s1 = d > '31'
s2 = a.isnumeric() and m.isnumeric() and d.isnumeric()
if s2 is False:
     print('Por Favor, Não use vírgula/ponto ou qualquer outra caractere que não seja números.')
elif s1 is True:
    print('Você digitou o dia inválido.')
elif s is True:
    print('Você digitou um mês inválido')
else:
    print('{}/{}/{}'.format(d,m,a))
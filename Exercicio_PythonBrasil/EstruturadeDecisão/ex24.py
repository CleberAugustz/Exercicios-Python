v = input('Digite um número:\n')
v2 = input('Digite outro número:\n')
q = str(input('O que você deseja fazer com esses núneros?;\n1-Somar\n2-Subtrair\n3-Saber se é par ou impar\n4-Saber se é positivo ou negativo\nOu 5-se é inteiro ou Decimal\n???\n')).lower()

if not v2.isnumeric() and v.isnumeric() and v2.isdecimal() and v.isdecimal():
    print('Por favor, use apenas números.')
elif q == '1':
    i = float(v)
    i2 = float(v2)
    r = i+i2
    print('O resultado da soma de {} mais {} é igual a {}'.format(v,v2,r))
elif q == '2':
    i = float(v)
    i2 = float(v2)
    r = i-i2
    print('O resultado da subtração de {} menos {} é igual a {}'.format(v,v2,r))
elif q == '3':
    i = int(v)
    i2 = int(v2)
    r = (i+i2)%2
    print(r)
    if r > 0:
        print('Impar')
    if r == 0:
        print('Par')
elif q == '4':
    m = v and v2 > '0'
    if m is True:
        print('Positivo')
    if m is False:
        print('Negativo')
elif q == '5':
    r = v.isdecimal() and v2.isdecimal()
    if r is True:
        print('Decimal')
    if r is False:
        print('Inteiro')
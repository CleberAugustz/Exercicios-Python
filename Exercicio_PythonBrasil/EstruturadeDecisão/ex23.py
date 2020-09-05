n = input('Digite um número')
v = n.isdecimal()
if v is True:
    print('É Decimal')
else:
    print('É um número inteiro.')
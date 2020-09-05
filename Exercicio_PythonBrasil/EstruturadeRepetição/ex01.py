n = 25
while n:
    if n not in range(0,11):
        n = int(input('Por Favor, Digite um valor de 0 a 10:\n'))
    if n in range(0,11):
        print('Você Digito um valor válido')
        break
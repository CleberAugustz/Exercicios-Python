l = int(input('Digite quantos litros de combústivel deseja:\n'))
t = str(input('Gasolina ou Álcool?\n')).lower()

if t == 'gasolina':
    if l < 20:
        p = (2.50*l)*0.96
        print(p)
    elif l >= 20:
        p = (2.50*l)*0.94
        print(p)
elif t == 'álcool':
    if l < 20:
        p = (1.90 * l) * 0.97
        print(p)
    elif l >= 20:
        p = (1.90 * l) * 0.95
        print(p)
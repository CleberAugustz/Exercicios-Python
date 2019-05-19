

def indeterminado():
    q = int(input('Quantos parâmetros deseja declarar:\n'))
    r = list(range(1,q))
    global primos
    primos = []
    for i in r:
        b = i/i
        if (b == 0):
            primos = i
        print(primos)
indeterminado()

print(primos)

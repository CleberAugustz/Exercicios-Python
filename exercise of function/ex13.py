palavra = str(input('Digite a palavra que deseja ivnerter:\n'))


def invertendo():
    b = 0
    global invertida
    invertida = []
    while (-b < len(palavra)):
        b -= 1
        invertida.append(palavra[b])
invertendo()

def transformando():
    global stringinvertida
    stringinvertida = ''
    for i in invertida:
        stringinvertida = stringinvertida + i

transformando()
print('Antes de inverter: {}'.format(palavra))
print('Depois de invertida: {}'.format(stringinvertida))
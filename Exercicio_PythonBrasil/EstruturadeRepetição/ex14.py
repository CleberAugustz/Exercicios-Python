w = 0
i = 0
n = list(range(1,11))
for idx,value in enumerate(n):
    d = int(input('Digite um valor:\n'))
    r = d%2
    if r == 0:
        w += 1
        print(w)
    if r > 0:
        i += 1
        print(i)
print('Você digitou, {} numeros pares'.format(w))
print('Você digitou, {} numeros impares'.format(i))
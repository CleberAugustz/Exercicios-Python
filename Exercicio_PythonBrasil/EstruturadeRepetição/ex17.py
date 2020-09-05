n = int(input('Digite o valor que deseja saber o Fatorial:\n'))
l = list(range(n,0,-1))
print(l)
fatoriais = [0,1]
b = 1
lista = []
for fatorial,item in enumerate(l):
    b *= (fatorial+1)
    print(b)
    lista.append(b)
print(lista)
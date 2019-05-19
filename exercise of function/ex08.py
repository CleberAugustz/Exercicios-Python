q = int(input('Quantos parâmetros deseja declarar?\n'))
n = list(range(0,q))
for key,value in enumerate(n):
    n[key] = input('Digite o parâmetro:\n')
z = zip((n),(list(range(0,q))))
def lista():
    l = dict(z)
    print(l)
lista()

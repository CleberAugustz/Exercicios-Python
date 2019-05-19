lista = [1,2,3,4,5,6,7,8,9]

def pares():
    global par
    par = []
    for i in lista:
        if (i%2 == 0):
            par.append(i)
        print(par)
pares()
print(par)
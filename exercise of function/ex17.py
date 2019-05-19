lista = [3,4,22,12,45,22,22,75,78,75,78,78]
lista.sort()
print(lista)

def semrepetir():
    global semrep
    a = 0
    semrep = []
    for i in lista:
        a += 1
        if (i == lista[-1]):
            semrep.append(i)
            break
        if (i != lista[a]):
            semrep.append(i)
        print(semrep)

semrepetir()

print(semrep)
#coding: utf-8

__author__ = 'Cleber Augusto'

########################
#### Cleber Augusto ####
########################
print("Determine o intervalo")
det = int(input("Valor Inicial:\n"))
det2 = int(input("Valor Final:\n"))
l = []
for a in list(range(det,det2)):
    x = 0
    for b in (2,3,5,7,11):
        c = a%b
        if c>1:
            x += 1
        if c == 0:
            x -= 1
    if (x>1):
        l.append(a)
print(l)

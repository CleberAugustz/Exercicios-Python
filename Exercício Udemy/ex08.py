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
    c2 = a%2
    if a==0:
        continue
    if c2==0:
        continue
    for b in range(a-1, 0, -1):
        if(a%b == 0):
            break
        if(a%b > 0):
            if(b==2):
                l.append(a)

print("Determine os 3 valores a serem excluidos")
a1 = int(input("Valor 1:\n"))
a2 = int(input("Valor 2:\n"))
a3 = int(input("Valor 3:\n"))

if a1 in l:
    l.remove(a1)
if a2 in l:
    l.remove(a2)
if a3 in l:
    l.remove(a3)
print(l)

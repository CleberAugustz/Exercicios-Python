#coding: utf-8

__author__ = 'Cleber Augusto'

########################
#### Cleber Augusto ####
########################

l = []
for a in list(range(1,101,2)):
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

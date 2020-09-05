#coding: utf-8

__autor__ = 'Cleber Augusto Dias Da Silva'

#Números Primos

print('Descubra se um número é primo!!')
n = int(input('Digte o número que deseja saber:\n'))

l = [2,3,5,7,9,11]
b = 0
for idx,item in enumerate(l):
    x = n%l[idx]
    if x == 0:
        b += 1
if b == 0 :
    print('é primo')
if b > 0:
    print('Não é primo')


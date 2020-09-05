#coding: utf-8

__autor__ = 'Cleber Augusto Dias Da Silva'

#Números Primos + saber por quais ele é divisível

print('Descubra se um número é primo!!')
n = int(input('Digte o número que deseja saber:\n'))

l = [2,3,5,7,9,11]
b = 0
ap = []
for idx,item in enumerate(l):
    x = n%l[idx]
    if x == 0:
        b += 1
        ap.append(item)
if b == 0 :
    print('é primo')
if b > 0:
    print('Não é primo')
    print('e é divisível pelos seguintes valores,\n{}'.format(ap))
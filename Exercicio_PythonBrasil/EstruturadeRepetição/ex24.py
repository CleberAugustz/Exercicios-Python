#coding: utf-8

__autor__ = 'Cleber Augusto Dias Da Silva'


n = int(input("Digite o número de fatores:\n"))
n1 = 0
range(1,n,1)
for i,i2 in enumerate(range(1,n+1,1)):
    n1 += i2

print('O total é {}, a média é {:.1f} e a quantidade de fatores é {}'.format(n1,n1/n,n))

#coding: utf-8

__author__ = 'Cleber Augusto Dias Da Silva'

########################
#### Cleber Augusto ####
########################

d = input('Deternime a quantidade de números:\n')
inteiro = int(d)
string = str(d)
l = list(range(inteiro+1))
def soma(x):
    for idx, item in enumerate(l):
        x += idx
    print('A soma dos valores é {}'.format(x))

soma()
print('Maior valor é {}'.format(l[-1]))
print('Menor valor é {}'.format(l[1]))

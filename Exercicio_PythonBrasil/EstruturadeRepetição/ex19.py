#coding: utf-8

__author__ = 'Cleber Augusto Dias Da Silva'

########################
#### Cleber Augusto ####
########################
try:
    def introducao():
        global inteiro, string, l, d
        d = input('Deternime a quantidade de números:\n')
        inteiro = int(d)
        string = str(d)
        l = list(range(inteiro+1))
    introducao()

    def permitido():
            print('Por Favor, Determine uma quantia até 1000')
            introducao()
    if inteiro > 1000:
        permitido()
    def soma():
        b = 0
        for idx, item in enumerate(l):
            b += idx
        print('A soma dos valores é {}'.format(b))

    soma()
    print('Maior valor é {}'.format(l[-1]))
    print('Menor valor é {}'.format(l[1]))
except:
    print('Por Favor, Use apenas números inteiros!')

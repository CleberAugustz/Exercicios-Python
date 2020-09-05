#coding: utf-8
__author__ = 'Cleber Augusto'

def re():
    a = str(input('Deseja iniciar novamente?\n[SIM] ou [NÃO]\n')).lower()
    if a == 'sim':
        begin2()
def begin2():
    try:
        print('Escolha entre 1 à 16')
        n = int(input('Digite o valor que deseja saber o Fatorial:\n'))
        if n > 0 and n < 16:
            l = list(range(n, 0, -1))
            fatoriais = [0, 1]
            b = 1
            lista = []
            for fatorial, item in enumerate(l):
                b *= (fatorial + 1)
                lista.append(b)
            print(lista)
        else:
            print('Por Favor, digite um valor entre 1 e 16!!!')
            begin2()
        re()
    except:
        print('Por Favor, utilize apenas números inteiros!')
        begin2()
begin2()
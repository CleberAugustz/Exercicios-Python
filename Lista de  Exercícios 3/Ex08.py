#8) Faça um algoritmo que imprima os valores no intervalo definido pelo usuário e permita que o mesmo possa definir 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela:
i = int(input('Digite o número inicial'))
f = int(input('Digite o número final'))
intervalo = int(input('Digite o Intervalo'))
d1 = int(input('Digite um valor à ignorar'))
d2 = int(input('Mais um valor'))
d3 = int(input('Mais outro valor'))
for s in range(i,f,intervalo):
    if(s == d1 or s == d2 or s == d3):
        continue
    else:
        print(s)




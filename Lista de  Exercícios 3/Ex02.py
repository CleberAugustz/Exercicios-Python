#2) Evolua o algoritmo no qual imprimimos os números num intervalo pré-definido para um algoritmo que pergunte ao usuário qual o intervalo que o mesmo deseja que seja impresso

import time
print('Digite o valor que você quer que inicie a contagem\ne o valor que termine e qual o espaço (1 em 1, 2 em 2, 3 em 3)')
i = int(input('Valor Inicial:\n'))
f = int(input('Valor Final:\n'))
q = int(input('Quantidade de espaço:\n'))
print(list(range(i, f, q)))
print('')
'''i = 0
while i<=99:
    i += 1
    print(i)'''
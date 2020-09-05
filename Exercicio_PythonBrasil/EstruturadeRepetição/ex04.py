a = 80.000
b = 200.000
anos = 0
qua = 0
while True:
    a += a*0.03
    b += b*0.015
    qua += 1
    if a >= b:
        print('A cidade A levará {} anos para alcançar a quantidade de habitantes de cidade B'.format(qua))
        break

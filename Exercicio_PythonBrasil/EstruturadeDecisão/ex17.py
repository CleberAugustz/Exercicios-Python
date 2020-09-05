a = int(input('Digite o ano:\n'))
t1 = a%4
t2 = a%100
t3 = a%400
if t1 == 0:
    if t2 == 0:
        print('não é bissexto')
    else:
        print('É bissexto')
elif t3 != 0:
    print('Não é bissexto')

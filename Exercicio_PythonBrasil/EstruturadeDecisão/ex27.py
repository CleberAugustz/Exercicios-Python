m = int(input('Quantos Kg de Morango, deseja comprar?\n'))
m1 = int(input('Quantos Kg de Maçã, deseja comprar?\n'))
m2 = m+m1
if m2 <= 5:
    r = m * 2.5
    r2 = m1 * 1.8
    r3 = r+r2
    print('Você irá pagar R${:.2f}'.format(r3))
elif m2 > 5:
    r = m * 2.2
    r2 = m1 * 1.5
    r3 = r+r2
    if m2 >= 8:
        r4 = r3 * 0.90
        print('Como você é um cliente especial, darei a você 10% de desconto OK?')
        print('Você irá pagar R${:.2f}'.format(r4))
    else:
        print('Você irá pagar R${:.2f}'.format(r3))
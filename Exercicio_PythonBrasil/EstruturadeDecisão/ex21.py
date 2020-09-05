s = int(input('Olá.\nDigite o valor do saque desejado:\nOBS: Valor minímo de R$10.00\n'))
u = s//1%10
d = s//10%10
c = s//100%10
m = s//1000%10
print('O valor solicitado para saque é tanto \033[0;32;0mR${}\033[m\nSerá imprimido com as seguintes notas!!'.format(s))
if u > 0:
    v5 = u//5
    if u == 5:
        print('{:.0f} Nota de R$5'.format(v5))
    if u > 5:
        v15 = u-5
        print('{:.0f} Nota de R$5'.format(v5))
        print('{:.0f} Notas de R$1'.format(v15))
    if u < 5:
        print('{:.0f} Notas de R$1'.format(u))
if d > 0:
    v50 = d//5
    if d == 5:
        print('{:.0f} Nota de R$50'.format(v50))
    if d > 5:
        v150 = d-5
        print('{:.0f} Nota de R$50'.format(v50))
        print('{:.0f} Notas de R$10'.format(v150))
    if d < 5:
        print('{:.0f} Notas de R$10'.format(d))
if c > 0:
    print('{:.0f} Nota de R$100'.format(c))
ap = int(input('Digite a medida em metros quadrados a ser pintada:\n'))
g = ap//(18*6)+1
print(g)
p = ap//(3.6*6)+1
print(p)
vp = p*25
vg = g*80
g1 = ap/(18*6)#Terceiro elemento de calculo
print(g1)
g2 = ((ap/(18*6))-(ap//(18*6)))/21.6#Terceiro elemento de calculo
print(g2)
g3 = (g1+1)*80#Valor a pagar pela lata grande
print(g3)
g4 = g2*25#Valor a pagar pela lata pequena
print(g4)
# print('Você irá usar {} latas de 18 Litros de tintas e o valor a ser pago é R${}'.format(g,vg))
# print('Você irá usar {} latas de 3.6 Litros de tinta e o valor a ser pago é R${}'.format(p,vp))
# print('Você irá usar {} Latas de 18 litros e {} latas de 3.6, o total a pagar é {}'.format(g1,g2,g3+g4))

ap = int(input('Digite a medida em metros quadrados a ser pintada:\n'))
total = ap//54+1
v = total*80
print('Você irá usar {} latas de tintas e o valor a ser pago é R${}'.format(total,v))

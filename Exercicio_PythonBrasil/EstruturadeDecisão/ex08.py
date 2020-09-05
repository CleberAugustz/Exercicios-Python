p1 = float(input('Digite o valor do primeiro Preço:\n'))
p2 = float(input('Digite o valor do segundo Preço:\n'))
p3 = float(input('Digite o valor do terceiro Preço:\n'))
if p1 <= p2 and p1 <= p3:
    print('O menor preço é',p1)
if p2 <= p3 and p2 <= p1:
    print('O menor Preço é',p2)
if p3 <= p2 and p3 <= p1:
    print('O menor Preço é',p3)
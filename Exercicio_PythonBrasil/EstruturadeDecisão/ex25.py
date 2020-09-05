p1 = str(input('Telefonou para Vítima?\n')).lower()
p2 = str(input('Esteve no local do crime?\n')).lower()
p3 = str(input('Mora perto da Vítima?\n')).lower()
p4 = str(input('Devia para Vítima?\n')).lower()
p5 = str(input('Já trabalhou com a Vítima?\n')).lower()
print('Responda apenas SIM ou NÃO.\n Caso responda qualquer outra informação será desconsiderada.')

tt = 0
if p1 == 'sim':
    tt += 1
if p2 == 'sim':
    tt += 1
if p3 == 'sim':
    tt += 1
if p4 == 'sim':
    tt += 1
if p5 == 'sim':
    tt += 1
if tt < 2:
    print('Te retornaremos!')
if tt == 2:
    print('Suspeito')
if tt > 2 and tt < 4:
    print('Cumplice')
if tt == 5:
    print('Assassino')
print(tt)
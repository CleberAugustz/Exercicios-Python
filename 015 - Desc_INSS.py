gh = int(input('Quanto você ganha por Hora?\n'))
ht = int(input('Quantas horas você trabalha por mês?\n'))
d = ((((gh*ht)*0.89)*0.92)*0.95)
print('Seu salário bruto é {}. Descontando IR, INSS, Sindicado, seu salário será {:.2f}'.format(ht*gh,d))

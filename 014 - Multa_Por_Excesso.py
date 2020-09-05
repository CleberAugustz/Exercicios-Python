p = int(input('Quantos Kg de peixes você está carregando joão?:\n'))
if p >= 50:
    excesso = p-50
    multa = (p-50)*4.00
    print(excesso,multa)
    print('João, você está carregando uma quantidade de peixes maior que o permitido')
    print('O permitido é até 50KG, você está carregando {}Kg a mais.'.format(excesso))
    print('Você irá pagar uma multa de R${}'.format(multa))
else:
    print('Parabéns Sr João, você está dentro das normas.')

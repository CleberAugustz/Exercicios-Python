t = str(input('Digite o turno que você estuda\nSeguindo a seguinte orientação\nM Para Matutino - V Para Vespertino - N Para Norturno\n')).lower()
if t in 'm':
    print('Você estuda no turno Matutino')
elif t in 'v':
    print('Você estuda no turno Vespertino')
elif t in 'n':
    print('Você estuda no turno Norturno')
else:
    print('Você digitou um comando Inválido')
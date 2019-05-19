h = float(input('Digite sua altura:\n'))
g = str(input('Você é Homem ou Mulher?\n')).rstrip().lower()
print(g)
if g == 'homem':
    print('Seu peso ideal baseado na sua altura é {}'.format((72.7*h)-58))
if g == 'mulher':
    print('Seu peso ideal baseado na sua altura é {}'.format((62.1*h)-44.7))
if g != 'mulher' and 'homem':
    print('Você digitou um dado inválido. Por favor, verifique e tente novamente.')
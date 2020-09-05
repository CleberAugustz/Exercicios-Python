#9) Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra. Caso a letra seja o "q" finalize a aplicação. Do contrário, imprima novamente a mesma frase até que o caractere "q" seja enviado:
s = 0
while s != 'q':
    print('Estou em Looping')
    s = str(input('Digite q para sair:\n')).lower()
    if s == 'q':
        break
palavra = str(input('Digite uma palavra:\n')).lower()

def verifica():
    if (palavra == palavra[::-1]):
        print('A palavra é Palindromo!')
    else:
        print('A palavra não é Palindromo!')
verifica()
t = str(input('Digite uma letra:\n')).lower()
lista = ['a','e','i','o','u']
if t in lista:
    print('Você digitou uma vogal')
else:
    print('Você digitou uma consoante')
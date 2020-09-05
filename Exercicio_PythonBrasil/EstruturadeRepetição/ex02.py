n = input('Digite seu nome:\n')
p = input('Digite a senha:\n')
while n == p:
    print('Por Favor, não digite a sua senha igual a seu nome')
    p = input('Digite a senha;\n')
    if n != p:
        print('Login Efetuado')
        break

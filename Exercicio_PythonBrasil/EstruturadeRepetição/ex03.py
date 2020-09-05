n = str(input('Digite seu nome: (MAIOR QUE 3 CARACTERES)\n'))
i = int(input('Digite sua idade:\n'))
s = float(input('Digite seu salário:\n'))
g = input('Digite seu Sexo: (f-Feminino ou m-Masculino)\n')
e = input('Estado Civil: (s-Solteiro,c-Casado,v-Viúvo,d-Divorciado')
while len(n) <= 3:
    n = str(input('Por Favor, Digite um nome maior que 3 Letras!!!'))
    if len(n) > 3:
        break
while i < 0 or i > 150:
    i = int(input('Por Favor, Digite uma idade de 0 a 150'))
    if i > 0 and i < 150:
        break
while s:
    if s > 0:
        break
    s = float(input('Digite seu salário:\n'))

while g:
    if g == 'f':
        g = 'Feminino'
        break
    if g == 'm':
        g = 'Masculino'
        break
    g = input('Digite seu Sexo: (f-Feminino ou m-Masculino)\n')
while e:
    if e == 's':
        e = 'Solteiro'
        break
    if e == 'c':
        e = 'Casado'
        break
    if e == 'v':
        e = 'Viúvo'
        break
    if e == 'd':
        e = 'Divorciado'
        break
    e = input('Estado Civil: (s-Solteiro,c-Casado,v-Viúvo,d-Divorciado')
print('Thank so much, Question Finish')
print(n,i,s,g,e)
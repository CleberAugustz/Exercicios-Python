n1 = int(input('Digite sua primeira nota:\n'))
n2 = int(input('Digite sua segunda nota:\n'))
m = (n1+n2)/2
if m >= 7:
    print('Você foi aprovado')
elif m < 7:
    print('Você foi reprovado')
if m == 10:
    print('Uauuu!!!! Você foi aprovado com distinção!')
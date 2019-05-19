try:
    def start():
        global d, d2, d3
        d = int(input('Digite valor onde iniciará o intervalo:\n'))
        d2 = int(input('Digite valor onde terminará o intervalo:\n'))
        d3 = int(input('Digite valor que deseja verificar:\n'))
    start()

    def r(x,y):
        global intervalo
        intervalo = list(range(x,y))
    r(d,d2)

    def pertence(x):
        if d3 in x:
            print('O número está presente no intervalo determinado.')
        else:
            print('Não está presente no intervalo determinado.')
    pertence(intervalo)

except:
    print('='*10,'Opss, Ocorreu um erro','='*10)
    print('Utilize apenas números inteiros')
    print('Recomece o procedimento')
    start()
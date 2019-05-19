n = list(range(1,4))
def coleta():
    try:
        for idx,item in enumerate(n):
            n[idx] = int(input('Digite o {}º Valor:\n'.format(n[idx])))
    except:
        print('Digite apenas numeros inteiros.')
        coleta()
coleta()
def maior():
    n.sort()
    return(n[-1])
maior()

print(maior())

q = int(input('Quantas palavras deseja digitar?\n'))
n = list(range(0,q,1))
for idx,item in enumerate(n):
    n[idx] = str(input('Digite o {}º nome desejado:\n'.format(n[idx]+1)))
def lista(n):
    print(n)
lista(n)
n = [1, 2, 3]
for idx, item in enumerate(n) :
    n[idx] = int(input('Digite um número:\n'))
    print(n)
def media(x,y,z):
    m = (x+y+z)/len(n)
    print('A média é {:.1f}'.format(m))
media(**dict(zip(('x','y','z'), n)))
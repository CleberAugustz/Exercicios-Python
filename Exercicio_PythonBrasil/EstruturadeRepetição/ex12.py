n1 = int(input('Digite o valor que deseja saber a tabuada:\n'))
n = list(range(0,11))
for idx,item in enumerate(n):
    d = idx*n1
    print('{} * {} = {}'.format(n1,idx,d))

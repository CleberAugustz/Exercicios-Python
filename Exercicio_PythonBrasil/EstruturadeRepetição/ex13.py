n1 = int(input('Digite um número:\n'))
n2 = int(input('Digite outro número:\n'))
r = list(range(1,n2))
d = n1
for idx,item in enumerate(r):
    d = d*n1
    print(d)
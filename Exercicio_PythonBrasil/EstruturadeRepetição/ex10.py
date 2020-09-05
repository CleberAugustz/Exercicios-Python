n1 = [0,0]
for idx,item in enumerate(n1):
    n1[idx] = int(input('Digite um valor:'))
n1.sort()
s = list(range(n1[0],n1[1]+1))
print(s)

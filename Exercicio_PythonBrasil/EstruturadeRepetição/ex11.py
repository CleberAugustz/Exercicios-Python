n1 = [0,0]
for idx,item in enumerate(n1):
    n1[idx] = int(input('Digite um valor:\n'))
n1.sort()
s = n1[0]+n1[1]
print(s)
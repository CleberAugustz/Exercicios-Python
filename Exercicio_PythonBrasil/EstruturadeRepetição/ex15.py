n = int(input('Quantos Termos Deseja?\n'))
l = list(range(0,n))
total = []
b = 0
lili = [0,]
print(b)
for idx,item in enumerate(l):
    if b > l[-1]:
        print(lili)
        break
    if idx <= 1:
        b = 1
        lili.append(b)
        print(b)
    if idx > 1:
        b += lili[-2]
        lili.append(b)
        print(b)

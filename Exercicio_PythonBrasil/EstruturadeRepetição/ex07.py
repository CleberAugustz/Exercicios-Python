
n = [0,0,0,0,0]
for idx, item in enumerate(n):
    n[idx] = int(input('Digite um valor:\n'))
n.sort()
print(idx,item)
print(n)
print('O maior numero é {}'.format(n[-1]))






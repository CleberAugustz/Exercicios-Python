n = [0,0,0,0,0]
for idx,item in enumerate(n):
    n[idx] = int(input('Digite um valor:\n'))
r = 0
for idx, item in enumerate(n):
    r += n[idx]
m = r/5
print('A soma dos numeros digitados é {} e a média é {}'.format(r,m))

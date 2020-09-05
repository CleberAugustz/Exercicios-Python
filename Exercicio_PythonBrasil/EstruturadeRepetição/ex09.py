rang = list(range(1,52))
for idx, item in enumerate(rang):
    t = rang[idx]%2
    if t == 1:
        print(idx)
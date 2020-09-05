i = int(input('Digite O intervalo'))
for s in range(0,100):
    for j in range(s-1,0,-i):
        if(s%j == 0):
            break
        if(s%j > 0):
            if(j==2):
                print(s)
    if(s==2):
        print(s)
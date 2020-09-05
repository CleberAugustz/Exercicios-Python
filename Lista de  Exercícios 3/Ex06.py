#6) Faça um algoritmo que imprima os números primos entre 0 e 100:
for i in range(0,100):
    for j in range(i-1,0,-1):
        if(i%j == 0):
            break
        if(i%j > 0):
                if(j==2):
                    print(i)
    if(i==2):
        print(i)


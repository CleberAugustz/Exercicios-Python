num = int(input('Digite um número inteiro para saber seu fatorial:\n'))
r = list(range(1,num))
def fatorial():
    global num
    for i in r:
        num *= i
fatorial()
print(num)
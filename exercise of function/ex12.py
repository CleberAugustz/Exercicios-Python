l = 1,2,3,4,5
def multiplica():
    global l
    global idx
    global item
    global n
    n = 1
    for idx,item in enumerate(l):
        n = n * l[idx]
        print(n)
multiplica()


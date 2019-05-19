def func1():
    def func2():
        x = int(input('Digite um valor:\n'))
        y = int(input('Digite outro valor:\n'))
        global r
        r = x+y
    func2()
    print(r)
func1()
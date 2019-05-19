palavra = str(input('Digite uma palavra:\n'))
print(palavra)

def convert():
    a = 0
    global string
    string = []
    while (a < len(palavra)):
        a += 1
        print(a)
        string.append(palavra[a-1])
        print(string)
convert()
print(string)

def separar():
    global maiuscula
    global minuscula
    global list1
    global list2
    minuscula = 0
    maiuscula = 0
    list1 = ''
    list2 = ''
    for i in string:
        if (i.isupper()):
            maiuscula += 1
            list1 += i
        if (i.islower()):
            minuscula += 1
            list2 += i
separar()

print('No seu texto tem {} Maiúsculas, sendo ({}), e {} Minúsculas, sendo ({})'.format(maiuscula,list1,minuscula,list2))


n1 = int(input('Digite um número:\n'))
n2 = int(input('Digite outro número:\n'))
n3 = int(input('Digite outro número:\n'))
if n1 >= n2 and n1 >= n3:
    print('O número maior é',n1)
if n2 >= n1 and n2 >= n3:
    print('O número maior e',n2)
if n3 >= n1 and n3 >= n2:
    print('O número maior é',n3)
if n1 <= n2 and n1 <= n3:
    print('O menor número é',n1)
if n2 <= n3 and n2 <= n1:
    print('O menor número é',n2)
if n3 <= n2 and n3 <= n1:
    print('O menor número é',n3)
#coding: utf-8

__autor__ = 'Cleber Augusto Dias Da Silva'

q = int(input("Quanto alunos há na classe?\n"))
a = 0
for i in enumerate(range(1,q,1)):
    a += int(input("Qual é a idade deles?\n Digite uma por vez.\n"))
m = a/q
i = ""
if m < 25:
    i = "Jovem"
elif m > 25 and m < 60:
    i = "Adulta"
elif m > 60:
    i = "Idosa"
print("São {} Alunos, a média de idade é {:.0f}, A sala é considerada {}".format(q,m,i))


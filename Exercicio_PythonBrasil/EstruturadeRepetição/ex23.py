#coding: utf-8

__autor__ = 'Cleber Augusto Dias Da Silva'
#
# #Números Primos
# print('Descobrindo se um número é primo!!')
# n = int(input('Digte o último número da lista que deseja saber quais são primos:\n'))
# l1 = list(range(0,n+1))
# l = [2,3,5,7,9,11]
# b = 0
# primos = []
# nprimos = []
# for idx,item in enumerate(l1):
#     for idx1,item1 in enumerate(l):
#         x = l1[idx]%l[item1]
#         if x == 0:
#             b += 1
#             nprimos.append(item)
#         if x == 1:
#             primos.append(item)
# print(primos)
# print(nprimos)
# if b == 0 :
#     print('é primo')
#     print(primos)
# if b > 0:
#     print('Não é primo')
#     print(nprimos)


# MÉTODO CRIVO DE ERATÓSTENES
import math

# Input: an integer n > 1.
N = int(input("N: "))

# Let A be an array of Boolean values, indexed by integers 2 to n, initially all set to true.
A = list(range(2, N))
print((2, int(math.sqrt(N)+1)))
# for i = 2, 3, 4, ..., not exceeding √n:
for i in range(2, int(math.sqrt(N)+1)):

  # if A[i] is true:
  if i in A:

    # for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n:
    for j in range(i**2, N, i):

      # A[j] := false.
      if j in A:
          A.remove(j)

# Output: all i such that A[i] is true.
print(A)
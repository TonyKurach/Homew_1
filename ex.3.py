
# Даны три числа a, b и c. Найти среднее геометрическое этих чисел, если они все отличны от нуля, и среднеарифметическое
# в противном случае

import random

a = random.randint(0, 10)
print("Значение числа a:")
print(a)
b = random.randint(0, 10)
print("Значение числа b:")
print(b)
c = random.randint(0, 10)
print("Значение числа c:")
print(c)
A = []
B = []
if a != 0:
    A.append(a)
else:
    B.append(a)
if b != 0:
    A.append(b)
else:
    B.append(b)
if c != 0:
    A.append(c)
else:
    B.append(c)
f = len(A)
g = len(B)
print("Значения элементов списка А: ")
for i in range(f):
    print(A[i])
k = 1
for i in range(f):
    k *= A[i]
m = k ** (1/f)
print("Среднее геометрическое элементов списка А: " + str(m))
print("Значения элементов списка B: ")
for j in range(g):
    print(B[j])
p = sum(B)
w = p/g
print("Среднее арифметическое элементов списка B: " + str(w))
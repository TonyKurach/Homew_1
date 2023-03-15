
# Определить, есть ли среди заданных целых чисел A, B, C, D хотя бы одно нечетное

import random

A = random.randint(-10, 10)
print("Число А - имеет следующее значение:")
print(A)
if A % 2 == 0:
    print("Число А - четное число")
else:
    print("Число A - нечетное число")
B = random.randint(-10, 10)
print("Число B - имеет следующее значение:")
print(B)
if B % 2 == 0:
    print("Число B - четное число")
else:
    print("Число B - нечетное число")
C = random.randint(-10, 10)
print("Число C - имеет следующее значение:")
print(C)
if C % 2 == 0:
    print("Число C - четное число")
else:
    print("Число C - нечетное число")
D = random.randint(-10, 10)
print("Число D - имеет следующее значение:")
print(D)
if D % 2 == 0:
    print("Число D - четное число")
else:
    print("Число D - нечетное число")

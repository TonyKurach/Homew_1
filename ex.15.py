import random

# Определить, есть ли среди заданных целых чисел A, B, C, D хотя бы одно четное

A = random.randint(1, 9)
if A % 2 == 0:
    print("A - четное число:")
    print(A)
else:
    print("A - нечетное число")
B = random.randint(1, 9)
if B % 2 == 0:
    print("B - четное число:")
    print(B)
else:
    print("B - нечетное число")
C = random.randint(1, 9)
if C % 2 == 0:
    print("C - четное число:")
    print(C)
else:
    print("C - нечетное число")
D = random.randint(1, 9)
if D % 2 == 0:
    print("D - четное число:")
    print(D)
else:
    print("D - нечетное число")
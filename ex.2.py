
#Определить, имеется ли среди трех чисел a, b и c хотя бы одна пара равных между собой чисел

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
if a == b or a == c or b == c:
    print("Есть хотя бы одна пара равных между собой чисел")
if a == b:
    print("Это пара чисел - a и b")
elif a == c:
    print("Это пара чисел - a и c")
elif b == c:
    print("Это пара чисел - b и c")
else:
    print("Пары равных между собой чисел - отсутствуют")
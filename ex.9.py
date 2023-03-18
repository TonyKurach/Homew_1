import random

# Проверить, является ли дробь A / B правильной

A = abs(random.randint(-100, 100))   #модуль числа
A != 0
B = abs(random.randint(-100, 100))   #модуль числа
B != 0
print("Значение числа A - ")
print(A)
print("Значение числа B - ")
print(B)
if A / B < 1:
    print("Дробь правильная")
else:
    print("Дробь неправильная")
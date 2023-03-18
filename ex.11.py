import random

#Даны три числа: a, b, c. Значение наибольшего из них присвоить переменной d

a = random.randint(0, 100)
print("Значение числа a")
print(a)
b = random.randint(0, 100)
print("Значение числа b")
print(b)
c = random.randint(0, 100)
print("Значение числа c")
print(c)
if a > b and a > c:
    d = a
    print("a - наибольшее число")
elif b > c and b > a:
    d = b
    print("b - наибольшее число")
elif c > a and c > b:
    d = c
    print("c - наибольшее число")
elif a == c and a == b:
    print("Наибольшее число отсутствует")
elif a == c and a != b:
    print("Наибольших чисел два (оба равные): a и c")
elif a == b and a != c:
    print("Наибольших чисел два (оба равные): a и b")
else:
    print("Наибольших чисел два (оба равные): b и c")



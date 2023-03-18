
# Дано натуральное четырехзначное число n. Верно, что все его цифры различны?

import random

a = random.randint(1, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
d = random.randint(0, 9)
f = a*1000 + b*100 + c*10 + d
print("Введенное натуральное четырехзначное ")
print(f)
if a == b and b == c and c == d:
    print("Все цифры числа одинаковы")
elif a == b and b == c and a != d:
    print("Первые три цифры четырехзначного числа равны")
elif a != b and b == c and c == d and b == d:
    print("Второе, третье и четвертое цифры четырехзначного числа равны")
elif a == b and c != d and a != d and b != d:
    print("Первые две цифры четырехзначного числа равны")
elif a != b and a == c and c != d and a != d:
    print("Первое и третье числа четырехзначного числа равны")
elif a != b and b != c and c == d and a == d:
    print("Первое, третье и четвертое числа четырехзначного числа равны")
elif a != b and b == d and c != d and a != d:
    print("Второе и четвертое числа четырехзначного числа равны")
elif a != b and b == c and c != d and a != d:
    print("Второе и третье числа четырехзначного числа равны")
elif a != b and b != c and c == d and a != d:
    print("Третье и четвертое числа четырехзначного числа равны")
elif a != b and c != d and b != c and a == d:
    print("Первое и четвертое цифры четырехзначного числа равны")
elif a == b and b != c and c == d and a != d:
    print("Первое и второе, а также третье и четвертое числа четырехзначного числа равны")
else:
    print("Все цифры четырехзначного числа разные")
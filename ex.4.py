
# По номеру месяца напечатать пору года

a = int(input("Введите номер месяца года от 1 до 12:\n"))
if a < 1:
    print("Вы ввели неправльный номер месяца")
    print("Вы ввели значение: ")
elif a > 12:
    print("Вы ввели неправльный номер месяца")
    print("Вы ввели значение: ")
elif a <= 12:
    print("Вы ввели значение: ")
print(a)
dict_month = {
    1: 'Январь', 2: 'Февраль', 3: 'Март',
    4: 'Апрель', 5: 'Май', 6: 'Июнь',
    7: 'Июль', 8: 'Август', 9: 'Сентябрь',
    10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'
}
dict_season = {
    'Декабрь': 'Зима', 'Январь': 'Зима', 'Февраль': 'Зима',
    'Март': 'Весна', 'Апрель': 'Весна', 'Май': 'Весна',
    'Июнь': 'Лето', 'Июль': 'Лето', 'Август': 'Лето',
    'Сентябрь': 'Осень', 'Октябрь': 'Осень', 'Ноябрь': 'Осень',
}
for k, v in dict_month.items():
    if a == k:
        #print("Выбранное значение соответствует месяцу:")
        #print(v)
        for p, m in dict_season.items():
            if v == p:
                print("Выбранный номер месяца соответствует поре года:")
                print(m)
# Расчет нормы сна
A = int(input("Норма сна"))
B = int(input("Спать не более, чем..."))
H = int(input("Фактическое время сна"))

if H < A:
    print("Недосып")
elif H > B:
    print("Пересып")
else:
    print("Это нормально")

# Является ли год високосным

year = int(input("Введите год"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Високосный")
else:
    print("Обычный")
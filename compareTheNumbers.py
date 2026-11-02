a = int(input("Введите число"))

if a % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

b = int(input("Введите первое число"))
c = int(input("Введите второе число"))
if c != 0:
    print(b / c)
else:
    print("Делить на ноль нельзя")
    c = int(input("Введите второе число != 0"))
    if c == 0:
        print("Не получилось")
    else:
        print(b / c)





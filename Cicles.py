a = 5
while a > -5:
    print(a, end=' ')
    a -= 1

# Вывод всех нечетных чисел в интервале от 5 до 55
b = 5
while b <= 55:
    if b % 2 == 1:
        print(b, end=' ')
    b += 1


i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
    print(i)

# Рисуем треугольник
n = int(input('Enter a count of...: '))
c = 1
while c <= n:
    print('*' * c)
    c += 1




# Рисуем треугольник снова

q = int(input('Enter a count of stars...: '))
stars = "*"
while len(stars) <= q:
    print(stars)
    stars = stars + "*"


# Задачка

w = 0
while w < 5:
    print("*")
    if w % 2 == 0:
        print('**')
    if w > 2:
        print('***')
    w = w + 1

# Сумма чисел на отрезке
number_1 = int(input('Enter a number: '))
number_2 = int(input('Enter another number: '))
s = 0
i = number_1
while i <= number_2:
    s += i
    i += 1
print(s)

# Сумма чисел, пока не введем 0
total = 0
num = int(input())
while num != 0:
    total += num
    num = int(input())
print(total)


# Кусочки торта для двух команд
team_1 = int(input('Enter a count of people 1: '))
team_2 = int(input('Enter a count of people 2: '))

d = team_1
while d % team_1 != 0 or d % team_2 != 0:
    d += 1
print(d)
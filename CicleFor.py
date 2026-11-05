# Квадрат числа
# for i in 2, 3, 5:
#     print(i ** 2)

# Range (последовательность)
# (start, to, step)

# for i in range(3, 9, 2):
#     print(i ** 2)


# Вывести квадрат
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print('*', end=" ")
#     print()

# Задачка

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# # Заголовочная строка
# print('\t', end='')
# for j in range(c, d + 1):
#     print('\t' + str(j), end='')
# print()
#
# # Строки таблицы
# for i in range(a, b + 1):
#     print(str(i), end='')
#     for j in range(c, d + 1):
#         print('\t' + str(i * j), end='')
#     print()



# a, b = input().split()
# a = int(a)
# b = int(b)
# s = 0
# for i in range(a, b + 1):
#     if i % 2 == 1:
#         s += i
# print(s)


# a, b = input().split()
# a = int(a)
# b = int(b)
# s = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1, 2):
#     s += i
# print(s)


# a, b = (int(i) for i in input().split())
# s = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1, 2):
#     s += i
# print(s)

a = int(input())
b = int(input())
s = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        count += 1
if count > 0:
    print(s/count)
else:
    print("На выбранном отрезке нет чисел, кратных 3")
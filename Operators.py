# 5 пар чисел и их произведение

i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a * b)
    i += 1

# Break

i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        break
    if a == 0 or b == 0:
        continue
    print(a * b)
    i += 1

# Задание
i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1
print(i)

# Задание 2

i = int(input())
while i <= 100:
    if i >= 10:
        print(i)
    i = int(input())





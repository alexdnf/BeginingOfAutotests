# Количество минут сна

a = int(input("Введите количество часов сна ночью"))
b = int(input("Введите количество минут сна днем"))
count_of_sleep_min = b + a*60
count_of_sleep_hours = count_of_sleep_min / 60

print("Количество минут сна равно:", count_of_sleep_min)
print("Количество часов сна равно:", count_of_sleep_hours)


# Оптимальное время для будильника

a = int(input("Оптимальное время сна в минутах"))
hours = int(a / 60)
minutes = a % 60
print(hours)
print(minutes)

# Оптимальное время для сна, если ложиться не в полночь
a = int(input("Оптимальное время сна в минутах"))
b = int(input("Час, когда ложишься спать"))
c = int(input("Минуты, когда ложишься спать"))
total = a + b * 60 + c
hours = total / 60
minutes = total % 60
print(int(hours))
print(minutes)
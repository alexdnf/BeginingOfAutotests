a = int(input('side a'))
b = int(input('side b'))
c = int(input('side c'))

p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(s)


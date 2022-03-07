duration = int(input('Введите число: '))
d = duration // 86400
h = duration // 3600
m = duration % 3600
if m >= 60:
    m = m // 60
else:
    m = 0
s = duration % 60
if d > 0:
    print(d, 'д', end = ' ')
if h > 0:
    print(h, 'ч', end = ' ')
if m > 0:
    print(m, 'мин', end = ' ')
if s > 0:
    print(s, 'сек', end = ' ')
# * Дан отсортированный список. Реализуйте бинарный поиск.
from random import random
k = int(input('введите длину списка'))
a = []
for i in range(k):
    a.append(int(random()*10))
a.sort()
print(a)

n = int(input('введите число для поиска'))

l = 0
h = k-1
while l <= h:
    m = (l + h) // 2
    if n < a[m]:
        h = m - 1
    elif n > a[m]:
        l = m + 1
    else:
        print('число под номером', m)
        break
else:
    print('нет такого')
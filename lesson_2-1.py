# Дана строка “spam and eggs or eggs with spam”. Посчитать сколько раз встретился каждый символ.
a = "spam and eggs or eggs with spam"
a=list(a)
print(a)
b = {}
for i in a:
    b[i] = b.get(i, 0)+1
for i in b:
    print('символ', i, 'встретился', b[i], 'раз')

# Дана строка "English = 78 Science = 83 Math = 68 History = 65". Вычислить сумму всех чисел в строке.
a = "English = 78 Science = 83 Math = 68 History = 65"
a = a.split()
b = 0
for i in a:
    if i.isdigit():
        b = b + int(i)
print('сумма чисел', b)
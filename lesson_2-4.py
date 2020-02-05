# На ввод дается строка. Нужно каждое слово развернуть наоборот. Порядок слов не должен меняться.
a = input('введите строку')
b = a.split()
for i in range(len(b)):
    b[i]=list(b[i])
    b[i].reverse()
    b[i]=''.join(b[i])
c = ' '.join(b)
print(c)

# Напишите генератор случайных паролей. После запуска программа должна ждать ввода числа - длины пароля и нажатия Enter.
# Завершить программу нужно если будет введен 0. Также нужно проверять является ли введенная строка числом.
# Допустимые символы - цифры, большие и маленькие латинские буквы.(нужно использовать метод input)
import sys
import random
while True:
    a = input('введите длину пароля')
    if a == '0':
        sys.exit()
    if not a.isdigit():
        print('это не число')
    s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    b=''
    for i in range(int(a)):
        b=b+random.choice(s)
    print('пароль', b)
# -*- coding: UTF-8 -*-
a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
if a < b:
        print('Ошибка')
else:
    for i in range(a,b-1,-3):
        print(i)

# -*- coding: UTF-8 -*-
n=int(input('Введите крайнее число: '))
if n>9:
    print('Ошибка')
else:
    for i in range(1,n+1):
        for k in range(1,i+ 1):
            print(k,end='')
        print()

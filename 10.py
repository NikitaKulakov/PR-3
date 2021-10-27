# -*- coding: UTF-8 -*-
n=int(input('Введите количество чисел: '))
k=int(input('Введите порядковый номер: '))
a=k
b=k
for i in range(k+1,n+1):
    a,b=b,a+b
    print(a,b,)

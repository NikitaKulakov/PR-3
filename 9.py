# -*- coding: UTF-8 -*-
n=int(input('Введите количество чисел: '))
a=1
b=1
for i in range(1,n+1):
    a,b=b,a+b
print (b)


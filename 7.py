# -*- coding: UTF-8 -*-
n=int(input('Введите число в конце цикла: '))
b=1
c=0
for i in range(1,n+1):
    b*=i
    c+=b
print(c)

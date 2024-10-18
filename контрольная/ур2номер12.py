import math as m
print("1-площадь квадрата"
      "2-площадь круга"
      "3-площадь треугольника")
x=int(input())
print("Введите количество значений")
n=int(input())
s=1
if x==1:
    for i in range(n):
        r=int(input())
        s=r**2
        print(s)
        s=1
elif x==2:
    for i in range(n):
        r = int(input())
        s=m.pi*r**2
        print(s)
        s=1
elif x==3:
    for i in range(n):
        r = int(input())
        s=(r**2*m.sqrt(3))/4
        print(s)
        s=1



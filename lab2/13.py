import math
a=None
b=None
print("1-площадь прямоугольника",
      "2-площадь участка заключенного между 2 кольцами",
      "3-площадь равнобедренного треугольника")
q=int(input())
while True:
    print('Введите a,b')
    a=input()
    b = input()
    if a == 'стоп' or b == 'стоп':
        break
    a=int(a)
    b=int(b)
    if q==1:
        print(a*b)
    elif q==2:
        print(math.fabs(math.pi*a**2-math.pi*b**2))
    elif q==3:
        h=math.sqrt(b**2-(a/2)**2)
        print(0.5*a*h)


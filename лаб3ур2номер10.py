print("Введите количество элементов массива")
n=int(input())
print("Введите элементы массива")
q=[]
r=[]
for i in range(n):
    x = int(input())
    q.append(x)
print("Изначально:",q)
q.sort()
for i in range(len(q)):
    if q[i]>0:
        u=q[i]
        print(q.count(q[i]))
        break
for i in range(len(q)):
    if q[i]!=u:
        r.append(q[i])
print("конечный массив:",r)
print("Минимальный положительный элемент :",u)

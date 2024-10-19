print("Введите количество элементов массива")
n=int(input())
print("Введите элементы массива")
q=[]
r=[]
w=[]
for i in range(n):
    x = float(input())
    q.append(x)
print("Изначально:",q)
for i in range(len(q)):
    if q[i]>1 or q[i]<-1:
        r.append(q[i])
for i in range(len(q)):
    if q[i]<=1 and q[i]>=-1:
        w.append(q[i])
print("Числа от -1 до 1 :", w)
print("Обратные числа :", r)




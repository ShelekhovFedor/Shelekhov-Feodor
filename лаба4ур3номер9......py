import random as rd
q=[[-3, -2, 5, -1, 10], [10, -7, -2, -3, 7], [-4, 10, -4, 1, 5], [-4, -3, 9, -8, -10], [3, 5, 2, 5, 7], [5, 8, 9, -9, 4], [5, -9, 0, -4, 2]]
for i in q:
    print(i,sep="")
e=0
r=[]
for i in range(5):
    for j in range(7):
        if q[j][i]<0:
            e+=1
    r.append(e)
    e=0
print()
print(r)
print()
for i in range(5):
    x=min(r[i:])
    t=r.index(x)
    r[i], r[t] = r[t], r[i]
    for j in range(7):
        q[j][i] , q[j][t] = q[j][t] , q[j][i]
for i in q:
    print(i,sep="")
print(r)

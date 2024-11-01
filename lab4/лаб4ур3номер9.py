import numpy as np
import random as rd
q=[[ rd.randint(-10,10) for i in range(5)] for j in range(7)]
for i in q:
    for j in i:
        print(j, end = ' ')
    print()
q=np.transpose(q)
print(q)
w=[]
e=0
r=[]
t=[]
u=[]
for i in range(5):
    for j in range(7):
        w.append(int(q[i][j]))
print(w)
for i in range(5):
    for j in range(7):
        if q[i][j]<0:
            e+=1
    r.append(e)
    e=0
print(r)
for i in range(5):
    p=min(r)
    v=r.index(p)
    u.append(v)
    r.pop(v)
u.sort()
print(u)
for i in range(len(u)):
    t.append(w[7*u[i]:7*u[i]+7])
t=np.transpose(t)
print(t)

import math as m
q=[]
for i in range (10):
    x=int(input())
    q.append(x)
for i in range(len(q)):
    y=m.log(q[i])*0.5
    print("x:",q[i],"y:",y)
    y=1

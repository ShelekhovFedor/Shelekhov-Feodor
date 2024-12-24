import math as mh
q=[[-2, 10, -2, -2, 5],
[6, -1, -5, 3, 1],
[5, -2, -2, -5, 2],
[1, -7, 0, 5, 7],
[7, -1, 3, 5, 0]]
for i in range(len(q)):
    print(q[i])
x=abs(q[1][0])
for i in range(len(q[1])):
    if abs(q[1][i])<x:
        x=abs(q[1][i])
print(x)
for i in range(len(q[0])):
    if abs(q[1][i])==x:
        c=i+1
        break
if c>4:
    c=0
print(c)
for i in range(len(q)):
    q[i].pop(c)
    i+=1
for i in range(len(q)):
    print(q[i])


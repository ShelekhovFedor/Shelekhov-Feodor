import random as r
q=[[ r.randint(0,10) for i in range(10)] for j in range(5)]
for i in q:
    for j in i:
        print(j, end = ' ')
    print()
for i in range(5):
    x=max(q[i])
    w=q[i].index(x)
    if w<=4:
        e=sum(q[i][w+1:])
        print(e)
        q[i].pop(0)
        q[i].insert(0,e)
for i in q:
    for j in i:
        print(j, end = ' ')
    print()


q=[[5, 0, 8, 5, 8],
[2, 6, 4, 1, 10],
[3, 10, 9, 8, 3],
[7, 2, 5, 5, 8],
[6, 6, 3, 5, 9],
[8, 7, 8, 5, 2],
[1, 9, 1, 9, 8],
[0, 1, 1, 3, 5],
[9, 4, 1, 8, 4],
[10, 6, 5, 8, 1]]
for i in q:
    for j in i:
        print(j, end = ' ')
    print()
r=[]
e=None
o=0
u=None
for i in range(5):
    for j in range(10):
        r.append(q[j][i])
    e=max(r)
    u = r.index(e)

    print(u)

    if u>=0 and u<5:
        o=sum(r[(u+1):])
        q[0].pop(i)
        q[0].insert(i,o)
        o=0
        u=0
    for s in range(len(r)):
        r.pop()
for i in range(len(q)):
    print(q[i])


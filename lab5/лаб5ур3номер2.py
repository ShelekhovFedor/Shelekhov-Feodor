q=[[0,1,2],[8,4,5],[2,0,3]]
w=1
for i in range(len(q)):
    print(q[i])
print()
def task(q,w):
    for i in range(len(q)):
        if w%2!=0:
            for j in range(len(q[0])):
                for t in range(len(q[0])):
                    if q[i][j]>q[i][t]:
                        q[i][j],q[i][t]=q[i][t],q[i][j]
            w+=1
        else:
            for o in range(len(q[0])):
                for u in range(len(q[0])):
                    if q[i][o]<q[i][u]:
                        q[i][o],q[i][u] = q[i][u] ,q[i][o]
            w+=1
    return q
for i in range(len(task(q,w))):
    print(task(q,w)[i])

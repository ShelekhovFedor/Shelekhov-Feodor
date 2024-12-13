q=[[0,1,2],[8,4,5],[2,0,3]]
w=1
def task(q,w):
    for i in range(len(q)):
        if w%2!=0:
            q[i].sort()
            q[i].reverse()
            w+=1
        else:
            q[i].sort()
            w+=1
    return q
for i in range(len(task(q,w))):
    print(task(q,w)[i])

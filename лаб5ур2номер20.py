q=[[0,1,2],[3,4,5],[2,0,3]]
i=0
def task(q):
    i=0
    while i!=len(q[0]):
        w = False
        for j in range(len(q)):
            if q[j][i]==0:
                w=True
                break
        if w==False:
            for j in range(len(q)):
                q[j].pop(i)
        else:
            i+=1
    return q
print(task(q))







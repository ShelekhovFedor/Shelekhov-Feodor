q=[[0,1,2],[8,4,5],[2,0,3]]
w=1
for i in range(len(q)):
    if w%2!=0:
        q[i].sort()
        q[i].reverse()
        w+=1
    else:
        q[i].sort()
        w+=1
print(q)

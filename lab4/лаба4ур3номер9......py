q=[[-3, -2, 5, -1, 8,-1,9], [-7, -7, 2, -3, 7,-9,4], [-4, -5, -4, 1, 5,-7,-2,], [-4, -3, -9, -8, 1,3,7], [3, -5, -2, -5, -7,-8,-9]]
for i in q:
    print(i,sep="")
e=0
r=[]
for i in range(7):
    for j in range(5):
        if q[j][i]<0:
            e+=1
    r.append(e)
    e=0
print()
print(r)
print()
for i in range(7):
    x=min(r[i:])
    t=r.index(x)
    r[i], r[t] = r[t], r[i]
    r[i]=99
    for j in range(5):
        q[j][i] , q[j][t] = q[j][t] , q[j][i]
    print(r)
print(r)
print()
for i in q:
    print(i,sep="")
print(r)


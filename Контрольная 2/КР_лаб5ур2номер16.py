q=[1,3,-4,0,-4,3,5,-9,2,-1]
print('Начальный массив:',q)
print()
w=[]
def task(q,w):
    for i in range(len(q)):
        if q[i]<0:
            w.append(q[i])
            q[i]=''
    print(w)
    print(q)
    w.sort()
    w.reverse()
    e=0
    for i in range(len(q)):
        if q[i]== '' :
            q[i]=w[e]
            e+=1
    return q
print('Конечный массив:',task(q,w))




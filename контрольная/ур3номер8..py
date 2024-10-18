q=[]
n=int(input())
for i in range(n):
    x = int(input())
    q.append(x)
w=[]


for i in range(len(q)):
    if q[i]<0:
        w.append(q[i])
        q[i]=""
e=0
w.sort()
w.reverse()
print(w)
print(q)
for i in range (len(q)):
    if q[i]=="":

        q.pop(i)
        q.insert(i,w[e])
        e+=1
print(e)
print("Итог:",q)

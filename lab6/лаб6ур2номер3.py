class sportsmens:
    def __init__(self,name,first,second,third):
        self.name=name
        self.first=first
        self.second=second
        self.third=third
a=[]
Dima=sportsmens('Дима',10,11,11)
Maria=sportsmens('Мария',2,13,1)
Anatoly=sportsmens('Анатолий',2,10,19)
a.append(Dima)
a.append(Maria)
a.append(Anatoly)
b=[]
w=[]
for i in range(len(a)):
    b.append(a[i].first)
    b.append(a[i].second)
    b.append(a[i].third)
    x = max(b)
    w.append(x)
    b=[]
print(w)
f=w[0]
for i in range(len(a)):
    c=w.index(max(w[i:]))
    w[i],w[c]=w[c],w[i]
    a[i], a[c] = a[c], a[i]
print(w)
for i in range(len(a)):
    print(a[i].name,a[i].first,a[i].second,a[i].third)


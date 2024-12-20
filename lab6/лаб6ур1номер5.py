class student:
    def __init__(self,name,marks,skips):
        self.name=name
        self.marks=marks
        self.skips=skips
a=[]
Dima=student('Дима',3,1)
Maria=student('Мария',2,10)
Anatoly=student('Анатолий',2,19)
a.append(Dima)
a.append(Maria)
a.append(Anatoly)
b=[]
for i in range(len(a)):
    if a[i].marks==2:
        b.append(a[i])
c=[]
while len(b)!=0:
    max_skips=0
    max_index=0
    for i in range(len(b)):
        print(b[i].skips)
        if b[i].skips>max_skips:
            max_skips=b[i].skips
            max_index=i
    c.append(b[max_index])
    b.pop(max_index)
for i in range(len(c)):
    print(c[i].name,c[i].marks,c[i].skips)


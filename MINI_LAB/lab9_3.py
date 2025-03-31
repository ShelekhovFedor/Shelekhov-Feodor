#3. На основании результатов соревнований по прыжкам в длину
# (фамилии и результаты трех попыток) составить итоговый протокол
# соревнований, считая, что в зачет идет лучший результат.
e=open('sportsmens.txt','r')

w=e.read()

q=w.split(',')


for i in range(0,3):
    q[i]=int(q[i])
for i in range(3,6):
    q[i]=int(q[i])
for i in range(6,9):
    q[i]=int(q[i])
r=q[0]
for i in range(0,3):
    if q[i]>r:
        r=q[i]
t=q[3]
for i in range(3,6):
    if q[i]>t:
        t=q[i]
y=q[6]
for i in range(6,9):
    if q[i]>y:
        y=q[i]
j=[]
j.append('first_sportsmen:')
j.append(str(r))
j.append('second_sportsmen:')
j.append(str(t))
j.append('third_sportsmen:')
j.append(str(y))
Results=open('Results.txt','w')
print(j)
for i in range(len(j)):
    Results.write(j[i])
e.close()
Results=open('Results.txt','r')
k=Results.read()
print(k)
Results.close()

#3. На основании результатов соревнований по прыжкам в длину
# (фамилии и результаты трех попыток) составить итоговый протокол
# соревнований, считая, что в зачет идет лучший результат.

first=open('first_sportsmen.txt','r')
second=open('second_sportsmen.txt','r')
third=open('third_sportsmen.txt','r')
q=first.read()
w=second.read()
e=third.read()
q=q.split(',')
w=w.split(',')
e=e.split(',')
for i in range(len(q)):
    q[i]=int(q[i])
for i in range(len(w)):
    w[i]=int(w[i])
for i in range(len(e)):
    e[i]=int(e[i])
r=q[0]
for i in range(len(q)):
    if q[i]>r:
        r=q[i]
t=w[0]
for i in range(len(w)):
    if w[i]>t:
        t=w[i]
y=e[0]
for i in range(len(e)):
    if e[i]>y:
        y=e[i]
print('first_sportsmen:',r)
print('second_sportsmen:',t)
print('third_sportsmen:',y)
first.close()
second.close()
third.close()
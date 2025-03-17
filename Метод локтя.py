import math
import random as rd
p = 0.8
xMin1=0
xMax1 = 50
yMin1=0
yMax1 = 50
xMin2 = 25
xMax2 = 75
yMin2 = 25
yMax2 = 75
classesCount = 2
pointsCount1= 50
pointsCount2 = 50
x=[]
y=[]
for i in range(pointsCount1):
    x.append([rd.uniform(xMin1,xMax1), rd.uniform(yMin1, yMax1)])
    y.append(1)
for i in range(pointsCount2):
    x.append([rd.uniform(xMin2,xMax2), rd.uniform(yMin2, yMax2)])
    y.append(2)
x_train =[]
y_train =[]
x_test = []
y_test = []
q=[]
w=None
e=None
for i in range(80):
    e=rd.randint(0,99)
    if e in q:
        while e in q:
            e = rd.randint(0, 99)
    q.append(e)
    x_train.append(x[e])
    y_train.append(y[e])
for i in range(20):
    e = rd.randint(0, 99)
    if e in q:
        while e in q:
            e = rd.randint(0, 99)
    q.append(e)
    x_test.append(x[e])
    y_test.append(y[e])
print('x_train')
print(x_train)
print('y_train')
print(y_train)
print('x_test')
print(x_test)
print('y_test')
print(y_test)
y_predict=[]
classes=[]
distance=[]
k=1
accuracy_q=[]
t=0
for d in range(1,81):
    for i in range(20):
        for j in range(80):
            distance.append(math.sqrt((x_train[j][0]-x_test[i][0])**2+(x_train[j][1]-x_test[i][1])**2))
        for f in range(k):
            l=min(distance)
            m_n=distance.index(l)
            classes.append(y_train[m_n])
            distance.pop(m_n)
            distance.insert(m_n,1000000)
        if classes.count(1)>classes.count(2):
            y_predict.append(1)
        else:
            y_predict.append(2)
        classes = []
        distance = []
    for z in range(20):
        if y_test[z] == y_predict[z]:
            t += 1
    accuracy_i = t / len(y_test)
    accuracy_q.append(accuracy_i)
    print('acc',accuracy_i)
    y_predict=[]
    t=0
    k+=1
print('accuracy_q',accuracy_q)
rty=accuracy_q.index(max(accuracy_q))+1
print('max accuracy_q',max(accuracy_q),'k=',rty)
m=[]
for i in range(3,83):
    m.append(i)
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
plt.plot(m,accuracy_q)
plt.show()
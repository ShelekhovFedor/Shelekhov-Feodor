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
k =3
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
t=0
green_doty=[]
green_dotx=[]
red_doty=[]
red_dotx=[]
for i in range(20):
    if y_test[i]==y_predict[i]:
        t+=1
        green_doty.append(y_test[i])
        green_dotx.append(x_test[i])
    else:
        red_doty.append(y_test[i])
        red_dotx.append(x_test[i])
accuracy=t/len(y_test)
print('accuracy',accuracy)
print('y_predict',y_predict)
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
for i in range(80):
    if y_train[i]==1:
        ax.scatter(x_train[i][0],x_train[i][1], marker='o',c='blue')
    else:
        ax.scatter(x_train[i][0], x_train[i][1], marker='x', c='blue')
for i in range(len(green_doty)):
    if green_doty[i]==1:
        ax.scatter(green_dotx[i][0],green_dotx[i][1], marker='o',c='green')
    else:
        ax.scatter(green_dotx[i][0], green_dotx[i][1], marker='x', c='green')
for i in range(len(red_doty)):
    if red_doty[i]==1:
        ax.scatter(red_dotx[i][0],red_dotx[i][1], marker='o',c='red')
    else:
        ax.scatter(red_dotx[i][0], red_dotx[i][1], marker='x', c='red')
plt.show()







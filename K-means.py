import random as rd
import matplotlib.pyplot as plt
import numpy as np
k=[]
for i in range(3):
    x=rd.uniform(1, 39)
    y=rd.uniform(1, 39)
    k.append([x,y])
print('k-old')
print(k)
dot_count=0
classes=[]
while dot_count!=100:
    q=rd.randint(1,3)
    if q==1:
        x=rd.uniform(1,19)
        y = rd.uniform(1, 19)
        if ((x-10)**2+(y-10)**2)<9**2:
            classes.append([x,y])
            dot_count+=1
        else:
            continue

    if q==2:
        x=rd.uniform(21,39)
        y = rd.uniform(4, 22)
        if ((x-30)**2+(y-13)**2)<9**2:
            classes.append([x,y])
            dot_count += 1
        else:
            continue
    if q==3:
        x=rd.uniform(5,23)
        y = rd.uniform(21, 39)
        if ((x-14)**2+(y-30)**2)<9**2:
            classes.append([x,y])
            dot_count += 1
        else:
            continue
print('classes')
print(classes)
delta=[]
n=2
while n>0.001:
    dist_1=[]
    dist_2=[]
    dist_3=[]
    n=0
    clas_predict=[]
    for i in range(len(classes)):
        q=round(((k[0][0]-classes[i][0])**2+(k[0][1]-classes[i][1])**2)**0.5,14)
        dist_1.append(q)
    for i in range(len(classes)):
        q=round(((k[1][0]-classes[i][0])**2+(k[1][1]-classes[i][1])**2)**0.5,14)
        dist_2.append(q)
    for i in range(len(classes)):
        q=round(((k[2][0]-classes[i][0])**2+(k[2][1]-classes[i][1])**2)**0.5,14)
        dist_3.append(q)

    for i in range(len(classes)):
        if dist_1[i]<dist_2[i] and dist_1[i]<dist_3[i]:
            clas_predict.append(1)

        if dist_2[i]<dist_1[i] and dist_2[i]<dist_3[i]:
            clas_predict.append(2)

        if dist_3[i]<dist_2[i] and dist_3[i]<dist_1[i]:
            clas_predict.append(3)
    print('clas_predict')
    print(clas_predict)
    sx_1=0
    sy_1=0
    sx_2=0
    sy_2=0
    sx_3=0
    sy_3=0
    for i in range(100):
        if clas_predict[i]==1:
            sx_1+=classes[i][0]
            sy_1 += classes[i][1]
        if clas_predict[i]==2:
            sx_2 += classes[i][0]
            sy_2 += classes[i][1]
        if clas_predict[i]==3:
            sx_3 += classes[i][0]
            sy_3 += classes[i][1]
    delta.append(((k[0][0]-sx_1/clas_predict.count(1))**2+(k[0][1]-sy_1/clas_predict.count(1))**2)**0.5)
    delta.append(((k[1][0] - sx_2 / clas_predict.count(2)) ** 2 + (k[1][1] - sy_2 / clas_predict.count(2)) ** 2) ** 0.5)
    delta.append(((k[2][0] - sx_3 / clas_predict.count(3)) ** 2 + (k[2][1] - sy_3 / clas_predict.count(3)) ** 2) ** 0.5)
    n=max(delta)
    print('n    ',n)
    k[0]=[sx_1/clas_predict.count(1),sy_1/clas_predict.count(1)]
    k[1]=[sx_2/clas_predict.count(2),sy_2/clas_predict.count(2)]
    k[2]=[sx_3/clas_predict.count(3),sy_3/clas_predict.count(3)]
    print('k-new')
    print(k)
    dist_1 = []
    dist_2 = []
    dist_3 = []
    clas_predict = []
    sx_1 = 0
    sy_1 = 0
    sx_2 = 0
    sy_2 = 0
    sx_3 = 0
    sy_3 = 0
    delta=[]

t=np.linspace(0,2*np.pi,200)
r=9
x=r*np.sin(t)+10
y=r*np.cos(t)+10

xx=r*np.sin(t)+30
yy=r*np.cos(t)+13

xxx=r*np.sin(t)+14
yyy=r*np.cos(t)+30

fig, ax = plt.subplots()
for i in range(len(classes)):
    plt.scatter(classes[i][0],classes[i][1], c='blue')
plt.plot(x,y,c='blue')
plt.plot(xx,yy,c='blue')
plt.plot(xxx,yyy,c='blue')
plt.gca().set_aspect('equal')
for i in range(3):
    plt.scatter(k[i][0],k[i][1],c='red')
plt.show(




























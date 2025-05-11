import math as mh
import matplotlib.pyplot as plt
import numpy as np
import random as rd

speed=0.001
epoch=10000

a=3                           
b=2
c=2
print('ideal:',a,b,c)
x=np.linspace(0.01,3,100)
# u=np.linspace(-4,-0.1,50)
# r=np.linspace(0.1,4,50)
# x=np.concatenate([u,r])
# xx=np.linspace(-4,0.1,100)
# print(u)
# print(r)

noise=np.random.normal(0, 2, size=100)
y=a*x**b+c+noise
y2=a*x**b+c
y2 = np.where(x >= 0, y2, y2)

plt.figure(1)
plt.scatter(x,y,c='r')
plt.plot(x,a*x**b+c,'y--',label='real')
plt.plot(-x,y2,'y--')

a=1
b=1
c=3
for o in range(epoch):
    j=0
    diff_a=0
    diff_b=0
    diff_c=0

    # for i in range(100):
    #     j+=(a*x[i]**b+c-y[i])**2
    # print(j)
    for i in range(100):
        diff_a+=2*a*x[i]**(2*b)+2*c*x[i]**b-2*y[i]*x[i]**b
        diff_b+=2*a*x[i]**b*np.log(mh.fabs(x[i]))*(a*x[i]**b+c-y[i])
        diff_c+=2*a*x[i]**b+2*c-2*y[i]
    

    a=a-speed*diff_a/100
    b=b-speed*diff_b/100
    c=c-speed*diff_c/100
y1=a*x**b+c
y1 = np.where(x >= 0, y1, y1)
plt.plot(x,a*x**b+c,label='pred',c='b')
plt.plot(-x,y1,c='b')
# plt.plot(xx,a*x**b+c)
plt.legend()
print(a,b,c)
plt.show()



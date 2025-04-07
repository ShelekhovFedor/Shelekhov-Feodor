import math as mh
import matplotlib.pyplot as plt
import numpy as np
n = 100
k_ideal = 10
b_ideal = 0
x1 = np.linspace(0, 10, n)
noise = np.random.normal(0, 2, size=n)
y1 = k_ideal * x1 + b_ideal + noise
k=0
b=0
a=0.00001
s=0.00001
q=0
e=0
for j in range(100000):
    for i in range(len(x1)):
        q+=x1[i]*(y1[i]-(k*x1[i]+b))
    q=(-2/100)*q
    for i in range(len(x1)):
        e+=y1[i]-(k*x1[i]+b)
    e=(-2/100)*e
    k=k-a*q
    b=b-s*e
print(k)
print(b)
fig,ax=plt.subplots()
plt.scatter(x1,y1,s=10)
plt.plot(x1,k_ideal*x1+b_ideal,'y--',label='real')
plt.plot(x1,k*x1+b,c='r',label='pred')
plt.legend()
plt.show()


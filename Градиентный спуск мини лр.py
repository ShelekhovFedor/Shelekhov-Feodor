import math as mh
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-2,2,10000)
# func=np.exp(-q**2)*np.sin(q**3/2)+np.arctan((q**2)/(1+q**4))+(q*np.cos(q))/(1+q**2)
func=np.exp(x)+np.exp(-x)+2
plt.figure(1)
plt.plot(x,func)
plt.show()

x=1
speed=0.01
epoch=100000

for i in range(epoch):
    diff=(np.exp(2*x)-1)/np.exp(x)
    # diff=np.exp(-x**2)*(-2*x)+2*x
    # diff=-(2*x*np.sin(x**3/2))/(np.exp(x**2))+(3*x**2*np.cos(x**3/2))/(2*np.exp(x**2))+(2*x-2*x**5)/(x**8+3*x**4+1)+(np.cos(x)-np.cos(x)*x**2-x*np.sin(x)-x**3*np.sin(x))/((1+x**2)**2)
    x=x-speed*diff
    
print(x)



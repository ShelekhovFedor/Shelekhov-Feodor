a=int(input())
b=int(input())
c=int(input())
d=int(input())
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(0, d, 200)
y =a+b*x**2+c*x**0.5

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
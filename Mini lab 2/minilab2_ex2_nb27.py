import matplotlib.pyplot as plt
import numpy as np
e=open('точки.txt','r')

w=e.read()

q=w.split(',')


import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
ax.scatter(q[:11], q[11:])
ax.invert_yaxis()
plt.show()

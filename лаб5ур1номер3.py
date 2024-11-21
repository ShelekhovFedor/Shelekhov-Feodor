import math
v=10
V=9
a=1
A=1.6
t=1
T=4
if v*t+(a*t**2)/2>V*t+(A*t**2)/2:
    print("За 1 час 1 проедет больше")
else:
    print("За 1 час 2 проедет больше")
if  v*T+(a*T**2)/2>V*T+(A*T**2)/2:
    print("За 4 час 1 проедет больше")
else:
    print("За 4 час 2 проедет больше")
o=(2*(v-V))/(a-A)
print(math.fabs(o))
import math
v=10
V=9
a=1
A=1.6
t=1
T=4
def result(v,V,a,A,t,T):
    x1=v*t+(a*t**2)/2>V*t+(A*t**2)/2
    x2 = v * T + (a * T ** 2) / 2 > V * T + (A * T ** 2) / 2
    if x1:
        return "За 1 час 1 проедет больше"
    else:
        return "За 1 час 2 проедет больше"
def resul(v, V, a, A, t, T):
    x2 = v * T + (a * T ** 2) / 2 > V * T + (A * T ** 2) / 2
    if  x2:
        return "За 4 час 1 проедет больше"
    else:
        return "За 4 час 2 проедет больше"
def resu(v, V, a, A):
    o=math.fabs((2*(v-V))/(a-A))
    return 'Догонит за ',o
print(result(v, V, a, A, t, T))
print(resul(v, V, a, A, t, T))
print(resu(v, V, a, A))

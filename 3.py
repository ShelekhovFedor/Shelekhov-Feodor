import math
a=0.1
b=1
h=0.1
s=0
q=1
i=0
y=1
x=0.1
while q>=0.0001:
   

    s+=((-1)**i)*(x**(2*i)/math.factorial(2*i))
    y=math.cos(x)
    print(y)
    q=(-1)**i*(x**(2*i)/math.factorial(2*i))
    x+=0.1
    i+=1
    if x==1:
        q=-1
print(s)              

import math 
x=2
s=0
q=1
n=1
while abs(q)>=(0.0001):
    s+=(math.cos(n*x))/n**2
    n+=1
    q=(math.cos(n*x))/n**2
print(s)
    
    
    

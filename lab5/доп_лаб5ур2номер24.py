q=[[-3, -2, 5,9], [-7, -7, 2, -3 ], [-4, -5, -4, 1], [-4, -3, -9, -8]]
for i in range(len(q)):
    print(q[i])
x=q[0][0]
def max_el(q,x):
    for i in range(len(q)):
        for j in range(len(q[0])):
            if q[i][j]>x:
                x=q[i][j]
    return x
print(max_el(q,x))
v=0
b=0
def str_max(q,b):
    for i in range(len(q)):
        if max_el(q,x) in q[i]:
            b=q[i].index(max_el(q,x))
    return b
print(str_max(q,b))
n=str_max(q, b)
for i in range(len(q)):
    q[i][i],q[i][n]=q[i][n],q[i][i]
for i in range(len(q)):
    print(q[i])











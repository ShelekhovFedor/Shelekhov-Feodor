
x=0
w=[[9, 6, 9, 2, 9], [3, 4, 5, 5, 9], [10, 5, 2, 9, 4], [8, 6, 5, 3, 9], [8, 1, 3, 3, 10], [3, 1, 7, 2, 7]]
print(w)
for i in range(6):
    x = max(w[i])
    w[i].insert(5,x)
    x=None
print(w)


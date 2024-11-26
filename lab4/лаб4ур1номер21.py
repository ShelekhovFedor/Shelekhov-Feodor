
x=0
w=[[9, 6, 9, 2, 9, 1], [3, 4, 5, 5, 9,5], [10, 5, 2, 9, 4, 2], [8, 6, 5, 3, 9,2], [8, 1, 3, 3, 10,9]]
for i in range(len(w)):
    print(w[i])
for i in range(5):
    x = max(w[i])
    w[i].insert(5,x)
    x=None
print()
for i in range(len(w)):
    print(w[i])

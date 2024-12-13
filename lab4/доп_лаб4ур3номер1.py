#переставить строки так чтобы мин элементы следовали в порядке убывания
A =[[1, 6, 3, 34, 5],
    [6, 7, 21, 9, 10],
    [1, 2, 13, 14, 15],
    [16, 17, 8, 19, 5],
    [7, 22, 3, 20, 25],
    [26, 7, 28,9, 30],
    [3, 32, 3, 4, 9]]
n = len(A)
for i in range(n):
    for j in range(0, n - i - 1):
        min_val_j = A[j][0]
        for k in range(1, len(A[j])):
            if A[j][k] < min_val_j:
                min_val_j = A[j][k]
        min_val_j1 = A[j + 1][0]
        for k in range(1, len(A[j + 1])):
            if A[j + 1][k] < min_val_j1:
                min_val_j1 = A[j + 1][k]
        if min_val_j < min_val_j1:
            A[j], A[j + 1] = A[j + 1], A[j]
for i in range (len(A)):
    print(A[i])
s=0
q=1
for i in range(64):
    s=s+q
    q*=2
print("Количество зерен:",s)
print("Количество грамм:",s//15)



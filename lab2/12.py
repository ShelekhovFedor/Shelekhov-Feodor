
r=None
s=1
while True:
    r=input()
    if str(r)=='стоп':
        break
    s=s*int(r)**2

    print(s)
    s=1


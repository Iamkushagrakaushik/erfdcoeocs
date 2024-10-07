t=int(input())
x=[]
for _ in range(t):
    n=int(input())
    a=0
    k=0
    for i in range(2,n+1):
        m=n//i
        l=(i*(m+1)*m)//2
        if l>k:
            z=i
            k=l
    x.append(z)
for i in x:
    print(i)
    
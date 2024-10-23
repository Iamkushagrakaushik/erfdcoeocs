t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n==1:
        print(a[0]+1)
    else:
        m=0
        c=0
        c1=(n+1)//2
        c2=n//2
        max1=max(a[::2])
        max2=max(a[1::2])
        if max1+c1>max2+c2:
            m,c=max1,c1
        else:
            m,c=max2,c2
        print(m+c)
        
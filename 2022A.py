t=int(input())
for _ in range(t):
    n,r=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        if a[i]%2==0:
            c+=a[i]
            a[i]=0
        else:
            c+=a[i]-1

            a[i]=1
    r-=(c//2)
    va=sum(a)
    if r>=va:
        c+=va
    else:
        c+=(2*r)-va
    print(c)
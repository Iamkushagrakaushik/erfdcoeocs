t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    i=0
    for j in range(n-1,n-k-1,-1):
        if b[j]>a[i]:
            a[i]=b[j]
            i+=1
    print(sum(a))
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    c=float('inf')
    for i in range(n-1):
        if a[i+1]-a[i]<c:
            c=a[i+1]-a[i]
    print(c)
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    c=0
    k=n//2
    c=sum([a[k+i+n%2]-a[i] for i in range(k)])
    print(c)

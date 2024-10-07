n,m=tuple(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
c=0
s=0
for i in range(m):
    s+=a[i]
    if s<c:
        c=s
print(-1*c)



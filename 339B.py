n,m=map(int,input().split())
a=[1]
l=list(map(int,input().split()))
a+=l
c=0
for i in range(m):
    if a[i]>a[i+1]:
        c=c+n-(a[i]-a[i+1])
    else:
        c+=a[i+1]-a[i]
print(c)
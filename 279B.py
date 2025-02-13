n,t=map(int,input().split())
a=list(map(int,input().split()))
s,c,m,j=0,0,0,0
for i in range(n):
    if s+a[i]<=t:
        c+=1
        s+=a[i]
    else:
        s-=a[j]
        j+=1
        s+=a[i]
    if c>m:
        m=c
print(m)
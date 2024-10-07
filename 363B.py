n,k=map(int,input().split())
a=list(map(int,input().split()))
s,j=0,0
q=0

for i in range(n):
    if i<k:
        s+=a[i]
    else:
        t=s
        t+=a[i]
        t-=a[i-k]
        if t<s:
            s=t
            q=i
if n==k:
    print(1)
else:
    print(q-k+2)

n,t=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
b=[0]*(n+1)
for i in range(n+1):
    b[i]=b[i-1]+a[i-1]



for  _ in range(t):
    x,y=map(int,input().split())
     
    s=b[x]-b[x-y]
    print(s)

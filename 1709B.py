n,t=map(int,input().split())
a=list(map(int,input().split()))

for _ in range(t):
    c=0
    x,y=map(int,input().split())
    if x<y:
        for i in range(x-1,y-1):
            if a[i]>a[i+1]:
                c+=(a[i]-a[i+1])
    else:
        for i in range(x-1,y-1,-1):
            if a[i]>a[i-1]:
                c=c+a[i]-a[i-1]
    print(c)

fdshnxf::ytg
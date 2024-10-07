n,t=map(int,input().split())
n-=1
if 10**n + t>=10**n+1:
    print(-1)
else:
    m=10**n %t
    if 10**n +t-m<10**n+1:
        print(10**n +t-m)
    else:
        print(-1)

    
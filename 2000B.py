t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for i in range(n):
        if i==0:
            d[a[i]]=1
        else:
            if (a[i]-1 in d.keys() ) or (a[i]+1 in d.keys()):
                d[a[i]]=1
            else:
                print("NO")
                break
    else:
        print("YES")

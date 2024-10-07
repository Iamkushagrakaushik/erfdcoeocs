t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
     
    for i in range(n-1,-1,-1):
        if a[i] in d:
            break
        else:
            d[a[i]]=1
    else:
        i=-1
    print(i+1)
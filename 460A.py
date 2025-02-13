def cal(n,m):
    d=0
    while n>0:
        n-=1
        d+=1
        if d%m==0:
            n+=1
    return d
n,m=map(int,input().split())
print(cal(n,m))
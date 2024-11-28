import functools
def nn(n):
    return n//2
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for i in range(n):
        if a[i] in d:
            d[a[i]]+=1
        else:
            d[a[i]]=1
    c=0
    for i in d.values():
        c+=i//2
    print(c)
def pre(n):
    r=0
    if len(n)==1:
        if n[0]==0:
            r=1
    else:
        for i in range(len(n)):
            if n[i]==(sum((n[0:i]+n[i+1:]))):
                r= 1
    return r
t=int(input())
x=[0 for _ in range(t)]
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    for j in range(n):
        x[i]+=pre(l[:j])
for i in x:
    print(i)
        

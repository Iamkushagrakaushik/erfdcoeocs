x,n=map(int,input().split())
k=0
for _ in range(x):
    o,c=tuple(input().split())
    c=int(c)
    if o=='+':
        n+=c
    else:
        if n<c:
            k+=1
        else:
            n-=c
print(n,k,sep=" ")
    
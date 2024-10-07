t=int(input())
a=[]
for _ in range(t):

    l,m,n=tuple(map(int,input().split()))
    x=n
    if (l>m and l<=n) or (l>n and l<=m):
        x=l
    elif (m>l and m<=n) or(m>n and m<=l):
        x=m
    a.append(x)
for i in a:
    print(i)


     
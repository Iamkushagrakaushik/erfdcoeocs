t=int(input())
for _ in range(t):
    c=0
    n,s,m=map(int,input().split())
    
    l=[0]
    for _ in range(n):
        a=list(map(int,input().split()))
        l+=a
    l.append(m)
    x=0
    y=0
    for i in range(len(l)-1):
        y=l[i+1]-l[i]
        if y>x:
            x=y
    if x>=s:
        print("YES")
    else:
        print("NO")




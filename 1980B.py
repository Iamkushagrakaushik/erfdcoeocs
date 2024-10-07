t=int(input())
a=[]
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    x=sorted(l)
    for i in range(n):
        if l[i:]+l[:i]==x:
            a.append("YES")
            break
    else:
        a.append("NO")
for i in a:
    print(i)

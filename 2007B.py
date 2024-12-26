t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=max(map(int,input().split()))
    x=[]
    for _ in range(m):
        o,l,r=tuple(input().split())
        l=int(l)
        r=int(r)
        if l<=a and r>=a:
            if o=='+':
                a+=1
            else:
                a-=1
        x.append(a)
    for i in x:
        print(i,end=" ")
    print()
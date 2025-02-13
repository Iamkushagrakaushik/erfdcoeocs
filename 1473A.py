t=int(input())
for _ in range(t):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    # a.sort()
    # x,y=a[0],a[1]

    
    # if x+y<=d or not any(True for i in a if i>d):
    #     print("YES")
    # else:
    #     print("NO")
    
 
    x,y=float('inf'),float('inf')
    k=True
    xi=-1
    for i in range(n):
        if a[i]>d:
            k=False

        if a[i]<x:
            y=x
            x=a[i]
            xi=i
        elif i!=xi and i<y:
            y=a[i]
    
    if x+y<=d or k:
        print("YES")
    else:
        print("NO")
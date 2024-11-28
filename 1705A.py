t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=sorted(list(map(int,input().split())))
    p=[a[i] for i in range(n)]
    q=[a[i] for i in range(n,2*n)]
    for i in range(n):
        if q[i]-p[i]<x:
            print("NO")
            break
    else:
        print("YES")
     
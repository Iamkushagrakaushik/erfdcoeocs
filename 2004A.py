t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n==2 and a[0]+1!=a[1]:
        print("YES")
    else:
        print("NO")
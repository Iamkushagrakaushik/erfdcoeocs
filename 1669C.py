t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x,y=a[0]%2,a[1]%2
    for i in range(0,n,2):
        if a[i]%2!=x:
            print("NO")
            continue
    for i in range(1,n,2):
        if a[i]%2!=y:
            print("NO")
            break
    else:
        print("YES")
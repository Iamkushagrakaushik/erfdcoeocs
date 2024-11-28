t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n==1:
        if a[0]>1:
            print("NO")
        else:
            print("YES")
    else:
        a.sort()
        if a[-1]>a[-2]+1:
            print("NO")
        else:
            print("YES")
     

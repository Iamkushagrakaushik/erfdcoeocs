t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n-1):
        k=abs(a[i]-a[i+1])
        if k==5 or k==7:
            continue
        else:
            print("NO")
            break
    else:
        print("YES") 
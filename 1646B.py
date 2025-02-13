t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    i=n-1
    j=1
    a.sort()
    s=a[0]
    while j<i:
        s+=(a[j]-a[i])
        i-=1
        j+=1
        if s<0:
            print("YES")
            break
    else:
        print("NO")

    

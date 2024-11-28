t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    i,j=0,n-1
    o=i if a[i]>a[j] else j
    m=a[o]
    for _ in range(n):
        if a[i]>a[j]:
            if a[i]<=m:
                i-=1
        elif a[j]<=m:
            j-=1
        else:
            print("NO")
            break
    else:
        print("YES")

        
        




         



             


    
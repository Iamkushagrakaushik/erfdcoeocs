t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c=0
    for i in range(n):
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                c+=1
    k=n*(n-1)//2
    k-=1
    if c>(k):
        print("NO")
    else:
        print("YES")


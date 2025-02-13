t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s=float('inf')
    for i in range(n-1):
        if a[i]>a[i+1]:
            print(0)
            break
        if a[i+1]-a[i]<s:
            s=a[i+1]-a[i]
    else:
        print(s//2+1)




t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a))==1:
        print("NO")
        continue
    else:
        print("YES")
        a.sort(reverse=True)
        a[0],a[-1]=a[-1],a[0]
        for i in a:
            print(i,end=" ")
        print()

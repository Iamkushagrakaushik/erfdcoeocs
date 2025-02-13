t = int(input())
for _ in range(t):
    n,k = map(int,(input().split()))
    a = list(map(int, input().split()))
    c=0
    for i in range(n):
        for j in range(n):
            if (a[i]-a[j])%k==0 and i!=j:
                break
        else:
            print("YES")
            print(i+1)
            break
    else:
        print("NO")

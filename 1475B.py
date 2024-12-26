t=int(input())
for _ in range(t):
    n=int(input())
    k=n//2020
    n%=2020
    if n>k:
        print("NO")
    else:
        print("YES")

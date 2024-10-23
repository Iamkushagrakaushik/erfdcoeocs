t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=(n+1)//2
    b=(n-k+1)//2
    c=a-b
    if c%2==0:
        print("YES")
    else:
        print("NO")

           
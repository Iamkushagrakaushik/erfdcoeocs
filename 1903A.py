t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    s=0
    if a==sorted(a):
        c=1
    if c==1 or k>1:
        print("YES")
    else:
        print("NO")
        
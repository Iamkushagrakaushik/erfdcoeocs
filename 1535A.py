t=int(input())
for _ in range(t):
    a,b,c,d=(map(int,input().split()))
    if max(a,b)<min(c,d) or max(c,d)<min(a,b):
        print("NO")
    else:
        print("YES") 
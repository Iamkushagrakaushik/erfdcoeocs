t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if a>b:
        n=a
        a=b
        b=n
    
    if b<=a*(c+1):
        print("YES")
    else:
        print("NO")
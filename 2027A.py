t=int(input())
for _ in range(t):
    n=int(input())
    x,y=[],[]
    for _ in range(n):
        a,b=map(int,input().split())
        x.append(a)
        y.append(b)
    print(2*(max(x)+max(y)))
        
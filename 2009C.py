import math
t=int(input())
for _ in range(t):
    a,b,k=map(int,input().split())
    m=max(a,b)
    c=math.ceil(m/k)*2
    if a>b:
        c-=1
    print(c)
import math
t=int(input())

for _ in range(t):
    a,b,c=map(int,input().split())
    x=0
    if a==b:
        pass
    else:
        x=math.ceil(abs(a-b)/(2*c))

    print(x)
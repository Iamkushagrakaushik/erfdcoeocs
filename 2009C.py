import math
t=int(input())
for _ in range(t):
    a,b,k=map(int,input().split())
    x,y=(a+k-1)//k,(b+k-1)//k
    if x>y:
        print(2*x-1)
    else:
        print(2*y)
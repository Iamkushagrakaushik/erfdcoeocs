import math 
t=int(input())

a=[]
for _ in range(t):
    n,a,b=tuple(map(int,input().split()))
    if a<=b:
        a.append(math.ceil(n/a))
    else:
        
import math
t=int(input())
a=[]
for _ in range(t):
    n,x=map(int,input().split())
    c=1
    n=n-2
    if n>0:
        c+=math.ceil(n/x)
    a.append(c)
for i in a:
    print(i)
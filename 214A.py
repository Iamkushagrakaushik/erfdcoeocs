import math
n,m=map(int,input().split())
x=max(n,m)
t=int(math.sqrt(x))
 
c=0
for a in range(t+1):
    for b in range(t+1):
        if a**2 + b==n and b**2 + a==m:
            c+=1
print(c)
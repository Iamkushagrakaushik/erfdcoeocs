import math
n,k=map(int,input().split())
a=list(map(int,input().split()))
c,m=0,0
for i in range(n):
    if math.ceil(a[i]/k)>=m:
        m=math.ceil(a[i]/k)
        c=i+1
print(c)
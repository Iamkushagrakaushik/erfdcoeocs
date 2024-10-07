import math
t=int(input())

a=[]
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    for i in l:
        s+=i
    if math.sqrt(s)**2==s:
        a.append("YES")
    else:
        a.append("NO")
for i in a:
    print(i)
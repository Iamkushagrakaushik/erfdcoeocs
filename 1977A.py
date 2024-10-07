t=int(input())
c=[]
for _ in range(t):
    a,b=tuple(map(int,input().split()))
    if a>=b and (a-b)%2==0:
        c.append('YES')
    else:
        c.append('NO')
for i in c:
    print(i)
n=int(input()):

c=[]
for _ in range(n):
    a,b=tuple(map(int,input().split()))
    m=abs(b)-abs(a)
    if m>=abs(a) and b<0:
        c.append("NO")
    else:
        c.append("YES")
for i in c:

    print(i)

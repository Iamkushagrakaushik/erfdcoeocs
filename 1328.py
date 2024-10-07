n=int(input())
c=[]
for _ in range(n):
    a,b=tuple(map(int,input().split()))
    if a%b!=0:
        c.append(b-a%b)
    else:
        c.append(0)
for i in c:
    print(i)
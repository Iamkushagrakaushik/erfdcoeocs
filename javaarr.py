n=int(input())
l=[]
for _ in range(n):
    a=list(map(int,input().split()))
    l.append(a)
q=int(input())
m=[]
for _ in range(q):
    x,y=map(int,input().split())
    try:
        m.append(l[x-1][y])
    except Exception :
        m.append("ERROR!!!")
for i in m:
    print(i)
            
t=int(input())
a=[]
for _ in range(t):
    n,k=map(int,input().split())
    l=[]
    for _ in range(n):
        l.append(list(map(int,input().split())))
    m=[]
    for i in range(n):
        s=[]
        for j in range(0,n,k):
            s.append(l[j])
        m.append(s)
    a.append(m)
for i in a:
    for j in i:
        for k in j:
            print(k,end="")
        print()
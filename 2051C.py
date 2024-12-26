t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    k=list(map(int,input().split()))
    s=""
    ks=sum(k)
    ass=sum(a)
    su=((n+1)*n)//2
    if su==ks:
        print('1'*m)
        continue
    for i in a:
        if (su-i)==ks:
            s+='1'
        else:
            s+='0'
    print(s)
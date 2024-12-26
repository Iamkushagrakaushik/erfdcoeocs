t=int(input())
for _ in range(t):
    m,a,b,c=map(int,input().split())
    s=0
    m1,m2=m,m
    if m1>a:
        s+=a
        m1-=a
    else:
        s+=m1
        m1=0
        
    if m2>b:
        s+=b
        m2-=b
    else:
        s+=m2
        m2=0
        
    s+=(min(m1+m2,c))
    print(s)
    
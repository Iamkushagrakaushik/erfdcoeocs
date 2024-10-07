t=int(input())
for _ in range(t):
    m=0
    a,b,c,d=map(int,input().split())
    if a>c and b>d:
        m+=2
    if a>d and b>c:
        m+=2
    print(m)
    

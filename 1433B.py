t=int(input())
for _ in range(t):
    n=int(input())
    s="".join(input().split())
    f=0
    c=0
    x=s.index('1')
    for i in range(n-1,-1,-1):
        if s[i]=='1':
            y=i
            break
    for i in range(x,y):
        if s[i]=='0':
            c+=1
    
    print(c)


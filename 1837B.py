t = int(input())
for _ in range(t):
    n = int(input())
    s=input()
    c,m=0,0
    x,y=0,0
    for i in s:
        if i=='<':
            c+=1
            x=0
        else:
            c=0
            x+=1
        if c>m:
            m=c
        if x>y:
            y=x
    print(max(y,m)+1)
        
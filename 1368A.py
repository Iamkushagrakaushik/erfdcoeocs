t=int(input())
for _ in range(t):
    c=0
    a,b,n=map(int,input().split())
    while n>=a and n>=b:
        c+=1
        m=a+b
        if b>a:
            a=m
        else:
            b=m
    print(c)
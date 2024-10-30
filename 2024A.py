t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a>=b:
        print(a)
    else:
        a-=(b-a)
        if a>0:
            print(a)
        else:
            print(0)
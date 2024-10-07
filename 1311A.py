t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a>b:
        if abs(a-b)%2==1:
            print(2)
        else:
            print(1)
    elif b>a:
        if abs(a-b)%2==1:
            print(1)
        else:
            print(2)
    else:
        print(0)

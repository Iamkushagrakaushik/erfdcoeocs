t=int(input())
for _ in range(t):
    r=0
    n,a,b,c=map(int,input().split())
    if n>(a+b+c):
        r=n//(a+b+c)

        n%=(a+b+c)
    r*=3
    if n>a+b:
        print(r+3)
    elif n>a:
        print(r+2)
    elif n>0:
        print(r+1)
    else:
        print(r)

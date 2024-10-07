t=int(input())
for _ in range(t):
    n=int(input())
    a,b=0,0
    a=2**n+sum(2**i for i in range(1,n//2))
    b=sum(2**i for i in range(n//2,n))
    print(a-b)
t = int(input())
for _ in range(t):
    n = int(input())
    a,b=0,1
    for _ in range(n):
        c=a+b+1
        print(c,end=" ")
        a=b
        b=c
    print()

     

t=int(input())
for _ in range(t):
    n=int(input())
    m=0
    c=1
    for i in range(n):
        a,b=map(int,input().split())
        if a<=10 and m<b:
            m=b
            c=i+1
    print(c)

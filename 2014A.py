t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    r=0
    c=0
    for i in a:
        if i==0 and r>0:
            r-=1
            c+=1
        elif i>=k:
            r+=i
    print(c)
 
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    z=s//n
    if s%n==0:
        s1=sum([a[i] for i in range(0,n,2)])
        s2=sum([a[i] for i in range(1,n,2)])
        if s1//((n+1)//2)==z and s2//((n)//2)==z:
            print("YES")
        else:
            print("NO") 
    
    else:
        print("NO")
     
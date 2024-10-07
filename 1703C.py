t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        m=a[i]
        x=input().split()
        s=x[1]
        for j in s:
            if j=='D':
                m+=1
                m%=10
            else:
                if m==0:
                    m=9
                else:
                    m-=1
        a[i]=m
    for k in a:
        print(k,end=" ")
    print()

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c,m=0,0
    for i in range(2*n):
        j=i%n
        if a[j]<a[(j+1)%n]:
            c+=1
        else:
            c=0
        if c>m:
            m=c
    print(m)
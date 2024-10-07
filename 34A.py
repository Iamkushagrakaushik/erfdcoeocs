n=int(input())
a=list(map(int,input().split()))
if n<=2:
    print(1,2)
else:
    a.append(a[0])
    c=float('inf')
    for i in range(n):
        m=abs(a[i+1]-a[i])
        if m<c:
            c=m
    for i in range(n):
        m=abs(a[i+1]-a[i])
        if m==c:
            if i==n-1:
                print(n,1)
            else:
                print(i+1,i+2)
            break
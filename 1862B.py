t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    b.append(a[0])
    for i in range(1,n):
        if(a[i]>=a[i-1]):
            b.append(a[i])

        b.append(a[i])
    for i in b:
        print(i,end=" ")
    print()


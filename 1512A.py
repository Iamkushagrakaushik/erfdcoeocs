n=int(input())
x=[]
for _ in range(n):
    n=int(input())
    a=list(map(int,input().split()))
    if a[0]!=a[1] and a[1]==a[n-1]:
        x.append(1)
    elif a[n-1]!=a[0] and a[0]==a[n-2]:
        x.append(n)
    else :
        for i in range(1,n-1,1):
            if a[i]!=a[i+1] and a[i]!=a[i-1]:
                x.append(i+1)
                break
for i in x:
    print(i)

        
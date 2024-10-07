t=int(input())
a=[]
for _ in range(t):
    n=int(input())
    if n%4==0:
        x=["YES"]
        l=list(range(2,n+1,2))
        m=list(range(1,n,2))
        m[-1]+=n//2
        x=x+l+m
        a.append(x)
    else:
        a.append("NO")
for i in a:
    if len(i)==2:
        print(i,end="")
    else:
        print(i[0])
        for j in range(1,len(i)):
            print(i[j],end=" ")
    print()

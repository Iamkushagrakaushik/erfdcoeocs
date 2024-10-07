t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    l,m=min(a),max(a)
    i=0
    c=0
    o=0::::::::
    j=n-1
    while o<2:
        if a[i]==l or a[i]==m :
            o+=1
            i+=1
        elif a[j]==l or a[j]==m :
            o+=1
            j-=1
        else:
            i+=1
            j-=1
        c+=1
    print(c)
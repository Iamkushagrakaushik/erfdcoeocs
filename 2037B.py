 

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    m=n-2
    for i in range(n):
        if a[i]!=0 and m%a[i]==0:
            k=m//a[i]
            if k in d:
                print(k,a[i],sep=" ")
                break
        d[a[i]]=True

    


     
    
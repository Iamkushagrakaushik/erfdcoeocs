t=int(input())
x=[]
for i in range(t):
    n,f,k=tuple(map(int,input().split()))
    a=list(map(int,input().split()))
    if n==1:
        x.append("YES")
    else:
        y=[]
        n-=1
        f-=1
        k-=1
        m=a[f]
        a.sort(reverse=True)
        if a.count(m)==1:
            if m>=a[k]:
                x.append('YES')
            else:
                x.append("NO")
        else:
            if m>=a[k] and a[k:].count(m)>=2:
                x.append('MAYBE')
            elif m>=a[k] and a[k:].count(m)<2:

                x.append("YES")
            else:
                x.append("NO")

             
for i in x:
    print(i)



                
                
        

            

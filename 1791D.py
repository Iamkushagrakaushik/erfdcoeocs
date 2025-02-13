t = int(input())
for _ in range(t):
    n = int(input())
    s=input()
    x,y=set(),set(s)
    d={}
    for i in s:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    m=0


    for i in s:
        x.add(i)
        if d[i]==1:
            y.discard(i)
        d[i]-=1
        m=max(m,len(x)+len(y))
    print(m)

         

    
     





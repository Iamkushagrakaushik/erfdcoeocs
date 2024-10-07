t=int(input())
a=[]
for i in range(t):
     
    n=int(input())
    x=list(map(int,input().split()))
    m,c=0,0
    for j in x:
        if j==0:
            c+=1
            if c>m:
                m=c
        else:
            
            c=0
    a.append(m)
for i in a:
    print(i)

t=int(input())
x=[]
for _ in range(t):
    a,b,c=map(int,input().split())
    m=0
    i,j,k=0,0,0
    if a+b+c==0:
        x.append((1,1,1))
    else:


        m = max(a, b, c)
        if a!=m:
            i=m-a+1
        if b!=m:
            j=m-b+1
    
        if c!=m:
            k=m-c+1
        x.append((i,j,k))

    


for i,j,k in x:
    print(i,j,k,sep=" ")
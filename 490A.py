n=int(input())
a=list(map(int,input().split()))
x,y,z=0,0,0
for i in a:
    if i==1:
        x+=1
    elif i==2:
        y+=1
    else:
        z+=1
c=min((x,y,z))
print(c)
for _ in range(c):
    p,q,r=a.index(1)+1,a.index(2)+1,a.index(3)+1
         
    print(p,q,r,sep=" ")
    a[p-1],a[q-1],a[r-1]=0,0,0

    


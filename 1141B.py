n=int(input())
a=list(map(int,input().split()))
c,m=0,0
for i in a:
    if i==1:
        c+=1
    else:
        c=0
    if c>m:
        m=c
if c>0:
    
    for i in a:
        if i!=0:
            c+=1
        else:
            break
    if c>m:
        m=c
print(m)
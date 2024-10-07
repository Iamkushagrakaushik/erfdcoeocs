n=int(input())
a=list(map(int,input().split()))
o,z=0,0
c,m=0,0

for i in a:
    if i==1:
        if o<=1:
            o+=1
        c+=1
    else:
        if z==0:
            z+=1
            c+=1
        else:
         

       

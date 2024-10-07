import math
t=int(input())
a=list(map(int,input().split()))
w,x,y,z=0,0,0,0
s=0

for i in a:
    if i==1:
        w+=1
    elif i==2:
        x+=1
    elif i==3:
        y+=1
    else:
        z+=1
 
s+=z
if w>y:
    s+=w-y
    w-=y
else:
    s+=y
    w=0

s+=x//2
x//=2
if x>0:
    w+=2
s+=math.ceil(w/4)


print(s)
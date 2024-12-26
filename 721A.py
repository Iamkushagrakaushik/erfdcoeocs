n=int(input())
c,x=0,0
s=input()
a=[]
for i in s:
    if i=='B':
        c+=1
    else:
        if c>0:
            x+=1
            a.append(c)
            c=0
if s[-1]=='B':
    x+=1
    a.append(c)
print(x)
for i in a:
    print(i,end=" ")

n,d=tuple(map(int,input().split()))
a=list(map(int,input().split()))
c=0
for i in a:
    for j in a:
        if abs(i-j)<=d:
            c+=1
    c-=1
print(c)
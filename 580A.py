n=int(input())
a=list(map(int,input().split()))
c=1
m=1
for i in range(n-1):
    if a[i+1]<a[i]:
        
        c=1
    else:
        c+=1
        if c>m:
            m=c
        
print(m)
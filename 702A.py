n=int(input())
a=list(map(int,input().split()))
c=1
m=1

for j in range(1,n):
    if a[j]>a[j-1]:
        c+=1
    else:
        c=1
    if c>m:
        m=c

print(m)

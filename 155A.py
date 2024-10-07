n=int(input())
x=0
a=list(map(int,input().split()))
l,m=0,0
for i in range(1,n):
    if a[i]<a[l]:
        x+=1
        l=i
    elif a[i]>a[m]:
        x+=1
        m=i

print(x)

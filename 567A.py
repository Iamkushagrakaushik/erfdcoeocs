n=int(input())
a=list(map(int,input().split()))
x,y=a[0],a[-1]
print(a[1]-x,y-x)

for i in range(1,n-1,1):

    print(min(a[i]-a[i-1],a[i+1]-a[i]),max(a[i]-x,y-a[i]))
print(y-a[-2],y-x)

n,m,a,b=tuple(map(int,input().split()))
x=n//m
y=n%m
print(min(x*b+y*a,n*b))
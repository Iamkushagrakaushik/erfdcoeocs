a,b=tuple(map(int,input().split()))

if a>b:
    a,b=b,a
x,y=a,b
y=(a+b-(2*a))//2
print(x,y,sep=" ")

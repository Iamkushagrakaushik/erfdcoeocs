n,m=tuple(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
y=float('inf')
for i in range(m-n+1):
    x= a[i + n - 1] - a[i]
    if y>x:
        y=x
print(y)
n=int(input())
a=set(range(1,n+1))
x=list(map(int,input().split()))
y=list(map(int,input().split()))
p=set(x[1:])
q=set(y[1:])
z=p.union(q)

if z==a:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
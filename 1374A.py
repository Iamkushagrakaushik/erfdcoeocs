t=int(input())
a=[]
for _ in range(t):
    x,y,n=tuple(map(int,input().split()))
     
    m = (n - y) // x
    k = m * x + y
    a.append(k)
for i in a:
    print(i)
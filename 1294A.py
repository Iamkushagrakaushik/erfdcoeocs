x=[]
t=int(input())
for _ in range(t):
    a,b,c,n=map(int,input().split())
    z=max(a,b,c)
    n=n-(3*z-(a+b+c))
    if n>=0 and n%3==0:
        x.append("YES")
    else:
        x.append("NO")
for i in x:
    print(i)
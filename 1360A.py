t=int(input())
l=[]
for _ in range(t):
    x,y=map(int,input().split())
    if x>y:
        a,b=y,x
    else:
        a,b=x,y
    if 2*a>b:
        b+=1
    l.append(b**2)
for i in l:
    print(i)::::::
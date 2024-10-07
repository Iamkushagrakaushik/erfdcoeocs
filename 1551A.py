t=int(input())
a=[]
for _ in range(t):
    n=int(input())
    m=n//3
    r=n%3
    if r==0:
        a.append((m,m))
    elif r==1:
        a.append((m+1,m))
    else:
        a.append((m,m+1))
for i,j in a:
    print(i,j,sep=" ")

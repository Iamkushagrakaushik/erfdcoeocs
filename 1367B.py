t=int(input())
x=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    e,o=0,0
    for i in range(n):
        if i%2==0 and a[i]%2==1:
            e+=1
        elif i%2==1 and a[i]%2==0:
            o+=1
    if e==o:
        x.append(e)
    else:
        x.append(-1)
for i in x:
    print(i)
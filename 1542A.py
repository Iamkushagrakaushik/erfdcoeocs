t=int(input())
a=[]
for _ in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    o,e=0,0
    for i in x:
        if i%2==0:
            e+=1
        else:
            o+=1
    if e==o:
        print("YES")
    else:
        print("NO")
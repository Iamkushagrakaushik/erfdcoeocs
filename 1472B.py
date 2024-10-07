t=int(input())
a=[]:qeawrsdtfygjhk
for _ in range(t):
    m=int(input())
    n=list(map(int,input().split()))
    x,y=0,0
    for i in n:
        if i==1:
            x+=1
        else:
            y+=1
    if x%2==1 or y%2==1:
        a.append("NO")
    else:
        a.append("YES")

for i in a:
    print(i)
t=int(input())
for _ in range(t):
    c=[0,0]
    x=[1,1]
    n=int(input())
    s=input()
    for i in s:
        if i=='U':
            c[1]+=1
        elif i=='D':
            c[1]-=1
        elif i=='R':
            c[0]+=1
        else:
            c[0]-=1
        if c==x:
            print("YES")
            break
    else:
        print("NO")
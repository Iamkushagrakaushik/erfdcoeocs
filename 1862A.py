t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=["" for _ in range(m)]
    x="vika"
    d=0
    for _ in range(n):
        s=input()
        for i in range(m):
            a[i]+=s[i]
    for i in a:
        if x[d] in i:
            d+=1
        if d>3:
            print("YES")
            break
    else:
        print("NO")

        


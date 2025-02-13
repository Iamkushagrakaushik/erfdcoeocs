
t = int(input())
for _ in range(t):
     
    n,a,b=(map(int, input().split()))
    for i in range(a+1):
        t=n
        for j in range(i):
            t//=2
            t+=10
        t-=(b*10)
        if t<=0:
            print("YES")
            break
        else:
            continue
    else:
        print("NO")
    



t=int(input())
a=[]
for _ in range(t):
    w,h,n=tuple(map(int,input().split()))
    c=1
    while(True):
        if c>=n:
            break
        if w%2==0:
            w//=2
            c*=2
        elif h%2==0:
            h//=2
            c*=2
        else:
            break
    if c>=n:
        a.append("YES")
    else:
        a.append("NO")
for i in a:
    print(i)
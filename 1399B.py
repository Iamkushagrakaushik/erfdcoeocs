t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    am,bm=min(a),min(b)
    c=0
    for i in range(n):
        x=a[i]-am
        y=b[i]-bm
        c+=max(x,y)
    print(c)

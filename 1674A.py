t=int(input())
for _ in range(t):
    a,b,c,x,y=map(int,input().split())
    a-=x
    b-=y
    if a<0:
        c+=a
    if b<0 :
        c+=b
    if c<0:
        print("NO")
    else:

        print("YES")
t=int(input())
x,y=0,0
for _ in range(t):
    m,c=tuple(map(int,input().split()))
    if m>c:
        x+=1
    elif c>m:
        y+=1
if x>y:
    print("Mishka")
elif y>x:
    print("Chris")
else:
    print("Friendship is magic!^^")
t=int(input())

for _ in range(t):
    m=int(input())
    n=list(map(int,input().split()))
    x,y=n.count(1),n.count(2)
    y%=2
    if y==1:
        if x>1 and x%2==0:
            print("YES")
        else:
            print("NO")
    else:
        if x%2==0:
            print("YES")
        else:
            print("NO")

     
     

 
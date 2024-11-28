t=int(input())
a,b=0,0
for _ in range(t):
    x,y=tuple(input().split())
    if x=='P':
        a+=int(y)
    else:
        b=int(y)
        if b>a:
            print("YES")
            a=0
        else:
            print("NO")
            a-=b
        
            

        



t = int(input())
for _ in range(t):
     
    w,x,y,z=(map(int, input().split()))
    i=y-x
    c=1

    if w+x==i:
        c+=1
    if i+y==z:
        c+=1
    print(c)
    

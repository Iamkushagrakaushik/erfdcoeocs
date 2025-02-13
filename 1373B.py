t = int(input())
for _ in range(t):
    s=input()
    x,y,c=0,0,0
    for i in s:
        if i=='1':
            x+=1
        else:
            y+=1
        if x>0 and y>0:
            c+=1
            x-=1
            y-=1
    if c%2==0:
        print("NET")
    else:
        print("DA")

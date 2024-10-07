t=int(input())
for _ in range(t):
    s=[]
    for _ in range(8):
        a=input().strip()
        s.append(a)
    a=0
    p,q=0,0

    for i in range(8):
        c=0
        for j in range(8):
            if s[i][j]=='#':
                c+=1
        if c>=a:
            a=c
        else:
            p=i
            q=j

    print(p+1,q+1,sep=" ")

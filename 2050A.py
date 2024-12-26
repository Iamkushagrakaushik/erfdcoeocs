t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l=[]
    for _ in range(n):
        l.append(input())
     
    c=0
    for i in l:
        m-=len(i)
        if m<0:
            break
        c+=1
    print(c)

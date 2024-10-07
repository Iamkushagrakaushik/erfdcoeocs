def no(n):
    i=1
    a=1
    while(i<=n):
        if i%3==0 or i%10==3:
            a+=1
            
            continue
        a+=1
        i+=1
    return 
khyhgiikhbigxcigbsxKxcbK//CijxP[]][]
    
            
t=int(input())
a=[]
for _ in range(t):
    n=int(input())
    a.append(no(n))
for i in a:
    print(i)

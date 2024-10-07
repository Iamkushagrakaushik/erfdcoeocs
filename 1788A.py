t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=a.count(2)
    c=0
    for i in range(n):
        if a[i]==2:
            c+=1
        if c==s-c:
            print(i+1)
            break
    else:
        print(-1)
        

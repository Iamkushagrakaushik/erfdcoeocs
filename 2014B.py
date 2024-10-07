t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    c=0
    e,o=0,0
    for i in range(n-k+1,n+1):
        if i%2==1:
            o+=1
        
    if o%2==0:
        print("NO")
    else:
        print("YES"):       
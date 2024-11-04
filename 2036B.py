t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    d={}
    l=[0]*k
    c=0
    for _ in range(k):
        a,b=map(int,input().split())
        if l[a-1]==0:
            c+=1
            
        l[a-1]+=b
    l.sort(reverse=True)
    print(sum(l[0:min(c,n)]))

        
        
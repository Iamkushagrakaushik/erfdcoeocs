t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    c=0
    for i in a:
        if k>0:
            k-=i
            if k<0:
                print(i+k)
                break
        
    else:
        print(k)


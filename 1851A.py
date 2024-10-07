t=int(input())
for _ in range(t):
    count=0
    n,m,k,h=map(int,input().split())
    a=list(map(int,input().split()))
    for i in a:
        s=abs(h-i)
        c=(m-1)*k
        if s%k==0 and s<=c and i>0 and i!=h:
            count+=1
    print(count)
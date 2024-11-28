t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=a.count(1)
    m=(c+1)//2
    print(m+(n-c))
    

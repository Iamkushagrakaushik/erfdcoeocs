t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        if (i+1)==a[i]:
            c+=1
    print((c+1)//2)
    
     
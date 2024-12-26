t=int(input())
for _ in range(t):
    n=int(input())
    i=1
    p,q=0,0
    while(i*i<n):
        i+=1
    x=(i-1)**2
    x+=i
    if x>n:
        p=i
        q=x-((i-1)**2)+1
    else:
        p=i
        q=(i**2)-n+1

    print(p,q)
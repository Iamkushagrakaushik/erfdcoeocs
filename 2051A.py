t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    s=0
    b.append(0)
    for i in range(n):
        if a[i]>b[i+1]:
            s+=a[i]-b[i+1]
    print(s)
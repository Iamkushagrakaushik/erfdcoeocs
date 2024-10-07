t=int(input())
for _ in range(t):
    m=[]
    for _ in range(4):
        m+=list(map(int,input().split()))
    x=m[0]
    y=m[1]
    c=0
    for i in range(2,7,2):
        if x==m[i]:
            c=i
            break
    print(abs(y-m[c+1])**2)

t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    c=0
    for i in range(l,r+1):
        if i%2==1:
            c+=1
    print(c//2)
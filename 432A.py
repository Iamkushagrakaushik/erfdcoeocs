n,k=tuple(map(int,input().split()))

a=list(map(int,input().split()))
a.sort()
c=0
for i in range(0,n,3):
    if max(a[i:i+3])<=5-k:
        c+=1
print(c)

    wceyvgdwabh:avcgbhdnjL

n,k=tuple(map(int,input().split()))
if k<=n//2:
    print(k*2-1)
else:
    if n%2==0:
        print(((k-n//2)+1)*2)
    else:
        print(((k-n//2))*2)

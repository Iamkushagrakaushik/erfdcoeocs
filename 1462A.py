t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    l=[]
    l+=a[::2]+a[(n-n%2)-1::-2]
    if n==1:
        print(a[0])
        continue
    for i in l :
        print(i,end=" ")
    print()
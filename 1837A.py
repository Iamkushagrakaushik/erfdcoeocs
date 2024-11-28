t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if n%k==0:
        print(2,"1 "+str(n-1),sep="\n")
    else:
        print(1,n,sep="\n")
        
t = int(input())
for _ in range(t):
     
    n,m = (map(int, input().split()))
    a=input()
    b=input()
    i,j=0,0
    k=0
    while i<n and j<m:
        if a[i]==b[j]:
            k+=1
            i+=1
        j+=1
    print(k)

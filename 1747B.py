t = int(input())
for _ in range(t):
    n = int(input())
    m=(n+1)//2
    i,j=1,3*n
    if n==1:
        print(1)
        print(1,2)
        continue
    print(m)
    for x in range(m):
        print(i,j)
        i+=3
        j-=3
        


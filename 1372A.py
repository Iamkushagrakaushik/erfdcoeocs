t = int(input())
for _ in range(t):
    n = int(input())
    c=0
    i=0
    while(i<n):
        c=i
        if i%2==0:
            c=i+1
        print(c,end=" ")
        i+=1
    print()

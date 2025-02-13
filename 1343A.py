t = int(input())
for _ in range(t):
    n = int(input())
    i=2
    s=3
    while True:
        if n%s==0:
            print(n//s)
            break
        else:
            s+=(2**i)
            i+=1


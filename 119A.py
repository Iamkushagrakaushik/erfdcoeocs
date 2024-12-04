def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
a,b,c=map(int,input().split())
i=0
while True:
    if i%2==0:
        c-=(gcd(a,c))
        if c<0:
            print(1)
            break
    else:
        c-=(gcd(b,c))
        if c<0:
            print(0)
            break
    i+=1



import math
def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

    

t=int(input())
a=[]
n=list(map(int,input().split()))
for i in n:
    x=math.sqrt(i)
    if x==math.floor(x) and isprime(int(math.floor(x))):
        a.append("YES")
    else:
        a.append("NO")

for i in a:
    print(i)





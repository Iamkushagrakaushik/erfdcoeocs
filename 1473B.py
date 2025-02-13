import math
def lcm( a, b):
    return a*b//math.gcd(a,b)
t=int(input())

for _ in range(t):
    s=input()
    u=input()
    lm=lcm(len(s),len(u))
    x,y=s*(lm//len(s)),u*(lm//len(u))
    if x==y:
        print(x)
    else:
        print(-1)
     
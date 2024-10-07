n=int(input())
s=0
a=n//100
n=n-100*a
b=n//20
n=n-20*b
c=n//10
n=n-10*c
d=n//5
n=n-5*d
s=a+b+c+d+n
print(s)
"""n = int(input())
denominations = [100, 20, 10, 5, 1]
s = 0

for denom in denominations:
    s += n // denom
    n %= denom

print(s)
"""
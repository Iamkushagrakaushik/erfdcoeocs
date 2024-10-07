n=int(input())
c=0
m=0
for _ in range(n):
    a,b=tuple(map(int,input().split()))
    c=c-a
    c=c+b
    if c>m:
        m=c
print(m)
    
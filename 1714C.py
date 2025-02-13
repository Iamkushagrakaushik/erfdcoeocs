t = int(input())
for _ in range(t):
    n = int(input())
    s=""
    i=9
    while n-i>0:
        s+=str(i)
        n-=i
        i-=1
    if n>0:
        s+=str(n)
    print(s[::-1])
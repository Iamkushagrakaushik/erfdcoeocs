t=int(input())
for _ in range(t):
    a=int(input())
    l=list(map(int,input().split()))
    s=set(l)
    f=[l.count(i) for i in s]
    print(a-max(f))
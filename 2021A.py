import functools
t=int(input())
for _ in range(t):
    n=int(input())
    a=sorted(list(map(int,input().split())))
    s=functools.reduce(lambda a,b:(a+b)//2,a)
    print(s)
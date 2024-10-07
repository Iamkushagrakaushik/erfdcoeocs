n=int(input())
x=[]
for _ in range(n):
    a=0
    n,m=tuple(map(int,input().split()))
    s=input()
    if s.count('A')<m:
        a+=m-s.count('A')
    if s.count('B')<m:
        a+=m-s.count('B')
    if s.count('C')<m:
        a+=m-s.count('C')
    if s.count('D')<m:
        a+=m-s.count('D')
    if s.count('E')<m:
        a+=m-s.count('E')
    if s.count('F')<m:
        a+=m-s.count('F')
    if s.count('G')<m:
        a+=m-s.count('G')
    x.append(a)
for i in x:
    print(i)
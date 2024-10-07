t=int(input())
x=[]
for _ in range(t):
    a,b,c=tuple(map(int,input().split()))
    if a+b==c:
        x.append('+')
    else:
        x.append('-')
for i in x:
    print(i)
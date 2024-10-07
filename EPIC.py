t=int(input())
x=[]
for _ in range(t):
    a,b=tuple(map(int,input().split()))
    x.append(b*(a-1)+1)
for i in x:
    print(i)
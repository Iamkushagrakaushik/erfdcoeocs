t=int(input())
x=[]
for _ in range(t):
    a,b,c=tuple(map(int,input().split()))
    if a-1<abs(b-c)+c-1:
        x.append(1)
    elif a-1>abs(b-c)+c-1:
        x.append(2)
    else:
        x.append(3)
for i in x:
    print(i)

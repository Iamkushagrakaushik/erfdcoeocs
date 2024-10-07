t=int(input())
a=[]
for _ in range(t):
    n=int(input())
    if n%4==0:
        a.append(n//4)
    else:
        a.append(n//4 +1)
for i in a:
    print(i)
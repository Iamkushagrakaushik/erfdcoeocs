t=int(input())
a=[]
for _ in range(t):
    n=int(input())
    if n%2==0:
        a.append(n//2)
    else:
        a.append(n//2 +1)
for i in a:
    print(i)
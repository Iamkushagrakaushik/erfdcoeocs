n=int(input())
a,b=[],[]
for _ in range(n):
    d=input().split()
    a.append(int(d[0]))
    b.append(int(d[1]))
c=0
for i in a:
    for j in b:
        if i==j:
            c+=1
print(c)

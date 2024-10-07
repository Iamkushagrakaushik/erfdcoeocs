t=int(input())
a=[]
for _ in range(t):
    n=int(input())
    x=[]
    for _ in range(n):
        s=input()
        x.append(s.index('#')+1)
    x.reverse()
    a.append(x)
for i in a:
    for j in i:
        print(j,end=" ")
    print()


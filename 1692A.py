n=int(input())
x=[]
for _ in range(n):
    c=0
    a,*n=tuple(map(int,input().split()))
    for i in n:
        if i>a:
            c+=1
    x.append(c)
for i in x:
    print(i)
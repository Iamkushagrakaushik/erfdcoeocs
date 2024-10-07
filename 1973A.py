t=int(input())
w=[]
for _ in range(t):
    a,b,c=tuple(map(int,input().split()))
    if (a+b+c)%2!=0:
        w.append(-1)
    elif  a+b<=c:
        w.append(a+b)
    else:
       
        w.append((a+b+c)//2)
for i in w:
    print(i)
        
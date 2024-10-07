s,n=tuple(map(int,input().split()))
d=[]
for _ in range(n):
    x,y=tuple(map(int,input().split()))
    d.append([x,y])
x=sorted(d,key=lambda x:x[0])
for i in x:
    if s<i[0]:
        print("NO")
        break
    else:
        s+=i[1]
else:
    print("YES")
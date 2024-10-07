n=int(input())
x=[]
for _ in range(n):
    a,b,c=tuple(map(int,input().split()))
    if a+b==c or b+c==a or a+c==b:
        x.append("YES")
    else :
        x.append("NO")
for i in x:
    print(i)
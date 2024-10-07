n=int(input())
x=[]
for _ in range(n):
    x+=list(map(int,input().split()))
if (sum(x[0:len(x):3])==0 and (sum(x[1:len(x):3])==0 and sum(x[2:len(x):3])==0)):
    print("YES")
else:
    print("NO")
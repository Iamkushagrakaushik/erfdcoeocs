x=list(map(int,input().split()))
x.sort()
p=x[3]-x[0]
q=x[3]-x[1]
r=x[3]-x[2]
print(p,q,r,sep=" ")



a=list(map(int,input().split()))
a.sort()
m=a[1]
print(abs(m-a[0])+abs(m-a[2]))
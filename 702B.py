i=1
s=set()
x=10**10
while i<(x):
    i*=2
    s.add(i)
n=int(input())
c=0
a=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if a[i]+a[j] in s:
            c+=1
print(c)
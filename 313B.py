s=input()
n=len(s)
x=[]
a=[0]*n
t=int(input())
for i in range(1,n):
    a[i]=a[i-1]
    if s[i]==s[i-1]:
        a[i]+=1

for _ in range(t):
    
    l,u=tuple(map(int,input().split()))
    c=a[u-1]-a[l-1]
    x.append(c)
for i in x:
    print(i)
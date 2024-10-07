n=int(input())
a=list(map(int,input().split()))
s=0
m=0
for i in range(n):
    m+=a[i]
    if m<s:
        s=m
    
print(s*-1)
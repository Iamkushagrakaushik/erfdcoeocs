n=int(input())
c=0
for _ in range(n):
    a,b=tuple(map(int,input().split()))
    if a<(b-1):
        c+=1
print(c)

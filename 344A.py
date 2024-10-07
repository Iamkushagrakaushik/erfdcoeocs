n=int(input())
a=[]
c=1
for _ in range(n):
    a.append(input())
for i in range(n-1):
    if a[i][1]==a[i+1][0]:
        c+=1 
print(c)
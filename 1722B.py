t=int(input())
a=[]
for _ in range(t):
    n=int(input())
    m=input().replace('B','G')
    l=input().replace('B','G')
     
    if l==m:
        a.append("YES")
    else:
        a.append("NO")
for i in a:
    print(i)
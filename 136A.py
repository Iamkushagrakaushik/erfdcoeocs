n=int(input())
s=list(map(int,input().split()))
a=[]
for i in range(1,n+1):
    a.append(s.index(i)+1)
for i in a:
    print(i,"",end="")
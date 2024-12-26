n=int(input())
a=list(map(int,input().split()))
d={}
x=[]
for i in a[::-1]:
    if i not in d:
        d[i]=1
        x.append(i)
for i in x[::-1]:
    print(i,end=" ")

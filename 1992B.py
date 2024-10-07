t=int(input())
x=[]
for _ in range(t):
    n,k=tuple(map(int,input().split()))
    a=list(map(int,input().split()))
    a.remove(max(a))
    c=0
    for i in a:
            c+=2*i-1
    
    x.append(c)
for i in x:
    print(i)

 

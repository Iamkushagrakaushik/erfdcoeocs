t=int(input())
a=[]
n=list(map(int,input().split()))
q=int(input())
for _ in range(q):
    c=0
    x=int(input())
    for i in n:
        if x>=i:
            c+=1
        
    a.append(c)
for i in a:
    print(i) 

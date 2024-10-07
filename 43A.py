n=int(input())
d={}
a=""
c=0
max=0
for _ in range(n):
    s=input()
    if s in d:

        d[s]+=1
        
    else:
        d[s]=1
    if d[s]>max:
            max=d[s]
            a=s
print(a)
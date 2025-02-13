n=int(input())
s=input()
d={}
for i in range(n-1):
    if s[i:i+2] in d:
        d[s[i:i+2]]+=1
    else:
        d[s[i:i+2]]=1
m,c=0,0
for i in d:
    if d[i]>m:
        m=d[i]
        c=i
print(c)
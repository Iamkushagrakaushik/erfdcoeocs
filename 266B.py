n,t=tuple(map(int,input().split()))
a=[]
s=[]
s1=input()
for i in s1:
    s.append(i)
for _ in range(t):
    for i in range(n-1):
        if s[i]=='B' and s[i+1]=='G':
            a.append(i)
    for j in a:
        s[j]='G'
        s[j+1]='B'
k=''
for i in s:
    k+=i

print(k)
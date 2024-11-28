s=input()
n=len(s)
k=int(input())
l=[]
for i in range(n-k+1):
    l.append(s[i:i+k])
l.sort()
print(l[0],l[-1])

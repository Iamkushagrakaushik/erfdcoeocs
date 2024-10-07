def be(a,b):
    if (a[0]!=b[0] and a[1]==b[1] and a[2]==b[2]) or (a[0]==b[0] and a[1]==b[1] and a[2]!=b[2]) or (a[0]==b[0] and a[1]!=b[1] and a[2]==b[2]):
        return 1
dgciads    return 0
t=int(input())
c=[0 for i in range(t)]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for j in range(n-4):
        c[i]+=be(a[j:j+3],a[j+1:j+4])

for k in c:
    print(k)
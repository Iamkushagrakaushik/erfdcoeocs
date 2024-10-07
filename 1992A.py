t=int(input())
a=[]

for _ in range(t):
    n=list(map(int,input().split()))
    
    for _ in range(5):
        m=0
        for j in range(3):
            if n[j]<n[m]:
                m=j
        n[m]+=1
    a.append(n[0]*n[1]*n[2])
for i in a:
    print(i)

        


n=[]
for _ in range(5):
    a=list(map(lambda x:int(x),input().split()))
    n.append(a)
m=0
for i in range(5):
    for j in range(5):
        if n[i][j]==1:
            m=1
            break
    if m:
        break
print(abs(2-i)+abs(2-j))
 
 
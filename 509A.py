n=int(input())
s=[[1]*n]*n
for i in range(1,n):
    for j in range(1,n):
        s[i][j]=s[i-1][j]+ s[i][j-1]
print(s[-1][-1])

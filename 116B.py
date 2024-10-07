m,n=tuple(map(int,input().split()))
l=[]
c=0
for i in range(m):
    l.append(list(map(str,input().split())))
for i in range(m):
    for j in range(n):
        if l[i][j]=='P':
            if i!=0 and j!=0:
                if l[i][j-1]=='W' or l[i+1][j]=='W' or l[i][j+1]=='W' or l[i-1][j]=='W':
                    c+=1
            elif i==0 and j!=0:
                if l[i][j-1]=='W' or l[i+1][j]=='W' or l[i][j+1]=='W':
                    c+=1
            elif i!=0 and j==0:

            

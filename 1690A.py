t=int(input())
for _ in range(t):
    n=int(input())
    m=n//3
    r=n%3
    if r==0:
        print(m,m+1,m-1,sep=" ")
    elif r==1:
        if m==2:
            print(m,m+2,m-1,sep=" ")
        else:

            print(m+1,m+2,m-2,sep=" ")
    else:
        print(m+1,m+2,m-1,sep=" ")
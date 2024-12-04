def syst(a,b,s):
    if a==0:
        return s
    s+=str(a%b)+" "
    return syst(a//b,b,s)    
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if k==1:
        print(n)
    else:
        print(sum(map(int,syst(n,k,""))))

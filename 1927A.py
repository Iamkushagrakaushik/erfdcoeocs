t=int(input())
a=[]
for _ in range(t):
    n=int(input())
    s=input()
    if s.count("B")==1:
        a.append(1)
    else:
        x,y=0,0
        for i in range(n):
            if s[i]=="B":
                x=i
                break
        for i in range(n-1,-1,-1):
            if s[i]=='B':
                y=i
                break
        a.append(y-x+1)

for i in a:
    print(i)
        

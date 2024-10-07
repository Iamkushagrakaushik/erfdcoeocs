n=int(input())
for _ in range(n):
    a=[]
    for i in range(10):
        s=input()
        a.append(s)
    b,c,d,e,f=0,0,0,0,0
    for i in range(10):
        for j in range(10):
            if a[i][j]=='X':
                if i==0 or i==9 or j==0 or j==9:
                    b+=1
                elif i==1 or i==8 or j==1 or j==8:
                    c+=1
                elif i==2 or i==7 or j==2 or j==7:
                    d+=1
                elif i==3 or i==6 or j==3 or j==6:
                    e+=1
                else:
                    f+=1
    print(b+c*2+d*3+e*4+f*5)


    

t=int(input())
a=[]
for _ in range(t):
    x=-1
    c=0
    n=int(input())
    if n==1:
        a.append(0)
    else:
        while(True):
            if n%3!=0:
                if n==1:
                    x+=1
                
                    break
                else:
                    a.append(-1)
                    c=1
                break

            if n%2==0:
                n//=6
            else:
                n*=2
            x+=1
        if c==0:
            a.append(x)
for i in a:
    print(i)
    
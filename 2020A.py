;;;"""time limit exceeded 
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if k==1 or k>n:
        print(n)
    else:
        d={}
        i=1
        o=k
        while True:
            if k<=n:
                d[i]=k
                i+=1
                k*=o
          
            
            else:
                break
         
        i=len(d)
        c=0
        while True:
            if n==1:
                c+=1
                break
            
            if d[i]>n:
                if i==1:
                    c+=n
                    break

                i-=1
            else:
                n-=d[i]
                c+=1
                if n==0:
                    break
        print(c)
"""






            
        
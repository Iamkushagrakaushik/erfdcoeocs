t=int(input())
a=[]
for _ in range(t):
    n=int(input())
    i=0
    while(n>0):
        if i%3!=0 and i%10!=3:
            n-=1
        i+=1
    a.append(i-1)
for i in a:
    print(i)
t=int(input())
'''input is in string this code add digits of a large number ie 1234-> 1234+123+12+1=1370'''
a=[]
for _ in range(t):
    x=int(input())
    n=input()
    o=""
    sum=0
    for i in range((len(n)-1),-1,-1):
        t=int(n[i])
        for j in range(0,i):
            t=t+int(n[j])
        t+=sum
        r=t%10
        o+=str(r)
        sum=t//10
    if(sum!=0):
        o+=str(sum)
    a.append(o[::-1])
for i in a:
    
    print(i.lstrip('0'))
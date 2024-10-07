a=input()
b=input()
c=input()
d=["+",'*']
s=eval(a+"*"+b+"*"+c)

for i in d:
    for j in d:
        if i=="+" and j!='+':
            x=int(a)+int(b)
            k=x*int(c)
        elif j=="+" and i!='+':
            x=int(c)+int(b)
            k=x*int(a)
        else:
            k=eval(a+i+b+j+c)
        
        if k>s:
            s=k
print(s)
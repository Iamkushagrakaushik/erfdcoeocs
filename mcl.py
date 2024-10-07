

t=int(input())
s=[]

for i in range(t):
    x,z="",""
    n=int(input())
    a=input()
    
    for j in range(n):
       z=str(eval(x+"+"+a[0:n-j]))
       x=z
    k=z.lstrip('0')
    s.append(k) 

print(s)

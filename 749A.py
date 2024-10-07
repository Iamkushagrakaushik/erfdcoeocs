n=int(input())
c=n//2
print(c)
if n%2==0:
    s="2 "*c
    
else:
    s="2 "*(c-1)+"3"
print(s.strip())
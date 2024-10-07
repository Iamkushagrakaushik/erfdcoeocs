n=int(input())
a=input()
b=input()
c=0
for i in range(n):
    x=abs(int(a[i])-int(b[i]))
    y=10-x
    c=c+min(x,y)
print(c)
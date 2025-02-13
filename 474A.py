s="qwertyuiopasdfghjkl;zxcvbnm,./"
d={}
for c,i in enumerate(s):
    d[i]=c
m=input()
c=1 if m=='R' else -1
x=input()
z=""
for i in x:
    z+=s[d[i]-c]
print(z)

    
s=input()
a=[]
for i in range(len(s),2):
    a.append(int(s[i]))
a.sort()
a=list(map(str,a))
r='+'.join(a)
print(a)
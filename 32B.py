s=input()
a=""
n=len(s)
i=0
while i<n:
    if s[i]=='.':
        a+='0'
        i+=1
    else:
        if s[i]+s[i+1]=='-.':
            a+='1'
        else:
            a+='2'
        i+=2
print(a)
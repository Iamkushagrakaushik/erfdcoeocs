s=input()
v="aeiouy"
c=""
for i in s:
    if i.lower() in v:
        c+=""
    else:
        c+='.'
       
        c+=i.lower()
print(c)

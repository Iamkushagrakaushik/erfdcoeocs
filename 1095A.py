n=int(input())
s=input()
i=0
m=""
j=0
while i+j<n:
    i+=j
    m+=s[i]
    j+=1
print(m)
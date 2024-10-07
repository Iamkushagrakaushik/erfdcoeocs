n=int(input())
s=input()
c=0
for i in range(n-1):
    if s[i:i+2]=='RR' or s[i:i+2]=='GG' or s[i:i+2]=='BB':
        c+=1
print(c)

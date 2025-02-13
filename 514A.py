s=input()
m=[i if int(i)<5 else str(9-int(i)) for i in s]
m[0]='9' if m[0]=='0' else m[0]
print("".join(m))
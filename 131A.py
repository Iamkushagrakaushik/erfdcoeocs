s=input()
if len(s)==1:
    print(s.swapcase())
else:
    if (s[0].islower() and s[1:len(s)].isupper()) or s.isupper():
        print(s.swapcase())
    else:
        print(s)
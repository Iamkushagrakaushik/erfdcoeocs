s=input()
n=len(s)
f=0
c=0
for i in range(n):
    if s[i]!='1' and s[i]!='4':
        print("NO")
        break
    else:
        if i==0:
            if s[i]!='1':
                print("NO")
                break
        else:
            if s[i]=='4':
                if f==0:
                    f=1
                    c+=1
                    continue
                else:
                    c+=1
                    if c>2:
                        print("NO")
                        break
            else:
                c=0
                f=0
else:
    print("YES")


            
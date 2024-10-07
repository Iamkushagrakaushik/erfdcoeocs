m=input()
s=str(m.count('4')+m.count('7'))

def luck(s):
    for i in s:
        if i!='4' and i!='7':
            print("NO")
            break
    else:
            print("YES")
    
luck(s)
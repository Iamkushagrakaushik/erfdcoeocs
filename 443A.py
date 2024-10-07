x=input()
if x=="{}":
    print(0)
else:    
    s=set(x[1::3])
    print(len(s))
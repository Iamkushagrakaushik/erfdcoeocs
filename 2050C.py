t=int(input())
for _ in range(t):
    v=input()
    d={str(i):0 for i in range(10)}
    for i in v:
        
        d[i]+=1
        
    s=0
    for i in d.keys():
        s+=int(i)*d[i]
    if d["3"]+d['9']==len(v):
        print("YES")
        continue    
    match (s%9):
        case 0:
            print("YES")
        case 1:
            if d['2']>3 or (d['3']>0 and d['2']>0) or d["3"]>2 or d["2"]>8:
                print("YES")
            else:
                print("NO")
        case 2:
            if (d['2']>1 and  (d['3']>0))or d["2"]>7 :
                print("YES")
            else:
                print("NO")

        case 3:
            if d['2']>2 or (d['3']>0):
                print("YES")
            else:
                print("NO")
        case 4:
            if d["2"]>6 or (d[2]>0 and d["3"]>1) :
                print("YES")
            else:
                print("NO")
        case 5:
            if  d['2']>1 :
                print("YES")
            else:
                print("NO")
         
        case 7:
            
            if  d['2']>0 :
                print("YES")
            else:
                print("NO")
        case 8:
            if d["3"]>2:
                print("YES")
            else:
                print("NO")

        case _:
            print("NO")



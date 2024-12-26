t=int(input())
for _ in range(t):
    s=[]
    for _ in range(3):
        s.append(input())
    if len(set(s[1][1]+s[0][0]+s[2][2]))==1 or len(set(s[1][1]+s[0][2]+s[2][0]))==1:
        if s[1][1]=='.':
            print("DRAW")
        else:


            print(s[1][1])
            continue
    for i in range(3):
        m=""
        n=""
        for j in range(3):
            m+=s[i][j]
            n+=s[j][i]
        if len(set(m))==1:
            if m[0]=='.':
                print("DRAW")
            else:


                print(m[0])
            break
        if len(set(n))==1:
            if n[0]=='.':
                print("DRAW")
            else:


                print(n[0])
            break
     
        
    

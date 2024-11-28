t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    d=0
    f=0
    a=ord('a')
    if s.isdigit() or s.islower():
        for i in s:
            
            
            if i.isdigit():
                if d>int(i) or f==1 :
                   print("NO")
                   break
                else:
                    
                    d=int(i) 
            else:
                f=1
                if ord(i)<a :
                    print("NO")
                    break
                else:
                    f=1
                    a=ord(i)
             
        else:
            print("YES")
    else:
        print("NO")
         
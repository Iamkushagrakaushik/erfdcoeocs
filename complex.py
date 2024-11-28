# import cmath
# s=input()
# if '+' in s[1:]:
#     l=s.split('+')
# else:
#     if s[0]=='-':
#         l=s[1:].split('-')
#         l[0]=int(l[0])*(-1)
#     else:
#         l=s.split('-')
#         l[1]=int(l[1])*(-1)
        
        
    
# x=int(l[0])
# if len(l[1])<3:
#     y=int(l[1][0])
# else:
#     y=int(l[1][:len(l[1])-1])
# print(x,y,sep=" ")

    
    


 
 

# print(abs(complex(x,y)))
# print(cmath.phase(complex(x,y)))

        
n=int(input())
x=set(map(int,input().split()))
q=int(input())
for _ in range(q):
    
    s=input()
    
    if s=='pop':
        x.pop()
         
    try:
        if "remove" in s:
            x.remove(int(s[-1]))
        elif "discard" in s:
            x.discard(int(s[-1])) 
    except KeyError:
        continue
    else:
        continue
m=hash(x)
 
        
    
print(sum(x))

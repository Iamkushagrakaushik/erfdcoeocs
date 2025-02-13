t=int(input())
for _ in range(t):
    s=input()
    x,y=s.find('1'),s.rfind('1')
    print(s[x:y].count('0'))


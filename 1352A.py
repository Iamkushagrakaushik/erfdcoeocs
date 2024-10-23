t=int(input())
a=[] 
for _ in range(t):
    x=[]
    i=0
    n=int(input())
    while(n>0):
        r=n%10
        if r!=0:
        
            x.append(r*(10**i))
            
        n//=10
        i+=1
    x.append(i)
    a.append(x)
for i in range(len(a)):
    for j in range(len(a[i])-1):
        if j==0:
            print(len(a[i])-1)
        print(a[i][j]," ",end="")
    print()


'''the below code is gpt generated but above one also works '''





t = int(input())  # Read number of test cases
for _ in range(t):
    n = input().strip()  # Read the number as a string
    components = []

    for i, digit in enumerate(reversed(n)):
        if digit != '0':
            components.append(int(digit) * (10 ** i))

    print(len(components))  # Print the count of non-zero components
    print(" ".join(map(str, components)))  # Print the non-zero components

 






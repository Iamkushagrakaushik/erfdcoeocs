def leap(n):
    if (n%4==0 and n%100!=0) or n%400==0:
        return ("leap")
    else:
        return ("no leap")
n=int(input())
print(leap(n))
while False:
    num1=int(input("enter number 1   "))
    num2=int(input("enter number 2   "))
    o=input("enter operator +  !  -  !  *  !  /  ")
    if o=='+':
        print("sum of the numbers is ",num1+num2)
    elif o=='-':
        print("difference of the numbers is ",num1-num2)
    elif o=='*':
        print("product of the numbers is ",num1*num2) 
    elif o=='/':
        print("division of the numbers is ",num1/num2)       
    else:
        print("input error")
    n=n-1
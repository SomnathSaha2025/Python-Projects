operator=input("Enter an operator (+ - * /): ")
num1=float(input("Enter the 1st no.: "))
num2=float(input("Enter the 2nd no.: "))
if operator=="+":
    print(num1+num2)
elif operator=='-':
    print(num1-num2)
elif operator=='*':
    print(num1*num2)
elif operator=='/':
    print(num1/num2)
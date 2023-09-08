operator = input("Enter the Operator : ")
num1 = int(input("Enter the First Number value : "))
num2 = int(input("Enter the Second Number value : "))

if operator == '+':
    print(num1,"+",num2,"=",num1+num2)
elif operator == '-':
    print(num1,"-",num2,"=",num1-num2)
elif operator == '*':
    print(num1,"*",num2,"=",num1*num2)
elif operator == '/':
    print(num1,"/",num2,"=",num1/num2)
elif operator == '**':
    print(num1,"**",num2,"=",num1**num2)
else:
    print("Wrong operator enterd")

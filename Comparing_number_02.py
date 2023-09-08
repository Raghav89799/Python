num1 = int(input("Enter the First Number value : "))
num2 = int(input("Enter the Second Number value : "))
num3 = int(input("Enter the Third Number value : "))

if num1 > num2:
    higher_result = num1
    lower_result = num2
else:
    higher_result = num2
    lower_result = num1

if num3 > higher_result:
    print(num3,"is the highest")
else:
    print(higher_result,"is the highest")

if num3 > lower_result:
    print(lower_result,"is th lowest")
else:
    print(num3,"is the lowest")

